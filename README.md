# Gemini Multi-turn Chat (CLI)

A command-line interface (CLI) that allows you to have a multi-turn conversation with Google's Gemini 1.5 Flash model. This script uses the official `google-generativeai` Python SDK and supports configurable creativity using the temperature setting.

---

## 🧠 What This Script Does

- Loads your API key securely from a `.env` file.
- Initiates a chat session using Gemini 1.5 Flash model.
- Supports multi-turn conversations with memory (chat history).
- Allows user to configure the response temperature interactively.

---

## ⚙️ Setup & How to Run

### 1. Clone This Repository

```bash
git clone https://github.com/Ankitshankhala/gemini-multi-turn-chat.git
cd gemini-multi-turn-chat
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, install manually:
```bash
pip install python-dotenv google-generativeai
```

### 3. Create a `.env` File

In the project root, create a `.env` file and add your Gemini API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

> 🔐 **Never share your real `.env` or API key on GitHub.**

### 4. Run the Chat Script

```bash
python gemini_chat.py
```

You’ll be prompted to enter a temperature (0.2 = focused, 0.9 = creative).

Type messages interactively and type `exit` to end the session.

---

## 💬 Example Session

```
Set temperature (e.g. 0.2 for focused, 0.9 for creative): 0.3

Gemini Chat Started! Type 'exit' to quit.

User (1): Hello!
Gemini (1): Hi there! How can I help you today?
User (2): Tell me a joke.
Gemini (2): Why don’t scientists trust atoms? Because they make up everything!
User (3): exit
```

---

## 📁 Files

- `gemini_chat.py` — Main Python chat script.
- `.env.example` — Example `.env` file for safe sharing.
- `output.PNG` — Screenshot of CLI session.
- `README.md` — This file.

---

## ✅ Notes

- Make sure `.env` is **not** tracked in Git.
- Error: `GEMINI_API_KEY not found`? → Your `.env` may be missing or misconfigured.

---

## 📜 License

MIT License © [Ankit Shankhala](https://github.com/Ankitshankhala)