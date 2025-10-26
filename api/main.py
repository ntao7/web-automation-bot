from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
from api.models import TaskRequest, AITaskRequest, TaskResponse
from core.task_executor import TaskExecutor
from ai_brain.task_planner import AITaskPlanner

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Web Automation Bot API",
    description="API service for automated web tasks",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root path, returns API information"""
    return {
        "message": "Web Automation Bot API",
        "version": "1.0.0",
        "endpoints": {
            "execute_task": "/execute-task",
            "execute_ai_task": "/execute-ai-task",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    """Health check"""
    return {"status": "healthy", "service": "web-automation-bot"}

@app.post("/execute-task", response_model=TaskResponse)
async def execute_task(request: TaskRequest):
    """Execute predefined task"""
    try:
        executor = TaskExecutor()
        
        # Convert request format
        task_config = {
            "url": str(request.url),
            "steps": [step.dict() for step in request.steps]
        }
        
        result = await executor.execute_task(task_config)
        
        if result["success"]:
            return TaskResponse(
                success=True,
                message=result["message"],
                results=result["results"]
            )
        else:
            return TaskResponse(
                success=False,
                error=result["error"],
                results=result.get("results")
            )
            
    except Exception as e:
        logger.error(f"Task execution exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/execute-ai-task", response_model=TaskResponse)
async def execute_ai_task(request: AITaskRequest):
    """Execute AI-driven task"""
    try:
        planner = AITaskPlanner()
        
        result = await planner.execute_ai_task(request.goal, str(request.url))
        
        if result["success"]:
            return TaskResponse(
                success=True,
                message=result.get("message", "AI task executed successfully"),
                results=result.get("results"),
                plan=result.get("plan"),
                page_info=result.get("page_info")
            )
        else:
            return TaskResponse(
                success=False,
                error=result["error"],
                results=result.get("results"),
                plan=result.get("plan"),
                page_info=result.get("page_info")
            )
            
    except Exception as e:
        logger.error(f"AI task execution exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    from config import Config
    
    uvicorn.run(
        "api.main:app",
        host=Config.API_HOST,
        port=Config.API_PORT,
        reload=True
    )
