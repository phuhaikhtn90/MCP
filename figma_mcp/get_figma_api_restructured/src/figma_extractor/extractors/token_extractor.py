"""Token extractor for extracting design tokens from Figma files."""

from typing import Dict, Any
from ..core.api_client import FigmaAPIClient
from ..utils.file_handler import FileHandler


class TokenExtractor:
    """Extractor for Figma design tokens."""
    
    def __init__(self, api_client: FigmaAPIClient):
        """Initialize the token extractor.
        
        Args:
            api_client (FigmaAPIClient): Figma API client instance
        """
        self.api_client = api_client
        self.file_handler = FileHandler()
    
    def extract(self, file_key: str = None) -> Dict[str, Any]:
        """Extract design tokens from Figma file.
        
        Args:
            file_key (str, optional): Figma file key
            
        Returns:
            dict: Extracted design tokens data
        """
        # Get file data from Figma API
        data = self.api_client.get_file(file_key)
        
        # Save raw data
        self.file_handler.save_json(data, 'figma_design.json')
        
        # TODO: Parse node tree to extract specific token info
        # You can start from data['document']['children']...
        
        return data
    
    def _parse_tokens(self, node: Dict[str, Any]) -> Dict[str, Any]:
        """Parse design tokens from a node.
        
        Args:
            node (dict): Figma node data
            
        Returns:
            dict: Parsed tokens
        """
        tokens = {}
        
        # Extract color tokens
        if 'fills' in node:
            tokens['colors'] = self._extract_color_tokens(node['fills'])
        
        # Extract typography tokens
        if 'style' in node:
            tokens['typography'] = self._extract_typography_tokens(node['style'])
        
        # Extract spacing tokens
        if 'absoluteBoundingBox' in node:
            tokens['spacing'] = self._extract_spacing_tokens(node)
        
        return tokens
    
    def _extract_color_tokens(self, fills: list) -> Dict[str, str]:
        """Extract color tokens from fills.
        
        Args:
            fills (list): Fill data from Figma
            
        Returns:
            dict: Color tokens
        """
        colors = {}
        for fill in fills:
            if fill.get('type') == 'SOLID' and 'color' in fill:
                color = fill['color']
                # Convert RGB to hex
                r = int(color.get('r', 0) * 255)
                g = int(color.get('g', 0) * 255)
                b = int(color.get('b', 0) * 255)
                hex_color = f"#{r:02x}{g:02x}{b:02x}"
                colors[f"color_{len(colors)}"] = hex_color
        return colors
    
    def _extract_typography_tokens(self, style: Dict[str, Any]) -> Dict[str, Any]:
        """Extract typography tokens from style.
        
        Args:
            style (dict): Style data from Figma
            
        Returns:
            dict: Typography tokens
        """
        typography = {}
        
        if 'fontFamily' in style:
            typography['fontFamily'] = style['fontFamily']
        if 'fontSize' in style:
            typography['fontSize'] = style['fontSize']
        if 'fontWeight' in style:
            typography['fontWeight'] = style['fontWeight']
        if 'lineHeightPx' in style:
            typography['lineHeight'] = style['lineHeightPx']
        
        return typography
    
    def _extract_spacing_tokens(self, node: Dict[str, Any]) -> Dict[str, float]:
        """Extract spacing tokens from node.
        
        Args:
            node (dict): Figma node data
            
        Returns:
            dict: Spacing tokens
        """
        spacing = {}
        bounds = node.get('absoluteBoundingBox', {})
        
        if 'width' in bounds:
            spacing['width'] = bounds['width']
        if 'height' in bounds:
            spacing['height'] = bounds['height']
        
        return spacing
