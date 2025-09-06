"""Figma API Extractor package."""

from .core.api_client import FigmaAPIClient
from .extractors.token_extractor import TokenExtractor
from .extractors.frame_extractor import FrameExtractor
from .extractors.component_extractor import ComponentExtractor
from .processors.distance_calculator import DistanceCalculator
from .processors.data_cleaner import DataCleaner

__version__ = "1.0.0"
__author__ = "Your Name"

class FigmaExtractor:
    """Main class for Figma data extraction."""
    
    def __init__(self, token=None, file_key=None):
        """Initialize the Figma extractor.
        
        Args:
            token (str): Figma API token
            file_key (str): Figma file key
        """
        self.api_client = FigmaAPIClient(token, file_key)
        self.token_extractor = TokenExtractor(self.api_client)
        self.frame_extractor = FrameExtractor(self.api_client)
        self.component_extractor = ComponentExtractor(self.api_client)
        self.distance_calculator = DistanceCalculator()
        self.data_cleaner = DataCleaner()
    
    def extract_tokens(self):
        """Extract design tokens from Figma file."""
        return self.token_extractor.extract()
    
    def extract_frames(self):
        """Extract frames from Figma file."""
        return self.frame_extractor.extract()
    
    def extract_components(self, node_id=None):
        """Extract components from Figma file."""
        return self.component_extractor.extract(node_id)
    
    def calculate_distances(self, data):
        """Calculate distances between elements."""
        return self.distance_calculator.calculate(data)
    
    def clean_data(self, data):
        """Clean and filter Figma data."""
        return self.data_cleaner.clean(data)

__all__ = [
    'FigmaExtractor',
    'FigmaAPIClient',
    'TokenExtractor',
    'FrameExtractor', 
    'ComponentExtractor',
    'DistanceCalculator',
    'DataCleaner'
]
