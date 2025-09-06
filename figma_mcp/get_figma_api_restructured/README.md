# Figma API Extractor

A Python package for extracting and processing Figma design data through the Figma API.

## Features

- Extract Figma design tokens and components
- Process frames and calculate layout distances
- Clean and structure Figma API responses
- Export design data in various formats

## Project Structure

```
figma_api_extractor/
├── src/
│   └── figma_extractor/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── api_client.py      # Figma API client
│       │   └── config.py          # Configuration management
│       ├── extractors/
│       │   ├── __init__.py
│       │   ├── token_extractor.py # Extract design tokens
│       │   ├── frame_extractor.py # Extract frames
│       │   └── component_extractor.py # Extract components
│       ├── processors/
│       │   ├── __init__.py
│       │   ├── distance_calculator.py # Calculate layout distances
│       │   └── data_cleaner.py    # Clean and filter data
│       └── utils/
│           ├── __init__.py
│           └── file_handler.py    # File I/O utilities
├── tests/
│   ├── __init__.py
│   ├── test_extractors.py
│   ├── test_processors.py
│   └── fixtures/
│       └── sample_figma_data.json
├── data/
│   ├── input/
│   └── output/
├── config/
│   ├── settings.py
│   └── .env.example
├── scripts/
│   ├── extract_all.py
│   └── process_data.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

1. Copy `.env.example` to `.env`
2. Add your Figma API token and file keys

## Usage

```python
from figma_extractor import FigmaExtractor

extractor = FigmaExtractor(token="your_token", file_key="your_file_key")
frames = extractor.extract_frames()
tokens = extractor.extract_tokens()
