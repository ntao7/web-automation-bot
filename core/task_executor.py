import asyncio
import logging
from typing import Dict, Any, List, Optional
from core.browser_driver import BrowserDriver

logger = logging.getLogger(__name__)

class TaskExecutor:
    """Task executor responsible for executing automation tasks"""
    
    def __init__(self):
        self.driver = BrowserDriver()
        self.results = {}
    
    async def execute_task(self, task_config: Dict[str, Any]) -> Dict[str, Any]:
        """Execute task"""
        try:
            # Start browser
            if not await self.driver.start():
                return {"success": False, "error": "Failed to start browser"}
            
            # Navigate to target page
            url = task_config.get("url")
            if not await self.driver.navigate_to(url):
                return {"success": False, "error": f"Cannot access URL: {url}"}
            
            # Execute task steps
            steps = task_config.get("steps", [])
            for i, step in enumerate(steps):
                step_result = await self._execute_step(step)
                self.results[f"step_{i}"] = step_result
                
                if not step_result.get("success", False):
                    return {
                        "success": False, 
                        "error": f"Step {i} execution failed: {step_result.get('error')}",
                        "results": self.results
                    }
            
            return {
                "success": True,
                "message": "Task execution successful",
                "results": self.results
            }
            
        except Exception as e:
            logger.error(f"Task execution error: {e}")
            return {"success": False, "error": str(e)}
        finally:
            await self.driver.close()
    
    async def _execute_step(self, step: Dict[str, Any]) -> Dict[str, Any]:
        """Execute single step"""
        action = step.get("action")
        
        try:
            if action == "click":
                selector = step.get("selector")
                if await self.driver.click_element(selector):
                    return {"success": True, "action": "click", "selector": selector}
                else:
                    return {"success": False, "error": f"Click failed: {selector}"}
            
            elif action == "type":
                selector = step.get("selector")
                text = step.get("text")
                if await self.driver.type_text(selector, text):
                    return {"success": True, "action": "type", "selector": selector, "text": text}
                else:
                    return {"success": False, "error": f"Type failed: {selector}"}
            
            elif action == "wait":
                selector = step.get("selector")
                timeout = step.get("timeout", 5000)
                if await self.driver.wait_for_element(selector, timeout):
                    return {"success": True, "action": "wait", "selector": selector}
                else:
                    return {"success": False, "error": f"Wait timeout: {selector}"}
            
            elif action == "get_text":
                selector = step.get("selector")
                text = await self.driver.get_text(selector)
                if text is not None:
                    return {"success": True, "action": "get_text", "selector": selector, "text": text}
                else:
                    return {"success": False, "error": f"Get text failed: {selector}"}
            
            elif action == "screenshot":
                path = step.get("path", "screenshot.png")
                if await self.driver.take_screenshot(path):
                    return {"success": True, "action": "screenshot", "path": path}
                else:
                    return {"success": False, "error": "Screenshot failed"}
            
            else:
                return {"success": False, "error": f"Unknown action: {action}"}
                
        except Exception as e:
            return {"success": False, "error": str(e)}

# Example task configuration
EXAMPLE_TASK = {
    "url": "https://example.com",
    "steps": [
        {
            "action": "wait",
            "selector": "body",
            "timeout": 10000,
            "description": "Wait for page to load"
        },
        {
            "action": "get_text",
            "selector": "h1",
            "description": "Get page title"
        }
    ]
}
