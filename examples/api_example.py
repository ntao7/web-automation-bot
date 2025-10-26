"""
API usage example
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import httpx
import asyncio
import json

async def test_api():
    """Test API functionality"""
    base_url = "http://localhost:8000"
    
    async with httpx.AsyncClient() as client:
        # Test health check
        print("Testing health check...")
        try:
            response = await client.get(f"{base_url}/health")
            print(f"Health status: {response.json()}")
        except Exception as e:
            print(f"Unable to connect to API server: {e}")
            print("Please ensure API service is running: python api/main.py")
            return
        
        # Test simple task
        print("\nTesting simple task...")
        task_request = {
            "url": "https://example.com",
            "steps": [
                {
                    "action": "wait",
                    "selector": "body",
                    "timeout": 5000,
                    "description": "Wait for page to load"
                },
                {
                    "action": "get_text",
                    "selector": "h1",
                    "description": "Get page title"
                }
            ]
        }
        
        response = await client.post(
            f"{base_url}/execute-task",
            json=task_request
        )
        print(f"Task result: {response.json()}")
        
        # Test AI task
        print("\nTesting AI task...")
        ai_request = {
            "goal": "Get page title",
            "url": "https://example.com"
        }
        
        response = await client.post(
            f"{base_url}/execute-ai-task",
            json=ai_request
        )
        print(f"AI task result: {response.json()}")

if __name__ == "__main__":
    asyncio.run(test_api())
