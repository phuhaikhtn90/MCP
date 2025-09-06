"""Frame extractor for extracting frames from Figma files."""

from typing import Dict, Any, List
from ..core.api_client import FigmaAPIClient
from ..utils.file_handler import FileHandler


class FrameExtractor:
    """Extractor for Figma frames."""
    
    def __init__(self, api_client: FigmaAPIClient):
        """Initialize the frame extractor.
        
        Args:
            api_client (FigmaAPIClient): Figma API client instance
        """
        self.api_client = api_client
        self.file_handler = FileHandler()
    
    def extract(self, file_key: str = None) -> List[Dict[str, Any]]:
        """Extract frames from Figma file.
        
        Args:
            file_key (str, optional): Figma file key
            
        Returns:
            list: List of extracted frames
        """
        # Get file data from Figma API
        data = self.api_client.get_file(file_key)
        
        # Save raw data
        self.file_handler.save_json(data, 'figma_file.json')
        
        all_frames = []
        
        # Process nodes data
        nodes_data = data.get('nodes', {})
        for node_id, node_content in nodes_data.items():
            if 'document' in node_content:
                self._find_frames(node_content['document'], all_frames)
        
        # Also check document root if available
        if 'document' in data:
            self._find_frames(data['document'], all_frames)
        
        print(f"✅ Tìm thấy {len(all_frames)} FRAME(s)\n")
        
        # Print frame information
        for frame in all_frames:
            print(f"🖼️ Frame: {frame['name']}")
            print(f"  ID: {frame['id']}")
            print(f"  Position: ({frame['x']}, {frame['y']})")
            print(f"  Size: {frame['width']} x {frame['height']}")
            print(f"  Children: {frame['child_count']}")
            print("-" * 40)
        
        return all_frames
    
    def _find_frames(self, node: Dict[str, Any], frames: List[Dict[str, Any]]) -> None:
        """Recursively find frames in the node tree.
        
        Args:
            node (dict): Current node to search
            frames (list): List to append found frames to
        """
        # Check if current node is a FRAME
        if node.get('type') == 'FRAME':
            frame_info = {
                'id': node.get('id'),
                'name': node.get('name'),
                'x': node.get('absoluteBoundingBox', {}).get('x'),
                'y': node.get('absoluteBoundingBox', {}).get('y'),
                'width': node.get('absoluteBoundingBox', {}).get('width'),
                'height': node.get('absoluteBoundingBox', {}).get('height'),
                'child_count': len(node.get('children', []))
            }
            frames.append(frame_info)
        
        # Recursively search children
        if 'children' in node:
            for child in node['children']:
                self._find_frames(child, frames)
    
    def get_frame_by_id(self, frame_id: str, file_key: str = None) -> Dict[str, Any]:
        """Get a specific frame by its ID.
        
        Args:
            frame_id (str): Frame ID to search for
            file_key (str, optional): Figma file key
            
        Returns:
            dict: Frame data or None if not found
        """
        frames = self.extract(file_key)
        for frame in frames:
            if frame['id'] == frame_id:
                return frame
        return None
    
    def get_frames_by_name(self, name_pattern: str, file_key: str = None) -> List[Dict[str, Any]]:
        """Get frames that match a name pattern.
        
        Args:
            name_pattern (str): Pattern to match frame names
            file_key (str, optional): Figma file key
            
        Returns:
            list: List of matching frames
        """
        frames = self.extract(file_key)
        matching_frames = []
        
        for frame in frames:
            if name_pattern.lower() in frame.get('name', '').lower():
                matching_frames.append(frame)
        
        return matching_frames
