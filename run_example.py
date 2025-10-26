"""
Quick run example script
"""
import sys
import asyncio
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

async def main():
    """Main function"""
    print("=" * 50)
    print("Web Automation Bot - Quick Test")
    print("=" * 50)
    print()
    
    # Test imports
    print("Testing module imports...")
    try:
        from core.task_executor import TaskExecutor
        print("[OK] Core module imported successfully")
    except ImportError as e:
        print(f"[ERROR] Core module import failed: {e}")
        return
    
    try:
        from ai_brain.task_planner import AITaskPlanner
        print("[OK] AI module imported successfully")
    except ImportError as e:
        print(f"[ERROR] AI module import failed: {e}")
    
    print()
    print("Available examples:")
    print("  1. python examples/simple_task.py")
    print("  2. python examples/ai_task.py")
    print("  3. python api/main.py (start API service)")
    print()
    print("For more information, see README.md and SETUP.md")
    print()

if __name__ == "__main__":
    asyncio.run(main())
