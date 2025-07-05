# OpenRouter API Utility Functions

This directory contains reusable functions for making API calls to OpenRouter, allowing you to easily switch between different AI models.

## Files

- `openrouter_utils.py` - Main utility functions
- `openrouter_example.py` - Example usage and demonstrations
- `README_openrouter.md` - This documentation

## Setup

1. **Get an OpenRouter API Key**: Visit [OpenRouter](https://openrouter.ai/) and create an account to get your API key.

2. **Set Environment Variable**: Add your API key to your environment:
   ```bash
   export OPENROUTER_API_KEY="your_api_key_here"
   ```
   
   Or create a `.env` file:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

3. **Install Dependencies**: Make sure you have the required packages:
   ```bash
   pip install requests python-dotenv
   ```

## Usage

### Basic Usage

```python
from openrouter_utils import call_openrouter_api, get_model_response

# Simple question
messages = [{"role": "user", "content": "What is the capital of France?"}]
response = call_openrouter_api(messages)

if response:
    content = get_model_response(response)
    print(content)
```

### Selecting Different Models

```python
# Use GPT-4o-mini (default)
response = call_openrouter_api(messages, model="openai/gpt-4o-mini")

# Use Claude
response = call_openrouter_api(messages, model="anthropic/claude-3-5-sonnet")

# Use Gemini
response = call_openrouter_api(messages, model="google/gemini-2.0-flash")

# Use Llama
response = call_openrouter_api(messages, model="meta-llama/llama-3.1-8b-instruct")
```

### Advanced Parameters

```python
response = call_openrouter_api(
    messages=messages,
    model="openai/gpt-4o-mini",
    temperature=0.7,    # Controls randomness (0.0 to 2.0)
    max_tokens=1000,    # Maximum tokens to generate
    api_key="custom_key"  # Optional: override API key
)
```

### Multi-turn Conversations

```python
conversation = [
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi there! How can I help you?"},
    {"role": "user", "content": "Tell me about machine learning."}
]

response = call_openrouter_api(conversation, model="anthropic/claude-3-5-sonnet")
```

## Available Models

OpenRouter provides access to many models. Here are some popular ones:

- **OpenAI Models**: `openai/gpt-4o-mini`, `openai/gpt-4o`, `openai/gpt-4-turbo`
- **Anthropic Models**: `anthropic/claude-3-5-sonnet`, `anthropic/claude-3-opus`
- **Google Models**: `google/gemini-2.0-flash`, `google/gemini-2.0-exp`
- **Meta Models**: `meta-llama/llama-3.1-8b-instruct`, `meta-llama/llama-3.1-70b-instruct`
- **Microsoft Models**: `microsoft/wizardlm-2-8x22b`

For a complete list, visit [OpenRouter Models](https://openrouter.ai/models).

## Error Handling

The functions include built-in error handling:

```python
response = call_openrouter_api(messages, model="invalid/model")
if response is None:
    print("API call failed - check your API key and model name")
```

## Running Examples

To see the functions in action:

```bash
python openrouter_example.py
```

This will demonstrate various use cases including:
- Simple questions
- Creative tasks
- Code generation
- Multi-turn conversations
- Error handling

## Integration with Jupyter Notebooks

You can import and use these functions in your Jupyter notebooks:

```python
# In a notebook cell
from openrouter_utils import call_openrouter_api, get_model_response

messages = [{"role": "user", "content": "Explain quantum computing in simple terms."}]
response = call_openrouter_api(messages, model="anthropic/claude-3-5-sonnet")

if response:
    print(get_model_response(response))
```

## Tips

1. **Model Selection**: Different models excel at different tasks:
   - GPT-4o-mini: Good all-around performance, cost-effective
   - Claude: Excellent for reasoning and analysis
   - Gemini: Good for creative tasks
   - Llama: Good for coding tasks

2. **Temperature**: 
   - Lower (0.1-0.3): More deterministic, good for factual responses
   - Higher (0.7-1.0): More creative, good for brainstorming

3. **Rate Limits**: Be mindful of API rate limits, especially when testing multiple models.

4. **Cost**: Different models have different pricing. Check [OpenRouter Pricing](https://openrouter.ai/pricing) for details. 