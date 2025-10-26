import httpx
import json
import logging
from typing import Dict, Any, List, Optional
from config import Config

logger = logging.getLogger(__name__)

class MCPClient:
    """MCP client for communicating with Playwright MCP server"""
    
    def __init__(self):
        self.base_url = Config.MCP_SERVER_URL
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def get_page_info(self, url: str) -> Optional[Dict[str, Any]]:
        """Get page information"""
        try:
            response = await self.client.post(
                f"{self.base_url}/page-info",
                json={"url": url}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Failed to get page info: {e}")
            return None
    
    async def get_accessible_elements(self, url: str) -> Optional[List[Dict[str, Any]]]:
        """Get accessible elements list"""
        try:
            response = await self.client.post(
                f"{self.base_url}/accessible-elements",
                json={"url": url}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Failed to get accessible elements: {e}")
            return None
    
    async def analyze_page_structure(self, url: str) -> Optional[Dict[str, Any]]:
        """Analyze page structure"""
        try:
            response = await self.client.post(
                f"{self.base_url}/analyze-structure",
                json={"url": url}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Failed to analyze page structure: {e}")
            return None
    
    async def close(self):
        """Close client"""
        await self.client.aclose()
