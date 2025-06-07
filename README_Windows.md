# 🤖 Simple Chatbot (Windows Version)

This is the **Windows-compatible version** of a modular AI-powered chatbot built in Python. It uses:

- [Google Gemini API](https://ai.google.dev)
- [Google Custom Search API](https://programmablesearchengine.google.com)
- [colorama](https://pypi.org/project/colorama/) for colored terminal output in CMD/PowerShell

---

## 🧠 Features

- 🤖 Chat with Google's Gemini
- 🔍 Fetch live internet results with Google Search
- 🖼️ Colored terminal output (via `colorama`)
- 🔐 Modular and secure API configuration

---

## 🔧 Setup Instructions

### 1. Install Dependencies

Open CMD or PowerShell and run:

```bash
python setup.py
```

It auto-installs all required packages from `settings.json`.

---

### 2. Add Your API Keys

Edit the `settings.json` file:

```json
"credentials": {
  "gemini": {
    "api-key": "your_gemini_api_key",
    "model-name": "gemini-pro"
  },
  "g-search": {
    "api-key": "your_google_search_api_key",
    "id": "your_custom_search_engine_id"
  }
}
```

Get your keys from:
- 🔑 [Gemini API](https://ai.google.dev)
- 🔍 [Google Programmable Search Engine](https://programmablesearchengine.google.com)

---

### 3. Run the Chatbot

```bash
python main.py
```

The chatbot will respond using Gemini and/or Google Search depending on your queries.

---

## 📄 Files Overview

```
├── main.py             # Chatbot CLI interface
├── setup.py            # Auto dependency installer
├── gemini.py           # Gemini API integration (colorama-based)
├── search.py           # Google Search integration (colorama-based)
├── head.py             # Bot personality & common responses
├── settings.json       # API keys & config
├── custom-cmds.json    # Optional phrases/responses
├── guide.json          # API acquisition help
├── manual.txt          # Help file displayed in CLI
```

---

## 💡 Note for Windows Users

This version uses `colorama` to correctly display colored text in:
- CMD
- PowerShell
- Windows Terminal

No additional setup is needed for ANSI support.

---

## 🙋 Author

Created by: **Your Name**  
GitHub: [@your-username](https://github.com/your-username)---

## ✅ Before You Run (Checklist for Windows Users)

Make sure you have the following ready:

| Requirement                  | Status | Notes |
|-----------------------------|--------|-------|
| 🐍 Python 3.8 or higher      | ✅     | Add to PATH or use full path |
| 🌐 Internet connection       | ✅     | Needed for API access |
| 🔑 Gemini API key            | ✅     | Add to `settings.json` |
| 🔍 Google Search API key     | ✅     | Add to `settings.json` |
| 📦 Dependencies installed    | ✅     | Run `python setup.py` once |
| 🧠 Gemini model name         | ✅     | Default: `gemini-pro` |
| 🛠️ Run the bot using         | ✅     | `python main.py` |

📌 If all boxes are ✅, your chatbot will run smoothly on **Windows CMD / PowerShell / Terminal**.