![image](https://github.com/user-attachments/assets/eaca1af8-1b57-4e0f-9377-64ec97db7efa)

# 🐦 Langchain: Chat with SQL DB

A simple yet powerful LangChain-based web app that allows you to **interact with your SQL databases using natural language**. Built to support **SQLite** and other SQL-compatible databases, it leverages LLMs (via Groq API) to convert queries into structured SQL responses.

---

## ✨ Features

- 🗣️ **Natural Language to SQL**  
  Ask questions in plain English — get SQL query results.

- 💾 **Built-in SQLite3 Support**  
  Use the preloaded `Student.db` or connect your own SQL database.

- 🔐 **Groq API Integration**  
  Powered by LLMs for precise query interpretation and response generation.

- 🧹 **Clear Chat History**  
  Easily reset your conversation context.

---

## 📸 UI Overview

- Choose between built-in or custom DB.
- Paste your Groq API key for authorization.
- Ask questions like:  
  > "Show all students who scored above 90."  
  > "List all subjects offered in semester 2."

---


## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/sahil110802/chatsql.git
cd chatsql
pip install -r requirements.txt
streamlit run app.py
```

## 📌 Usage
- Select a Database

- Choose between:

- ✅ Use SQLite3 Database - Student.db

- 🔄 Connect to your SQL DB (e.g., MySQL, PostgreSQL, etc.)

- Enter Your Groq API Key

- Paste your valid Groq API Key into the input field.

This key enables access to the underlying large language model for query interpretation.

- Ask a Question in Plain English

- Type your question in the input box. For example:

“Show all students with marks above 85.”

“How many students failed in Science?”

“List students sorted by their total marks.”

- Get SQL-Driven Answers Instantly

- The app converts your natural language into SQL, runs it on the database, and shows results in a chat-style interface.

- Clear Session (Optional)

Click clear message history to reset the conversation context if needed.
