# AI/ML Learning Assistant

A beginner-friendly AI/ML learning assistant built with Python, Ollama, Llama 3.2, prompt engineering, and Streamlit.

## Features

- 💬 Conversational AI
- 🧠 Conversation memory
- 📚 AI/ML topic explanations
- 📝 Quiz generation
- 💻 Code explanation
- 🗑️ Conversation reset
- ⚠️ Error handling
- 🌐 Streamlit web interface
- 🔒 Runs locally using Ollama(LLM)

## Technologies

- Python
- Ollama
- Llama 3.2
- Streamlit
- Prompt Engineering
- Git
- GitHub

## How It Works

```text
User
 ↓
Streamlit
 ↓
Python
 ↓
Ollama
 ↓
Llama 3.2
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sesadi13/AI-ML-Learning-Assistant.git
cd AI-ML-Learning-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv env
```

### 3. Activate the environment

Windows:

```powershell
.\env\Scripts\Activate.ps1
```

### 4. Install Python packages

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Install Ollama and download the Llama 3.2 model:

```bash
ollama pull llama3.2:3b
```

### 6. Run Ollama

```bash
ollama serve
```

### 7. Run the Streamlit application

Open another terminal and run:

```bash
streamlit run streamlit_app.py
```

The application will open in your browser.

## Future Improvements

* Better UI
* Multiline code input
* More learning commands
* Model selection
* Conversation export
