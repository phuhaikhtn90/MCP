"""Configuration settings for Figma API Extractor."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Figma API settings
FIGMA_TOKEN = os.getenv('FIGMA_TOKEN')
FIGMA_FILE_KEY = os.getenv('FIGMA_FILE_KEY')
FIGMA_API_BASE_URL = 'https://api.figma.com/v1'

# Directory settings
DATA_DIR = BASE_DIR / 'data'
INPUT_DIR = DATA_DIR / 'input'
OUTPUT_DIR = DATA_DIR / 'output'

# Ensure directories exist
INPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# API settings
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3

# Fields to keep when cleaning Figma data
KEEP_FIELDS = {
    "id", "name", "type", "children", "fills", "strokes", "strokeWeight", 
    "strokeAlign", "absoluteBoundingBox", "constraints", "characters", 
    "lineIndentations", "style", "componentId", "overrides", "clipsContent", 
    "effects", "interactions", "backgroundColor"
}

# Distance calculation tolerance
DISTANCE_TOLERANCE = 2
