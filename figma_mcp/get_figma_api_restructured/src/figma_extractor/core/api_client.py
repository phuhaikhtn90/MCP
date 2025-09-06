"""Figma API client for making requests to Figma API."""

import requests
import time
from typing import Dict, Any, Optional
import sys
from pathlib import Path

# Add config to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'config'))

from settings import (
    FIGMA_TOKEN, FIGMA_FILE_KEY, FIGMA_API_BASE_URL,
    REQUEST_TIMEOUT, MAX_RETRIES
)


class FigmaAPIClient:
    """Client for interacting with Figma API."""
    
    def __init__(self, token: Optional[str] = None, file_key: Optional[str] = None):
        """Initialize the Figma API client.
        
        Args:
            token (str, optional): Figma API token. Defaults to config value.
            file_key (str, optional): Figma file key. Defaults to config value.
        """
        self.token = token or FIGMA_TOKEN
        self.file_key = file_key or FIGMA_FILE_KEY
        self.base_url = FIGMA_API_BASE_URL
        
        if not self.token:
            raise ValueError("Figma API token is required")
        
        self.headers = {
            'X-Figma-Token': self.token
        }
    
    def _make_request(self, url: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a request to Figma API with retry logic.
        
        Args:
            url (str): API endpoint URL
            params (dict, optional): Query parameters
            
        Returns:
            dict: API response data
            
        Raises:
            requests.RequestException: If request fails after retries
        """
        for attempt in range(MAX_RETRIES):
            try:
                response = requests.get(
                    url, 
                    headers=self.headers, 
                    params=params,
                    timeout=REQUEST_TIMEOUT
                )
                response.raise_for_status()
                return response.json()
            
            except requests.RequestException as e:
                if attempt == MAX_RETRIES - 1:
                    raise e
                time.sleep(2 ** attempt)  # Exponential backoff
    
    def get_file(self, file_key: Optional[str] = None) -> Dict[str, Any]:
        """Get Figma file data.
        
        Args:
            file_key (str, optional): File key. Defaults to instance file_key.
            
        Returns:
            dict: File data
        """
        key = file_key or self.file_key
        if not key:
            raise ValueError("File key is required")
        
        url = f"{self.base_url}/files/{key}"
        return self._make_request(url)
    
    def get_file_nodes(self, node_ids: str, file_key: Optional[str] = None) -> Dict[str, Any]:
        """Get specific nodes from Figma file.
        
        Args:
            node_ids (str): Comma-separated node IDs
            file_key (str, optional): File key. Defaults to instance file_key.
            
        Returns:
            dict: Node data
        """
        key = file_key or self.file_key
        if not key:
            raise ValueError("File key is required")
        
        url = f"{self.base_url}/files/{key}/nodes"
        params = {'ids': node_ids}
        return self._make_request(url, params)
    
    def get_file_components(self, file_key: Optional[str] = None) -> Dict[str, Any]:
        """Get components from Figma file.
        
        Args:
            file_key (str, optional): File key. Defaults to instance file_key.
            
        Returns:
            dict: Components data
        """
        key = file_key or self.file_key
        if not key:
            raise ValueError("File key is required")
        
        url = f"{self.base_url}/files/{key}/components"
        return self._make_request(url)
