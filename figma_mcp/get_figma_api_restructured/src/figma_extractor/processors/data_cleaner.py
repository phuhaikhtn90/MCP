"""Data cleaner for filtering and cleaning Figma API responses."""

from typing import Dict, Any, Optional
import sys
from pathlib import Path

# Add config to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'config'))

from settings import KEEP_FIELDS


class DataCleaner:
    """Cleaner for Figma data filtering and processing."""
    
    def __init__(self):
        """Initialize the data cleaner."""
        pass
    
    def clean(self, data: Dict[str, Any], keep_fields: Optional[set] = None) -> Dict[str, Any]:
        """Clean and filter Figma data.
        
        Args:
            data (dict): Raw Figma data
            keep_fields (set, optional): Fields to keep. Defaults to KEEP_FIELDS.
            
        Returns:
            dict: Cleaned data
        """
        if keep_fields is None:
            keep_fields = KEEP_FIELDS
        
        if isinstance(data, dict):
            cleaned_data = {}
            for key, value in data.items():
                if key in keep_fields:
                    if isinstance(value, (dict, list)):
                        cleaned_data[key] = self.clean(value, keep_fields)
                    else:
                        cleaned_data[key] = value
            return cleaned_data
        elif isinstance(data, list):
            return [self.clean(item, keep_fields) for item in data]
        else:
            return data
    
    def filter_node(self, node: Dict[str, Any], parent_box: Optional[Dict[str, float]] = None, 
                   keep_fields: Optional[set] = None) -> Dict[str, Any]:
        """Filter and clean a single node, keeping only relevant fields.
        
        Args:
            node (dict): Raw node data from Figma
            parent_box (dict, optional): Parent bounding box for padding calculation
            keep_fields (set, optional): Fields to keep. Defaults to KEEP_FIELDS.
            
        Returns:
            dict: Filtered node data
        """
        if keep_fields is None:
            keep_fields = KEEP_FIELDS
        
        new_node = {}
        current_box = node.get('absoluteBoundingBox')
        
        # Copy relevant fields
        for key, value in node.items():
            if key in keep_fields:
                if key == 'children':
                    new_children = [self.filter_node(child, current_box, keep_fields) for child in value]
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
    
    def remove_empty_fields(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Remove empty fields from data.
        
        Args:
            data (dict): Data to clean
            
        Returns:
            dict: Data with empty fields removed
        """
        if isinstance(data, dict):
            cleaned = {}
            for key, value in data.items():
                if value is not None and value != "" and value != []:
                    if isinstance(value, (dict, list)):
                        cleaned_value = self.remove_empty_fields(value)
                        if cleaned_value:  # Only add if not empty
                            cleaned[key] = cleaned_value
                    else:
                        cleaned[key] = value
            return cleaned
        elif isinstance(data, list):
            return [self.remove_empty_fields(item) for item in data if item is not None]
        else:
            return data
    
    def normalize_colors(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize color values in the data.
        
        Args:
            data (dict): Data containing color information
            
        Returns:
            dict: Data with normalized colors
        """
        if isinstance(data, dict):
            normalized = {}
            for key, value in data.items():
                if key == 'fills' and isinstance(value, list):
                    normalized[key] = self._normalize_fills(value)
                elif isinstance(value, (dict, list)):
                    normalized[key] = self.normalize_colors(value)
                else:
                    normalized[key] = value
            return normalized
        elif isinstance(data, list):
            return [self.normalize_colors(item) for item in data]
        else:
            return data
    
    def _normalize_fills(self, fills: list) -> list:
        """Normalize fill color values.
        
        Args:
            fills (list): List of fill objects
            
        Returns:
            list: Normalized fills
        """
        normalized_fills = []
        for fill in fills:
            if isinstance(fill, dict) and fill.get('type') == 'SOLID' and 'color' in fill:
                normalized_fill = fill.copy()
                color = fill['color']
                
                # Convert RGB values to hex
                if isinstance(color, dict):
                    r = int(color.get('r', 0) * 255)
                    g = int(color.get('g', 0) * 255)
                    b = int(color.get('b', 0) * 255)
                    a = color.get('a', 1)
                    
                    normalized_fill['hexColor'] = f"#{r:02x}{g:02x}{b:02x}"
                    if a < 1:
                        normalized_fill['opacity'] = a
                
                normalized_fills.append(normalized_fill)
            else:
                normalized_fills.append(fill)
        
        return normalized_fills
