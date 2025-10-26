"""
AI Feature Test on Real Websites
Testing AI automation on actual websites
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Fix Windows console encoding issue
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import asyncio
import logging
from ai_brain.task_planner import AITaskPlanner

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def test_quotes_website():
    """Test AI on http://quotes.toscrape.com"""
    print("\n" + "=" * 70)
    print("AI Test: Quotes to Scrape Website")
    print("=" * 70)
    
    planner = AITaskPlanner()
    
    # AI Task: Get the first quote text
    goal = "Get the first quote from the page"
    url = "http://quotes.toscrape.com"
    
    print(f"\nGoal: {goal}")
    print(f"URL: {url}")
    print("\nExecuting AI task...")
    
    result = await planner.execute_ai_task(goal, url)
    
    print("\n" + "-" * 70)
    if result["success"]:
        print("AI Task Completed Successfully!")
        print("\nAI Generated Plan:")
        if result.get("plan"):
            for i, step in enumerate(result["plan"]):
                print(f"  Step {i+1}: {step.get('description', step.get('action'))}")
        
        print("\nExecution Results:")
        if result.get("results"):
            for step_name, step_result in result["results"].items():
                if isinstance(step_result, dict) and step_result.get("success"):
                    action = step_result.get("action")
                    if action == "get_text" and "text" in step_result:
                        text = step_result["text"]
                        if len(text) > 80:
                            text = text[:80] + "..."
                        print(f"  {step_name}: Got text - {text}")
                    else:
                        print(f"  {step_name}: {action} - Success")
    else:
        print("AI Task Failed!")
        print(f"Error: {result['error']}")
    print("=" * 70)

async def test_wikipedia():
    """Test AI on Wikipedia"""
    print("\n" + "=" * 70)
    print("AI Test: Wikipedia Search")
    print("=" * 70)
    
    planner = AITaskPlanner()
    
    # AI Task: Search for Python
    goal = "Search for Python programming and get the page title"
    url = "https://en.wikipedia.org/wiki/Main_Page"
    
    print(f"\nGoal: {goal}")
    print(f"URL: {url}")
    print("\nExecuting AI task...")
    
    result = await planner.execute_ai_task(goal, url)
    
    print("\n" + "-" * 70)
    if result["success"]:
        print("AI Task Completed Successfully!")
        print("\nAI Generated Plan:")
        if result.get("plan"):
            for i, step in enumerate(result["plan"]):
                print(f"  Step {i+1}: {step.get('description', step.get('action'))}")
        
        print("\nExecution Results:")
        if result.get("results"):
            for step_name, step_result in result["results"].items():
                if isinstance(step_result, dict) and step_result.get("success"):
                    action = step_result.get("action")
                    if action == "type" and "text" in step_result:
                        print(f"  {step_name}: Typed - {step_result['text']}")
                    elif action == "get_text" and "text" in step_result:
                        print(f"  {step_name}: Got title - {step_result['text']}")
                    else:
                        print(f"  {step_name}: {action} - Success")
    else:
        print("AI Task Failed!")
        print(f"Error: {result['error']}")
    print("=" * 70)

async def test_github():
    """Test AI on GitHub"""
    print("\n" + "=" * 70)
    print("AI Test: GitHub")
    print("=" * 70)
    
    planner = AITaskPlanner()
    
    # AI Task: Get GitHub title
    goal = "Navigate to GitHub and get the page title"
    url = "https://github.com"
    
    print(f"\nGoal: {goal}")
    print(f"URL: {url}")
    print("\nExecuting AI task...")
    
    result = await planner.execute_ai_task(goal, url)
    
    print("\n" + "-" * 70)
    if result["success"]:
        print("AI Task Completed Successfully!")
        print("\nAI Generated Plan:")
        if result.get("plan"):
            for i, step in enumerate(result["plan"]):
                print(f"  Step {i+1}: {step.get('description', step.get('action'))}")
    else:
        print("AI Task Failed!")
        print(f"Error: {result['error']}")
    print("=" * 70)

async def main():
    """Run all AI tests"""
    print("\n" + "=" * 70)
    print("AI Feature Test on Real Websites")
    print("=" * 70)
    print("\nNote: These tests use the AI to generate automation plans")
    print("based on natural language goals.")
    
    # Test 1: Simple quotes website
    try:
        await test_quotes_website()
    except Exception as e:
        print(f"\nTest 1 failed with error: {e}")
    
    # Test 2: GitHub (simpler)
    try:
        await test_github()
    except Exception as e:
        print(f"\nTest 2 failed with error: {e}")
    
    # Note: Wikipedia test might be skipped if it takes too long
    # Uncomment if you want to test
    # try:
    #     await test_wikipedia()
    # except Exception as e:
    #     print(f"\nTest 3 failed with error: {e}")
    
    print("\n" + "=" * 70)
    print("All AI Tests Completed!")
    print("=" * 70)
    print("\nNote: The AI feature requires OpenAI API key to work fully.")
    print("Without it, the system uses fallback mock plans.")

if __name__ == "__main__":
    asyncio.run(main())
