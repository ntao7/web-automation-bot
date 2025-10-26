import asyncio
import logging
from typing import Dict, Any, List, Optional
from ai_brain.mcp_client import MCPClient
from ai_brain.llm_handler import LLMHandler
from core.task_executor import TaskExecutor

logger = logging.getLogger(__name__)

class AITaskPlanner:
    """AI task planner, integrates MCP and LLM functionality"""
    
    def __init__(self):
        self.mcp_client = MCPClient()
        self.llm_handler = LLMHandler()
        self.task_executor = TaskExecutor()
    
    async def execute_ai_task(self, goal: str, url: str) -> Dict[str, Any]:
        """Execute AI-driven task"""
        try:
            # 1. Get page info (use mock data if MCP server unavailable)
            logger.info("Analyzing page...")
            page_info = await self.mcp_client.get_page_info(url)
            if not page_info:
                # If MCP server unavailable, use mock data
                logger.warning("MCP server unavailable, using mock data")
                page_info = {
                    "url": url,
                    "title": "Web Page",
                    "form_count": 0,
                    "link_count": 0
                }
            
            # 2. Get accessible elements
            accessible_elements = await self.mcp_client.get_accessible_elements(url)
            if not accessible_elements:
                # If no MCP server, create a simple fallback plan
                logger.warning("Cannot get page elements, creating basic task plan")
                
                # Smart fallback based on goal
                goal_lower = goal.lower()
                if "search" in goal_lower or "find" in goal_lower:
                    plan = [
                        {
                            "action": "wait",
                            "selector": "input[type='search'], input[name*='search'], input[id*='search']",
                            "timeout": 10000,
                            "description": "Wait for search box"
                        },
                        {
                            "action": "screenshot",
                            "path": "search_page.png",
                            "description": "Take screenshot of page"
                        }
                    ]
                elif "quote" in goal_lower or "text" in goal_lower or "get" in goal_lower:
                    plan = [
                        {
                            "action": "wait",
                            "selector": ".quote, blockquote, .text, article",
                            "timeout": 10000,
                            "description": "Wait for content to load"
                        },
                        {
                            "action": "get_text",
                            "selector": ".quote .text, blockquote, .text",
                            "description": "Get text content"
                        },
                        {
                            "action": "screenshot",
                            "path": "content_page.png",
                            "description": "Take screenshot"
                        }
                    ]
                else:
                    # Default plan
                    plan = [
                        {
                            "action": "wait",
                            "selector": "body",
                            "timeout": 5000,
                            "description": "Wait for page to load"
                        },
                        {
                            "action": "get_text",
                            "selector": "h1, .title, title",
                            "description": "Get page title"
                        },
                        {
                            "action": "screenshot",
                            "path": "page_screenshot.png",
                            "description": "Take screenshot"
                        }
                    ]
            else:
                # 3. Generate task plan using AI
                logger.info("Generating task plan...")
                plan = await self.llm_handler.generate_task_plan(goal, page_info, accessible_elements)
                if not plan:
                    return {"success": False, "error": "Cannot generate task plan"}
            
            logger.info(f"Generated {len(plan)} steps")
            
            # 4. Execute task
            task_config = {
                "url": url,
                "steps": plan
            }
            
            result = await self.task_executor.execute_task(task_config)
            result["plan"] = plan
            result["page_info"] = page_info
            
            return result
            
        except Exception as e:
            logger.error(f"AI task execution failed: {e}")
            return {"success": False, "error": str(e)}
        finally:
            await self.mcp_client.close()
