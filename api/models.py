from pydantic import BaseModel, HttpUrl
from typing import List, Dict, Any, Optional

class TaskStep(BaseModel):
    action: str
    selector: str
    text: Optional[str] = None
    timeout: Optional[int] = None
    description: Optional[str] = None

class TaskRequest(BaseModel):
    url: HttpUrl
    steps: List[TaskStep]

class AITaskRequest(BaseModel):
    goal: str
    url: HttpUrl

class TaskResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    error: Optional[str] = None
    results: Optional[Dict[str, Any]] = None
    plan: Optional[List[Dict[str, Any]]] = None
    page_info: Optional[Dict[str, Any]] = None
