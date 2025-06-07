### 🤖 Simple Chatbot (SISA) — Smart Interactive Search Assistant

SISA is a terminal-based AI chatbot built using **Python**, designed to deliver intelligent, real-time responses using the **Google Gemini API** and **Google Programmable Search Engine (CSE)**. It supports both **Linux/macOS** and **Windows** platforms with tailored configurations.

---

### 📁 Project Structure

```
Simple-Chatbot-SISA--Project/
│
├── Simple_chatbot_linux_version/       # Linux/macOS compatible version
│   └── [source files, settings.json, instructions]
│
├── Simple_chatbot_windows_version/     # Windows-compatible version
│   └── [source files, settings.json, instructions]
│
├── Creator.md
└── README.md (this file)
```

---

### ✅ Requirements

- Python 3.8 or newer
- Internet connection
- API keys for:
  - Google Gemini API
  - Google Programmable Search (CSE)

---

### 🧩 How It Works

- The chatbot accepts questions via terminal input.
- If the query starts with `search`, it uses Google Search API.
- Otherwise, it uses Gemini (LLM) to generate the response.
- Commands like `help`, `exit`, or custom commands are also supported.

---

### 🔐 API Setup

You'll need 3 keys:

1. **Google Gemini API key** from [makersuite.google.com](https://makersuite.google.com/app/apikey)
2. **Google API Key** from [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
3. **Google Programmable Search Engine ID** from [programmablesearchengine.google.com](https://programmablesearchengine.google.com/about/)

Place them inside the `settings.json` file for each version:

```json
{
  "credentials": {
    "gemini": {
      "api-key": "your_gemini_api_key",
      "model-name": "gemini-pro"
    },
    "g-search": {
      "api-key": "your_google_api_key",
      "id": "your_search_engine_id"
    }
  }
}
```

---

### 🖥️ How to Run

### For Linux/macOS

```bash
cd Simple_chatbot_linux_version
python3 setup.py
python3 main.py
```

### For Windows

```bash
cd Simple_chatbot_windows_version
python setup.py
python main.py
```

---

### 📚 Files Overview

- `main.py` — Entry point of the chatbot
- `gemini.py` — Gemini AI interaction handler
- `search.py` — Google search handler
- `head.py` — Header and CLI utilities
- `settings.json` — API credentials and config
- `manual.txt` — Help guide
- `custom-cmds.json` — Optional command mappings

---

### ✨ Features

- AI-powered responses using Google Gemini
- Real-time search via Google Programmable Search
- Platform-specific UI (Colorama for Windows, ANSI for Linux/macOS)
- Fully modular and customizable

---


> ### Built to bring AI-powered assistance to your terminal — on any OS. 🚀
