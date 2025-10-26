"""AI brain tests"""
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
from ai_brain.task_planner import AITaskPlanner

@pytest.mark.asyncio
async def test_ai_planner():
    """Test AI task planner"""
    planner = AITaskPlanner()
    
    result = await planner.execute_ai_task(
        goal="Get page title",
        url="https://example.com"
    )
    
    # Basic verification
    assert "success" in result
    print(f"AI task result: {result}")

if __name__ == "__main__":
    asyncio.run(test_ai_planner())
