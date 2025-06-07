# 🚀 How to Use the Simple Chatbot "SISA"(Linux/macOS Version)

Welcome! This guide explains how to set up and run the AI-powered chatbot on any **Linux or macOS** system.

---

## ✅ Requirements

Before starting, ensure you have:

- 🐍 **Python 3.8 or higher**
- 🌐 **Internet connection**
- 🔑 **API keys for:**
  - [Google Gemini](https://ai.google.dev)
  - [Google Programmable Search](https://programmablesearchengine.google.com)

---

## 📦 Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/isayani-78/simple-chatbot-project.git
cd simple-chatbot-project/Simple_chatbot_linux_version
```

---

### 2. Install Dependencies

Run the setup script (auto-installs packages from `settings.json`):

```bash
python3 setup.py
```

---

### 3. Add Your API Keys

Open `settings.json` and update it like this:

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

Run the chatbot with:

```bash
python3 main.py
```

You will see:
```bash
🤖 Ask me anything...
```

Now you can:
- Ask real-world questions
- Get smart answers from Gemini
- Type `search <query>` to fetch live web results
- Type `help` to see command instructions
- Type `exit` to quit the bot

---

## 🧪 Example Commands

```bash
What is the capital of Japan?
search Python web frameworks
help
exit
```

---

## ❓ Help & Troubleshooting

- 📂 `manual.txt` shows CLI help
- 🔧 Make sure Python is installed and added to your PATH
- 🛠️ If a package fails, rerun `setup.py` or install manually via:
  ```bash
  pip3 install -r requirements.txt
  ```

---

## 🙋 Author

Developed by: **Sayani Maity**
              **Srijan Bhattacharyya**
GitHub: [@isayani-78](https://github.com/isayani-78)
        [@srijan-76448](https://github.com/srijan-76448)

---

Enjoy your AI chatbot on Linux/macOS! 🎉
