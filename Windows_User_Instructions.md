# 🚀 How to Use the Simple Chatbot "SISA" (Windows Version)

Welcome! This guide explains how to set up and run the AI-powered chatbot on **Windows (CMD, PowerShell, or Windows Terminal)**.

---

## ✅ Requirements

Before starting, ensure you have:

- 🐍 **Python 3.8 or higher** (added to your system PATH)
- 🌐 **Internet connection**
- 🔑 **API keys for:**
  - [Google Gemini](https://ai.google.dev)
  - [Google Programmable Search](https://programmablesearchengine.google.com)

---

## 📦 Installation Steps

### 1. Clone the Repository

Open Command Prompt or PowerShell:

```bash
git clone https://github.com/isayani-78/simple-chatbot-project.git
cd simple-chatbot-project\Simple_chatbot_windows_version
```

---

### 2. Install Dependencies

Run the setup script (auto-installs packages listed in `settings.json`):

```bash
python setup.py
```

---

### 3. Add Your API Keys

Open the `settings.json` file and insert your credentials like this:

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

---

## 💬 How to Use the Chatbot

To start the chatbot:

```bash
python main.py
```

You’ll see:

```text
🤖 Ask me anything...
```

Now you can:
- Ask smart questions
- Use `search <query>` to get live web results
- Type `help` to see available commands
- Type `exit` to quit the program

---

## 🧪 Example Commands

```bash
Tell me a joke
search best VS Code extensions
help
exit
```

---

## ❓ Help & Troubleshooting

- Run `setup.py` to install missing packages
- `manual.txt` provides help inside the CLI
- If Python isn’t recognized, ensure it's added to your system’s PATH

---

## 💡 Note

- This version uses `colorama` to display colored output properly on Windows
- Works in:  
  ✅ CMD  
  ✅ PowerShell  
  ✅ Windows Terminal

---

## 🙋 Author

Developed by: **Sayani Maity**  
GitHub: [@isayani-78](https://github.com/isayani-78)

---

Enjoy chatting with your AI bot on Windows! 🎉
