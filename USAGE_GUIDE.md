# Usage Guide - Direct Core Service Access

## Quick Start

### Method 1: Run Predefined Tasks

```bash
# Run Amazon search example
python amazon_search_example.py
```

### Method 2: Create Your Own Task

Create a new Python file, for example `my_task.py`:

```python
import asyncio
from core.task_executor import TaskExecutor

async def main():
    # Create task executor
    executor = TaskExecutor()
    
    # Define your task
    my_task = {
        "url": "https://example.com",
        "steps": [
            {
                "action": "wait",
                "selector": "input[type='search']",
                "timeout": 10000
            },
            {
                "action": "type",
                "selector": "input[type='search']",
                "text": "search keywords"
            },
            {
                "action": "click",
                "selector": "button[type='submit']"
            }
        ]
    }
    
    # Execute task
    result = await executor.execute_task(my_task)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Available Action Types

### 1. wait - Wait for Element to Appear

```python
{
    "action": "wait",
    "selector": "CSS selector",
    "timeout": 10000  # milliseconds, optional
}
```

### 2. type - Type Text

```python
{
    "action": "type",
    "selector": "input[name='username']",
    "text": "text to type"
}
```

### 3. click - Click Element

```python
{
    "action": "click",
    "selector": "button.submit"
}
```

### 4. get_text - Get Element Text

```python
{
    "action": "get_text",
    "selector": "h1.title"
}
```

### 5. screenshot - Take Screenshot

```python
{
    "action": "screenshot",
    "path": "screenshot.png"  # optional, default screenshot.png
}
```

---

## Complete Examples

### Example 1: Search on DuckDuckGo

```python
import asyncio
from core.task_executor import TaskExecutor

async def main():
    executor = TaskExecutor()
    
    task = {
        "url": "https://duckduckgo.com",
        "steps": [
            {
                "action": "wait",
                "selector": "#searchbox_input",
                "timeout": 10000
            },
            {
                "action": "type",
                "selector": "#searchbox_input",
                "text": "Python programming"
            },
            {
                "action": "click",
                "selector": "button[type='submit']"
            },
            {
                "action": "screenshot",
                "path": "search_result.png"
            }
        ]
    }
    
    result = await executor.execute_task(task)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

### Example 2: Get Page Title

```python
import asyncio
from core.task_executor import TaskExecutor

async def main():
    executor = TaskExecutor()
    
    task = {
        "url": "https://example.com",
        "steps": [
            {
                "action": "wait",
                "selector": "h1",
                "timeout": 5000
            },
            {
                "action": "get_text",
                "selector": "h1"
            }
        ]
    }
    
    result = await executor.execute_task(task)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

