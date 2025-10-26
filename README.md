# Web Automation Bot

An intelligent Python-based web automation bot supporting both traditional programming and AI-driven task execution.

## Features

### Core Functionality (Required Core)
- Playwright-based browser automation
- Complete error handling and reliability guarantees
- Clear console output and logging
- Support for multiple browser operations (click, type, wait, screenshot, etc.)

### AI Brain (Optional Challenge 1)
- Model Context Protocol (MCP) integration
- OpenAI GPT-4-driven dynamic task planning
- Intelligent page analysis and element identification
- Natural language goal to automation steps conversion

### API Service (Optional Challenge 2)
- FastAPI-based RESTful API
- Support for remote execution of traditional and AI tasks
- Complete request/response model validation
- CORS support and health checks

## Quick Start

### 1. Environment Setup

```bash
# Clone the project
cd web-automation-bot

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser
playwright install chromium
```

### 2. Environment Configuration

Create a `.env` file for AI features (optional):

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# MCP Server Configuration
MCP_SERVER_URL=http://localhost:3000

# Browser Configuration
BROWSER_HEADLESS=true
BROWSER_TIMEOUT=30000

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Logging Configuration
LOG_LEVEL=INFO
```

### 3. Run Examples

#### Core Functionality Example
```bash
python examples/simple_task.py
```

#### AI Brain Example (requires OpenAI API Key)
```bash
python examples/ai_task.py
```

#### API Service
```bash
python api/main.py
```

#### API Test (API service must be running)
```bash
python examples/api_example.py
```

## API Documentation

Once the API service is running, visit `http://localhost:8000/docs` for complete API documentation.

### Main Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `POST /execute-task` - Execute predefined task
- `POST /execute-ai-task` - Execute AI-driven task

### Request Examples

#### Execute Simple Task
```json
{
  "url": "https://example.com",
  "steps": [
    {
      "action": "wait",
      "selector": "input[name='search']",
      "timeout": 10000,
      "description": "Wait for search box"
    },
    {
      "action": "type",
      "selector": "input[name='search']",
      "text": "Python automation",
      "description": "Type search term"
    },
    {
      "action": "click",
      "selector": "button[type='submit']",
      "description": "Click submit button"
    }
  ]
}
```

#### Execute AI Task
```json
{
  "goal": "Get page title",
  "url": "https://example.com"
}
```

## Project Structure

```
web-automation-bot/
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies
├── config.py                 # Configuration management
├── core/                     # Core functionality
│   ├── __init__.py
│   ├── browser_driver.py     # Browser driver
│   └── task_executor.py      # Task executor
├── ai_brain/                 # AI brain module
│   ├── __init__.py
│   ├── mcp_client.py         # MCP client
│   ├── llm_handler.py        # LLM handler
│   └── task_planner.py       # Task planner
├── api/                      # API service module
│   ├── __init__.py
│   ├── main.py               # FastAPI application
│   └── models.py             # Data models
├── examples/                 # Usage examples
│   ├── simple_task.py        # Simple task example
│   ├── ai_task.py            # AI task example
│   └── api_example.py        # API usage example
└── tests/                    # Test files
    ├── __init__.py
    ├── test_core.py          # Core functionality tests
    └── test_ai_brain.py      # AI brain tests
```

## Technology Stack

- **Python 3.8+** - Main programming language
- **Playwright** - Browser automation
- **FastAPI** - Web API framework
- **OpenAI GPT-4** - AI model
- **Pydantic** - Data validation
- **httpx** - HTTP client
- **pytest** - Testing framework

## Extending the Project

### Adding Browser Operations

Edit `core/browser_driver.py`:

```python
async def new_action(self, param: str) -> bool:
    """Add new browser action"""
    try:
        # Implement your action
        return True
    except Exception as e:
        logger.error(f"Action failed: {e}")
        return False
```

### AI Features

Edit `ai_brain/llm_handler.py` to customize AI behavior.

### API Endpoints

Edit `api/main.py` to add new endpoints:

```python
@app.post("/new-endpoint")
async def new_endpoint(request: NewRequestModel):
    # Implement your logic
    pass
```

## Running Tests

```bash
# Run all tests
pytest

# Run specific test files
pytest tests/test_core.py
pytest tests/test_ai_brain.py
```

## Deployment

### Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install chromium

COPY . .
EXPOSE 8000

CMD ["python", "api/main.py"]
```

### Environment Variables

Configure `OPENAI_API_KEY` for AI features.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License
