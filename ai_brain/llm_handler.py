import openai
import json
import logging
from typing import Dict, Any, List, Optional
from config import Config

logger = logging.getLogger(__name__)

class LLMHandler:
    """LLM handler, responsible for interacting with AI models"""
    
    def __init__(self):
        self.client = openai.AsyncOpenAI(api_key=Config.OPENAI_API_KEY) if Config.OPENAI_API_KEY else None
    
    async def generate_task_plan(
        self, 
        goal: str, 
        page_info: Dict[str, Any],
        accessible_elements: List[Dict[str, Any]]
    ) -> Optional[List[Dict[str, Any]]]:
        """Generate task plan based on goal and page information"""
        
        if not self.client:
            logger.error("OpenAI API key not configured")
            return None
        
        prompt = self._build_prompt(goal, page_info, accessible_elements)
        
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional web automation expert. Generate detailed automation steps based on user goals and page information."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.1
            )
            
            content = response.choices[0].message.content
            return self._parse_plan(content)
            
        except Exception as e:
            logger.error(f"Failed to generate task plan: {e}")
            return None
    
    def _build_prompt(self, goal: str, page_info: Dict[str, Any], accessible_elements: List[Dict[str, Any]]) -> str:
        """Build prompt"""
        elements_text = "\n".join([
            f"- {elem.get('role', 'unknown')}: {elem.get('name', 'unnamed')} (selector: {elem.get('selector', 'N/A')})"
            for elem in accessible_elements[:20]  # Limit number of elements
        ])
        
        return f"""
User Goal: {goal}

Page Information:
- URL: {page_info.get('url', 'N/A')}
- Title: {page_info.get('title', 'N/A')}
- Form Count: {page_info.get('form_count', 0)}
- Link Count: {page_info.get('link_count', 0)}

Accessible Elements:
{elements_text}

Please generate a detailed automation step plan using the following JSON format:
[
    {{
        "action": "wait|click|type|get_text|screenshot",
        "selector": "CSS selector",
        "text": "Text to type (only for type action)",
        "timeout": "Timeout in milliseconds (only for wait action)",
        "description": "Step description"
    }}
]

Ensure the steps are logical and include necessary waits and error handling.
"""
    
    def _parse_plan(self, content: str) -> Optional[List[Dict[str, Any]]]:
        """Parse AI-generated plan"""
        try:
            # Try to extract JSON part
            start_idx = content.find('[')
            end_idx = content.rfind(']') + 1
            
            if start_idx != -1 and end_idx != -1:
                json_str = content[start_idx:end_idx]
                return json.loads(json_str)
            else:
                logger.error("Cannot find JSON formatted plan")
                return None
                
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse plan JSON: {e}")
            return None
