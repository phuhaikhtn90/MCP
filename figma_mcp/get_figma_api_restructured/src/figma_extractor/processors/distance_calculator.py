"""Distance calculator for calculating layout distances between Figma elements."""

from typing import Dict, Any, List, Tuple, Optional
from ..utils.file_handler import FileHandler


class DistanceCalculator:
    """Calculator for distances between Figma elements."""
    
    def __init__(self):
        """Initialize the distance calculator."""
        self.file_handler = FileHandler()
    
    def calculate(self, data: Dict[str, Any], target_node_id: str = '1:5055') -> Dict[str, Any]:
        """Calculate distances between sibling elements in Figma data.
        
        Args:
            data (dict): Figma file data
            target_node_id (str): Target node ID to analyze
            
        Returns:
            dict: Distance calculation results
        """
        # Collect all parent nodes that have children
        parent_nodes = []
        
        # Start from the specified node
        if 'nodes' in data and target_node_id in data['nodes']:
            document_node = data['nodes'][target_node_id]['document']
            all_nodes_in_document = self._get_nodes_with_bounds(document_node)
            
            # Filter for nodes that are parents (have children)
            for node in all_nodes_in_document:
                if 'children' in node and node['children']:
                    parent_nodes.append(node)
        
        if not parent_nodes:
            print("Không tìm thấy các node có chứa children để tính khoảng cách.")
            return {}
        
        print("✅ Tính toán khoảng cách giữa các đối tượng anh em ruột (siblings):\n")
        
        results = {}
        
        for parent in parent_nodes:
            if not parent.get('children'):
                continue
            
            parent_id = parent['id']
            parent_name = parent['name']
            
            print(f"Parent Node: {parent_name} (ID: {parent_id})")
            
            children = parent['children']
            parent_results = []
            
            # Calculate distances between all pairs of children
            for i in range(len(children)):
                for j in range(i + 1, len(children)):
                    node1 = children[i]
                    node2 = children[j]
                    
                    # Ensure both nodes have absoluteBoundingBox
                    if 'absoluteBoundingBox' not in node1 or 'absoluteBoundingBox' not in node2:
                        continue
                    
                    h_dist, v_dist = self._calculate_distance(node1, node2)
                    if h_dist is not None and v_dist is not None:
                        distance_info = {
                            'node1': {
                                'id': node1['id'],
                                'name': node1.get('name', 'Unknown')
                            },
                            'node2': {
                                'id': node2['id'],
                                'name': node2.get('name', 'Unknown')
                            },
                            'horizontal_distance': round(h_dist, 2),
                            'vertical_distance': round(v_dist, 2)
                        }
                        parent_results.append(distance_info)
                        
                        print(f"  Khoảng cách giữa '{node1.get('name', 'Unknown')}' (ID: {node1['id']}) và '{node2.get('name', 'Unknown')}' (ID: {node2['id']}):")
                        print(f"    Ngang: {h_dist:.2f}")
                        print(f"    Dọc: {v_dist:.2f}")
            
            results[parent_id] = {
                'parent_name': parent_name,
                'distances': parent_results
            }
            
            print("-" * 60)
        
        return results
    
    def _get_nodes_with_bounds(self, node: Dict[str, Any], nodes_with_bounds: Optional[List] = None) -> List[Dict[str, Any]]:
        """Recursively find all nodes with 'absoluteBoundingBox'.
        
        Args:
            node (dict): Current node to search
            nodes_with_bounds (list, optional): List to append nodes to
            
        Returns:
            list: List of nodes with bounding boxes
        """
        if nodes_with_bounds is None:
            nodes_with_bounds = []
        
        if 'absoluteBoundingBox' in node:
            nodes_with_bounds.append(node)
        
        if 'children' in node:
            for child in node['children']:
                self._get_nodes_with_bounds(child, nodes_with_bounds)
        
        return nodes_with_bounds
    
    def _calculate_distance(self, node1: Dict[str, Any], node2: Dict[str, Any]) -> Tuple[Optional[float], Optional[float]]:
        """Calculate horizontal and vertical distances between two nodes.
        
        Args:
            node1 (dict): First node
            node2 (dict): Second node
            
        Returns:
            tuple: (horizontal_distance, vertical_distance)
        """
        bounds1 = node1.get('absoluteBoundingBox')
        bounds2 = node2.get('absoluteBoundingBox')
        
        if not bounds1 or not bounds2:
            return None, None
        
        x1, y1 = bounds1['x'], bounds1['y']
        w1, h1 = bounds1['width'], bounds1['height']
        x2, y2 = bounds2['x'], bounds2['y']
        w2, h2 = bounds2['width'], bounds2['height']
        
        # Calculate horizontal distance
        horz_dist = 0
        if x1 + w1 < x2:  # node1 is to the left of node2
            horz_dist = x2 - (x1 + w1)
        elif x2 + w2 < x1:  # node2 is to the left of node1
            horz_dist = x1 - (x2 + w2)
        else:  # They overlap horizontally
            horz_dist = max(x1, x2) - min(x1 + w1, x2 + w2)
            if horz_dist < 0:
                horz_dist = 0  # Consider overlap as 0 distance
        
        # Calculate vertical distance
        vert_dist = 0
        if y1 + h1 < y2:  # node1 is above node2
            vert_dist = y2 - (y1 + h1)
        elif y2 + h2 < y1:  # node2 is above node1
            vert_dist = y1 - (y2 + h2)
        else:  # They overlap vertically
            vert_dist = max(y1, y2) - min(y1 + h1, y2 + h2)
            if vert_dist < 0:
                vert_dist = 0  # Consider overlap as 0 distance
        
        return horz_dist, vert_dist
    
    def calculate_from_file(self, file_path: str, target_node_id: str = '1:5055') -> Dict[str, Any]:
        """Calculate distances from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file
            target_node_id (str): Target node ID to analyze
            
        Returns:
            dict: Distance calculation results
        """
        data = self.file_handler.load_json(file_path)
        return self.calculate(data, target_node_id)
