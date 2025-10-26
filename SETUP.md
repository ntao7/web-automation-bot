# Setup Guide

## Installation Steps

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Playwright Browser

```bash
playwright install chromium
```

### 3. Configure Environment Variables (Optional)

Create a `.env` file:

```bash
copy .env.example .env
```

Then edit the `.env` file and add your OpenAI API Key (for AI features).

## Quick Test

### Test Core Functionality

```bash
python examples/simple_task.py
```

This example will:
- Start a browser
- Navigate to https://example.com
- Wait for the page to load
- Get the page title
- Display the result

### Test AI Functionality (Requires OpenAI API Key)

```bash
python examples/ai_task.py
```

### Start API Service

```bash
python api/main.py
```

Then run the test in another terminal:

```bash
python examples/api_example.py
```

Or visit http://localhost:8000/docs to view the API documentation.

## Usage Instructions

### 1. Using Core Features

Create a task configuration:

```python
from core.task_executor import TaskExecutor

task_config = {
    "url": "https://example.com",
    "steps": [
        {
            "action": "wait",
            "selector": "input[name='search']",
            "timeout": 10000
        },
        {
            "action": "type",
            "selector": "input[name='search']",
            "text": "Python automation"
        },
        {
            "action": "click",
            "selector": "button[type='submit']"
        }
    ]
}

executor = TaskExecutor()
result = await executor.execute_task(task_config)
```

### 2. Using AI Features

```python
from ai_brain.task_planner import AITaskPlanner

planner = AITaskPlanner()
result = await planner.execute_ai_task(
    goal="Buy the cheapest blue shirt",
    url="https://shop.example.com"
)
```

### 3. API Call Examples

#### Using curl

```bash
# Health check
curl http://localhost:8000/health

# Execute task
curl -X POST http://localhost:8000/execute-task \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com",
    "steps": [
      {
        "action": "get_text",
        "selector": "h1"
      }
    ]
  }'

# Execute AI task
curl -X POST http://localhost:8000/execute-ai-task \
  -H "Content-Type: application/json" \
  -d '{
    "goal": "Get page title",
    "url": "https://example.com"
  }'
```

## Common Issues

### Q: Playwright browser fails to start

A: Make sure you have run the `playwright install chromium` command.

### Q: AI functionality doesn't work

A: Check if you have configured the correct `OPENAI_API_KEY` in the `.env` file.

### Q: Page element not found

A: Use developer tools to inspect the page and ensure the selector is correct. Playwright supports multiple selector types: CSS, XPath, text selectors, etc.

### Q: API returns 502 error

A: Make sure the API service is running and check if port 8000 is available.

## Next Steps

- Check the `examples/` directory for more examples
- Read `README.md` for complete API documentation
- Check the `tests/` directory to learn how to write tests
