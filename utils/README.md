# Utils Module

A comprehensive utility module for the agents project, providing reusable functions for API interactions, file operations, and common helper functions.

## Module Structure

```
utils/
├── __init__.py              # Main module exports
├── README.md               # This documentation
├── api/                    # API-related utilities
│   ├── __init__.py
│   ├── openrouter_utils.py
│   └── openrouter_example.py
└── helpers/                # General helper functions
    └── __init__.py
```

## Quick Start

### Basic Import

```python
# Import the entire utils module
import utils

# Use OpenRouter API
response = utils.call_openrouter_api([{"role": "user", "content": "Hello!"}])
print(utils.get_model_response(response))

# Use helper functions
utils.load_env_file()
utils.check_api_key("OPENROUTER_API_KEY")
```

### Specific Imports

```python
# Import specific functions
from utils import call_openrouter_api, get_model_response, check_api_key

# Use directly
response = call_openrouter_api([{"role": "user", "content": "Hello!"}])
content = get_model_response(response)
check_api_key("OPENAI_API_KEY")
```

### Submodule Imports

```python
# Import from specific submodules
from utils.api import call_openrouter_api
from utils.helpers import load_env_file, save_json

# Use functions
load_env_file()
response = call_openrouter_api([{"role": "user", "content": "Hello!"}])
save_json(response, "response.json")
```

## API Utilities

### OpenRouter API Functions

The `utils.api` submodule provides functions for interacting with OpenRouter API:

#### `call_openrouter_api()`

Main function for making OpenRouter API calls.

```python
from utils import call_openrouter_api

# Basic usage
messages = [{"role": "user", "content": "What is the capital of France?"}]
response = call_openrouter_api(messages)

# With custom parameters
response = call_openrouter_api(
    messages=messages,
    model="anthropic/claude-3-5-sonnet",
    temperature=0.7,
    max_tokens=1000
)
```

#### `get_model_response()`

Extract the model's response text from the API response.

```python
from utils import get_model_response

response = call_openrouter_api(messages)
content = get_model_response(response)
print(content)
```

#### `get_usage_info()`

Get token usage information from the API response.

```python
from utils import get_usage_info

response = call_openrouter_api(messages)
usage = get_usage_info(response)
print(f"Tokens used: {usage}")
```

#### `quick_openrouter_call()`

Convenience function for simple API calls.

```python
from utils import quick_openrouter_call

# Simple one-liner
response = quick_openrouter_call("What is the capital of France?")
print(response)

# With custom model
response = quick_openrouter_call("Write a poem", model="anthropic/claude-3-5-sonnet")
print(response)
```

## Helper Functions

The `utils.helpers` submodule provides common utility functions:

### Environment Management

#### `load_env_file()`

Load environment variables from a .env file.

```python
from utils import load_env_file

# Load default .env file
load_env_file()

# Load custom env file
load_env_file("custom.env")
```

#### `check_api_key()`

Check if an API key is set in environment variables.

```python
from utils import check_api_key

# Check various API keys
check_api_key("OPENROUTER_API_KEY")
check_api_key("OPENAI_API_KEY")
check_api_key("ANTHROPIC_API_KEY")
```

### File Operations

#### `save_json()` and `load_json()`

Save and load JSON data.

```python
from utils import save_json, load_json

# Save data
data = {"response": "Hello world", "model": "gpt-4"}
save_json(data, "output.json")

# Load data
loaded_data = load_json("output.json")
print(loaded_data)
```

#### `ensure_directory()`

Ensure a directory exists, create it if it doesn't.

```python
from utils import ensure_directory

# Create directory if it doesn't exist
ensure_directory("output/results")
```

### Display Helpers

#### `format_messages_for_display()`

Format a list of messages for display.

```python
from utils import format_messages_for_display

messages = [
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi there! How can I help you?"}
]

formatted = format_messages_for_display(messages)
print(formatted)
```

## Usage Examples

### Complete Workflow Example

```python
import utils

# 1. Load environment
utils.load_env_file()

# 2. Check API keys
utils.check_api_key("OPENROUTER_API_KEY")

# 3. Make API call
messages = [{"role": "user", "content": "Explain quantum computing"}]
response = utils.call_openrouter_api(
    messages, 
    model="anthropic/claude-3-5-sonnet"
)

# 4. Extract response
content = utils.get_model_response(response)

# 5. Save results
utils.ensure_directory("output")
utils.save_json({
    "prompt": messages[0]["content"],
    "response": content,
    "model": response.get("model"),
    "usage": utils.get_usage_info(response)
}, "output/quantum_computing_response.json")

print("Response saved successfully!")
```

### Jupyter Notebook Usage

```python
# In a Jupyter notebook cell
from utils import quick_openrouter_call, check_api_key

# Check setup
check_api_key("OPENROUTER_API_KEY")

# Quick test
response = quick_openrouter_call("What is machine learning?")
print(response)
```

### Testing Different Models

```python
from utils import call_openrouter_api, get_model_response

models = [
    "openai/gpt-4o-mini",
    "anthropic/claude-3-5-sonnet",
    "google/gemini-2.0-flash"
]

question = "What is the meaning of life?"

for model in models:
    print(f"\n=== Testing {model} ===")
    response = call_openrouter_api([{"role": "user", "content": question}], model=model)
    if response:
        content = get_model_response(response)
        print(content[:200] + "..." if len(content) > 200 else content)
```

## Configuration

### Environment Variables

Set up your environment variables in a `.env` file:

```bash
# .env file
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

### Available Models

OpenRouter provides access to many models:

- **OpenAI**: `openai/gpt-4o-mini`, `openai/gpt-4o`, `openai/gpt-4-turbo`
- **Anthropic**: `anthropic/claude-3-5-sonnet`, `anthropic/claude-3-opus`
- **Google**: `google/gemini-2.0-flash`, `google/gemini-2.0-exp`
- **Meta**: `meta-llama/llama-3.1-8b-instruct`, `meta-llama/llama-3.1-70b-instruct`

For a complete list, visit [OpenRouter Models](https://openrouter.ai/models).

## Error Handling

All functions include built-in error handling:

```python
from utils import call_openrouter_api

# Invalid model
response = call_openrouter_api([{"role": "user", "content": "Hello"}], model="invalid/model")
if response is None:
    print("API call failed - check your API key and model name")

# Missing API key
response = call_openrouter_api([{"role": "user", "content": "Hello"}])
if response is None:
    print("API call failed - check your OPENROUTER_API_KEY")
```

## Contributing

To add new utilities to this module:

1. **API functions**: Add to `utils/api/` directory
2. **Helper functions**: Add to `utils/helpers/` directory
3. **Update exports**: Add new functions to the appropriate `__init__.py` files
4. **Add documentation**: Update this README with usage examples

## Dependencies

Required packages:
- `requests` - For API calls
- `python-dotenv` - For environment variable management

Install with:
```bash
pip install requests python-dotenv
``` 