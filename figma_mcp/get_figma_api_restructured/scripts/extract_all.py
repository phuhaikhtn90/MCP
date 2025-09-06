#!/usr/bin/env python3
"""Script to extract all data from Figma file."""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from figma_extractor import FigmaExtractor


def main():
    """Main function to extract all Figma data."""
    print("🚀 Starting Figma data extraction...")
    
    try:
        # Initialize extractor
        extractor = FigmaExtractor()
        
        # Extract tokens
        print("\n📋 Extracting design tokens...")
        tokens = extractor.extract_tokens()
        
        # Extract frames
        print("\n🖼️ Extracting frames...")
        frames = extractor.extract_frames()
        
        # Extract components (example with specific node)
        print("\n🧩 Extracting components...")
        components = extractor.extract_components("2-96")
        
        # Calculate distances
        print("\n📏 Calculating distances...")
        if tokens:
            distances = extractor.calculate_distances(tokens)
        
        print("\n✅ Extraction completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during extraction: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
