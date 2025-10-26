"""Core functionality tests"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Fix Windows console encoding issue
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import pytest
import asyncio
from core.task_executor import TaskExecutor

@pytest.mark.asyncio
async def test_task_executor():
    """Test task executor"""
    executor = TaskExecutor()
    
    # Simple test task
    test_task = {
        "url": "https://example.com",
        "steps": [
            {
                "action": "wait",
                "selector": "body",
                "timeout": 10000
            }
        ]
    }
    
    result = await executor.execute_task(test_task)
    
    # Basic verification
    assert "success" in result
    print(f"Task execution result: {result}")

if __name__ == "__main__":
    asyncio.run(test_task_executor())
