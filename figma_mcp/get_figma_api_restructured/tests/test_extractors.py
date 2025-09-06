"""Tests for Figma extractors."""

import unittest
import sys
from pathlib import Path
from unittest.mock import Mock, patch

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from figma_extractor.core.api_client import FigmaAPIClient
from figma_extractor.extractors.token_extractor import TokenExtractor
from figma_extractor.extractors.frame_extractor import FrameExtractor
from figma_extractor.extractors.component_extractor import ComponentExtractor


class TestTokenExtractor(unittest.TestCase):
    """Test cases for TokenExtractor."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_client = Mock(spec=FigmaAPIClient)
        self.extractor = TokenExtractor(self.mock_client)
    
    def test_extract_calls_api_client(self):
        """Test that extract method calls API client."""
        mock_data = {'document': {'children': []}}
        self.mock_client.get_file.return_value = mock_data
        
        result = self.extractor.extract()
        
        self.mock_client.get_file.assert_called_once()
        self.assertEqual(result, mock_data)


class TestFrameExtractor(unittest.TestCase):
    """Test cases for FrameExtractor."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_client = Mock(spec=FigmaAPIClient)
        self.extractor = FrameExtractor(self.mock_client)
    
    def test_find_frames(self):
        """Test frame finding functionality."""
        mock_node = {
            'type': 'FRAME',
            'id': 'test-frame',
            'name': 'Test Frame',
            'absoluteBoundingBox': {
                'x': 0, 'y': 0, 'width': 100, 'height': 100
            },
            'children': []
        }
        
        frames = []
        self.extractor._find_frames(mock_node, frames)
        
        self.assertEqual(len(frames), 1)
        self.assertEqual(frames[0]['name'], 'Test Frame')


class TestComponentExtractor(unittest.TestCase):
    """Test cases for ComponentExtractor."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_client = Mock(spec=FigmaAPIClient)
        self.extractor = ComponentExtractor(self.mock_client)
    
    def test_extract_padding_calculation(self):
        """Test padding calculation."""
        parent_box = {'x': 0, 'y': 0, 'width': 100, 'height': 100}
        child_box = {'x': 10, 'y': 10, 'width': 80, 'height': 80}
        
        padding = self.extractor._extract_padding(parent_box, child_box)
        
        expected = {
            'left': 10.0,
            'top': 10.0,
            'right': 10.0,
            'bottom': 10.0
        }
        self.assertEqual(padding, expected)


if __name__ == '__main__':
    unittest.main()
