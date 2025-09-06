"""Component extractor for extracting components from Figma files."""

from typing import Dict, Any, Optional
from ..core.api_client import FigmaAPIClient
from ..utils.file_handler import FileHandler
import sys
from pathlib import Path

# Add config to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'config'))

from settings import KEEP_FIELDS


class ComponentExtractor:
    """Extractor for Figma components."""
    
    def __init__(self, api_client: FigmaAPIClient):
        """Initialize the component extractor.
        
        Args:
            api_client (FigmaAPIClient): Figma API client instance
        """
        self.api_client = api_client
        self.file_handler = FileHandler()
    
    def extract(self, node_id: Optional[str] = None, file_key: str = None) -> Dict[str, Any]:
        """Extract components from Figma file.
        
        Args:
            node_id (str, optional): Specific node ID to extract
            file_key (str, optional): Figma file key
            
        Returns:
            dict: Extracted component data
        """
        if node_id:
            # Extract specific node
            data = self.api_client.get_file_nodes(node_id, file_key)
            
            # Save raw data
            self.file_handler.save_json(data, 'extract_figma_component_tokens.json')
            
            # Process the specific node
            node_id_json = node_id.replace('-', ':')
            if 'nodes' in data and node_id_json in data['nodes']:
                raw_node = data['nodes'][node_id_json]['document']
                clean_node = self._filter_node(raw_node)
                
                # Save cleaned data
                self.file_handler.save_json(clean_node, 'clean_figma_output.json')
                
                return clean_node
        else:
            # Extract all components
            data = self.api_client.get_file_components(file_key)
            return data
        
        return {}
    
    def _filter_node(self, node: Dict[str, Any], parent_box: Optional[Dict[str, float]] = None) -> Dict[str, Any]:
        """Filter and clean node data, keeping only relevant fields.
        
        Args:
            node (dict): Raw node data from Figma
            parent_box (dict, optional): Parent bounding box for padding calculation
            
        Returns:
            dict: Filtered node data
        """
        new_node = {}
        current_box = node.get('absoluteBoundingBox')
        
        # Copy relevant fields
        for key, value in node.items():
            if key in KEEP_FIELDS:
                if key == 'children':
                    new_children = [self._filter_node(child, current_box) for child in value]
                    self._process_siblings(new_children)
                    new_node[key] = new_children
                else:
                    new_node[key] = value
        
        # Calculate padding if parent box is available
        if parent_box and current_box:
            new_node['padding'] = self._extract_padding(parent_box, current_box)
        
        return new_node
    
    def _extract_padding(self, parent_box: Dict[str, float], child_box: Dict[str, float]) -> Dict[str, float]:
        """Calculate padding between parent and child elements.
        
        Args:
            parent_box (dict): Parent element bounding box
            child_box (dict): Child element bounding box
            
        Returns:
            dict: Padding values (left, top, right, bottom)
        """
        px, py, pw, ph = parent_box["x"], parent_box["y"], parent_box["width"], parent_box["height"]
        cx, cy, cw, ch = child_box["x"], child_box["y"], child_box["width"], child_box["height"]
        
        return {
            "left": round(cx - px, 2),
            "top": round(cy - py, 2),
            "right": round((px + pw) - (cx + cw), 2),
            "bottom": round((py + ph) - (cy + ch), 2)
        }
    
    def _is_same_row(self, box1: Dict[str, float], box2: Dict[str, float], tolerance: float = 2) -> bool:
        """Check if two elements are in the same row.
        
        Args:
            box1 (dict): First element bounding box
            box2 (dict): Second element bounding box
            tolerance (float): Tolerance for row alignment
            
        Returns:
            bool: True if elements are in same row
        """
        return abs(box1["y"] - box2["y"]) < tolerance
    
    def _is_same_column(self, box1: Dict[str, float], box2: Dict[str, float], tolerance: float = 2) -> bool:
        """Check if two elements are in the same column.
        
        Args:
            box1 (dict): First element bounding box
            box2 (dict): Second element bounding box
            tolerance (float): Tolerance for column alignment
            
        Returns:
            bool: True if elements are in same column
        """
        return abs(box1["x"] - box2["x"]) < tolerance
    
    def _calc_distance(self, box1: Dict[str, float], box2: Dict[str, float], relation: str) -> Optional[float]:
        """Calculate distance between two elements based on their relationship.
        
        Args:
            box1 (dict): First element bounding box
            box2 (dict): Second element bounding box
            relation (str): Relationship type ('sameRow' or 'sameColumn')
            
        Returns:
            float: Distance between elements
        """
        if relation == "sameRow":
            return abs(box1["x"] - box2["x"])
        elif relation == "sameColumn":
            return abs(box1["y"] - box2["y"])
        return None
    
    def _process_siblings(self, children: list) -> None:
        """Process sibling relationships and add layout information.
        
        Args:
            children (list): List of child nodes
        """
        for i, node_i in enumerate(children):
            box_i = node_i.get("absoluteBoundingBox")
            if not box_i:
                continue
            
            siblings_info = []
            for j, node_j in enumerate(children):
                if i == j:
                    continue
                
                box_j = node_j.get("absoluteBoundingBox")
                if not box_j:
                    continue
                
                if self._is_same_row(box_i, box_j):
                    siblings_info.append({
                        "targetId": node_j.get("id"),
                        "relation": "sameRow",
                        "distance": round(self._calc_distance(box_i, box_j, "sameRow"), 2)
                    })
                elif self._is_same_column(box_i, box_j):
                    siblings_info.append({
                        "targetId": node_j.get("id"),
                        "relation": "sameColumn",
                        "distance": round(self._calc_distance(box_i, box_j, "sameColumn"), 2)
                    })
            
            if siblings_info:
                node_i["siblingsLayout"] = siblings_info
