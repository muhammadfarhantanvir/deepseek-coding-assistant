# DeepSeek Personal Coding Assistant



A Streamlit-based chat interface powered by Ollama and DeepSeek models, designed to provide intelligent coding assistance with real-time interaction capabilities.

## Key Features

- 🧠 Dual Model Support: Choose between deepseek-r1:1.5b and deepseek-r1:3b models
- 💬 Interactive Chat Interface: Modern UI with distinct user/AI message bubbles
- 🚀 Real-Time Processing: Streamlined pipeline for instant responses
- � Context-Aware Assistance: Maintains conversation history for coherent dialogs
- 🖥 Developer-Centric Design: Built-in guidance for strategic debugging

## Quick Start

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.com/) installed and running

### Installation
```bash
# Clone repository
git clone https://github.com/muhammadfarhantanvir/deepseek-coding-assistant
cd deepseek-coding-assistant

# Install dependencies
pip install -r requirements.txt

# Download DeepSeek models (run in separate terminal)
ollama pull deepseek-r1:1.5b
ollama pull deepseek-r1:3b

# Launch application
streamlit coding_assistant.py