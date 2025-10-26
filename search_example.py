"""
Search Engine Example - Direct CORE Service Usage
Demonstrates searching DuckDuckGo
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Fix Windows console encoding issue
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import asyncio
import logging
from core.task_executor import TaskExecutor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def main():
    """Execute DuckDuckGo search task"""
    print("Starting DuckDuckGo search task...")
    print("=" * 60)
    
    # Create task executor
    executor = TaskExecutor()
    
    # Define search task - focused on search and screenshot
    search_task = {
        "url": "https://duckduckgo.com",
        "steps": [
            {
                "action": "wait",
                "selector": "input[name='q']",
                "timeout": 15000,
                "description": "Wait for search box to load"
            },
            {
                "action": "type",
                "selector": "input[name='q']",
                "text": "shoes",
                "description": "Type 'shoes' in search box"
            },
            {
                "action": "click",
                "selector": "button[type='submit']",
                "description": "Click search button"
            },
            {
                "action": "wait",
                "selector": "body",
                "timeout": 10000,
                "description": "Wait for page to load"
            },
            {
                "action": "screenshot",
                "path": "search_results.png",
                "description": "Save screenshot of search results"
            }
        ]
    }
    
    # Execute task
    result = await executor.execute_task(search_task)
    
    # Display results
    print("\n" + "=" * 60)
    if result["success"]:
        print("Task executed successfully!")
        print(f"Result: {result['message']}")
        print("\nExecution steps details:")
        for step_name, step_result in result["results"].items():
            print(f"  {step_name}:")
            if isinstance(step_result, dict):
                for key, value in step_result.items():
                    if key != "text":  # Skip long text content
                        print(f"    - {key}: {value}")
            else:
                print(f"    {step_result}")
        print("\nScreenshot saved to: search_results.png")
        print("\nSuccessfully completed search task!")
    else:
        print("Task execution failed!")
        print(f"Error: {result['error']}")
    
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())
