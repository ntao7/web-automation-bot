"""
Simple Task Example - Demonstrate core functionality
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
from core.task_executor import TaskExecutor, EXAMPLE_TASK

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def main():
    """Execute simple task example"""
    print("Starting simple automation task...")
    
    executor = TaskExecutor()
    result = await executor.execute_task(EXAMPLE_TASK)
    
    if result["success"]:
        print("Task executed successfully!")
        print(f"Result: {result['message']}")
        for step, step_result in result["results"].items():
            print(f"  {step}: {step_result}")
    else:
        print("Task execution failed!")
        print(f"Error: {result['error']}")

if __name__ == "__main__":
    asyncio.run(main())
