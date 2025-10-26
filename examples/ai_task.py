"""
AI Task Example - Demonstrate AI brain functionality
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
import logging
from ai_brain.task_planner import AITaskPlanner

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def main():
    """Execute AI task example"""
    print("Starting AI-driven automation task...")
    
    planner = AITaskPlanner()
    
    # Example task
    goal = "Get page title"
    url = "https://example.com"
    
    result = await planner.execute_ai_task(goal, url)
    
    if result["success"]:
        print("AI task executed successfully!")
        print(f"Result: {result.get('message', 'Task completed')}")
        
        if result.get("plan"):
            print("Execution plan:")
            for i, step in enumerate(result["plan"]):
                print(f"  {i+1}. {step.get('description', step.get('action'))}")
        
        if result.get("results"):
            print("Execution results:")
            for step, step_result in result["results"].items():
                print(f"  {step}: {step_result}")
    else:
        print("AI task execution failed!")
        print(f"Error: {result['error']}")

if __name__ == "__main__":
    asyncio.run(main())
