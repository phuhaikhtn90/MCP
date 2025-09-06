"""File handler utility for JSON file operations."""

import json
from pathlib import Path
from typing import Dict, Any, Union
import sys
from pathlib import Path

# Add config to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'config'))

from settings import OUTPUT_DIR, INPUT_DIR


class FileHandler:
    """Utility class for handling file operations."""
    
    def __init__(self, output_dir: Union[str, Path] = None, input_dir: Union[str, Path] = None):
        """Initialize the file handler.
        
        Args:
            output_dir (str|Path, optional): Output directory path
            input_dir (str|Path, optional): Input directory path
        """
        self.output_dir = Path(output_dir) if output_dir else OUTPUT_DIR
        self.input_dir = Path(input_dir) if input_dir else INPUT_DIR
        
        # Ensure directories exist
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.input_dir.mkdir(parents=True, exist_ok=True)
    
    def save_json(self, data: Dict[str, Any], filename: str, output_dir: Union[str, Path] = None) -> Path:
        """Save data to a JSON file.
        
        Args:
            data (dict): Data to save
            filename (str): Name of the file
            output_dir (str|Path, optional): Output directory. Defaults to instance output_dir.
            
        Returns:
            Path: Path to the saved file
        """
        directory = Path(output_dir) if output_dir else self.output_dir
        directory.mkdir(parents=True, exist_ok=True)
        
        file_path = directory / filename
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Saved data to: {file_path}")
        return file_path
    
    def load_json(self, filename: str, input_dir: Union[str, Path] = None) -> Dict[str, Any]:
        """Load data from a JSON file.
        
        Args:
            filename (str): Name of the file to load
            input_dir (str|Path, optional): Input directory. Defaults to instance input_dir.
            
        Returns:
            dict: Loaded data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file contains invalid JSON
        """
        directory = Path(input_dir) if input_dir else self.input_dir
        file_path = directory / filename
        
        if not file_path.exists():
            # Try in output directory as fallback
            file_path = self.output_dir / filename
            if not file_path.exists():
                raise FileNotFoundError(f"File not found: {filename}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ Loaded data from: {file_path}")
        return data
    
    def file_exists(self, filename: str, directory: Union[str, Path] = None) -> bool:
        """Check if a file exists.
        
        Args:
            filename (str): Name of the file
            directory (str|Path, optional): Directory to check. Defaults to output_dir.
            
        Returns:
            bool: True if file exists
        """
        directory = Path(directory) if directory else self.output_dir
        return (directory / filename).exists()
    
    def list_files(self, directory: Union[str, Path] = None, pattern: str = "*.json") -> list:
        """List files in a directory.
        
        Args:
            directory (str|Path, optional): Directory to list. Defaults to output_dir.
            pattern (str): File pattern to match
            
        Returns:
            list: List of file paths
        """
        directory = Path(directory) if directory else self.output_dir
        return list(directory.glob(pattern))
    
    def copy_file(self, source: Union[str, Path], destination: Union[str, Path]) -> Path:
        """Copy a file from source to destination.
        
        Args:
            source (str|Path): Source file path
            destination (str|Path): Destination file path
            
        Returns:
            Path: Destination file path
        """
        import shutil
        
        source_path = Path(source)
        dest_path = Path(destination)
        
        # Ensure destination directory exists
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        shutil.copy2(source_path, dest_path)
        print(f"✅ Copied {source_path} to {dest_path}")
        
        return dest_path
    
    def move_file(self, source: Union[str, Path], destination: Union[str, Path]) -> Path:
        """Move a file from source to destination.
        
        Args:
            source (str|Path): Source file path
            destination (str|Path): Destination file path
            
        Returns:
            Path: Destination file path
        """
        import shutil
        
        source_path = Path(source)
        dest_path = Path(destination)
        
        # Ensure destination directory exists
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        shutil.move(str(source_path), str(dest_path))
        print(f"✅ Moved {source_path} to {dest_path}")
        
        return dest_path
    
    def delete_file(self, filename: str, directory: Union[str, Path] = None) -> bool:
        """Delete a file.
        
        Args:
            filename (str): Name of the file to delete
            directory (str|Path, optional): Directory containing the file
            
        Returns:
            bool: True if file was deleted
        """
        directory = Path(directory) if directory else self.output_dir
        file_path = directory / filename
        
        if file_path.exists():
            file_path.unlink()
            print(f"✅ Deleted file: {file_path}")
            return True
        else:
            print(f"❌ File not found: {file_path}")
            return False
    
    def get_file_size(self, filename: str, directory: Union[str, Path] = None) -> int:
        """Get file size in bytes.
        
        Args:
            filename (str): Name of the file
            directory (str|Path, optional): Directory containing the file
            
        Returns:
            int: File size in bytes
        """
        directory = Path(directory) if directory else self.output_dir
        file_path = directory / filename
        
        if file_path.exists():
            return file_path.stat().st_size
        else:
            raise FileNotFoundError(f"File not found: {file_path}")
