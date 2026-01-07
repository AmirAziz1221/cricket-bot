# 🏏 RAG-Based Cricket Chatbot

**A full-stack intelligent conversational agent capable of answering cricket-related queries using Retrieval-Augmented Generation (RAG).**

---
### 🎓 Academic Context (Semester Project)

- **Course:** Computational Intelligence
- **Instructor:** Mr. Hamas ur Rehman
- **Instructor GitHub:** [Hamas-ur-Rehman](https://github.com/Hamas-ur-Rehman)
- **Project Type:** Semester Project

> This project was developed and submitted as part of the **Computational Intelligence** course, demonstrating practical application of modern AI techniques including **RAG pipelines**, **vector databases**, and **large language models**.

### 👥 Group Members
| Name | Registration Number | Role |
| :--- | :--- | :--- |
| **Amir Aziz** | 22PWDSC0062 | Data Science / Backend Logic |
| **Laiba Wahab** | 22PWDSC0051 | Frontend / UI Integration |
| **Wahid Ali** | 22PWDSC0054 | API / System Architecture |

---

## 📖 Project Overview
This project implements a domain-specific chatbot focusing on the sport of **Cricket**. Unlike generic chatbots, this system uses **RAG (Retrieval-Augmented Generation)** to fetch real-time, factual context from Wikipedia before generating an answer. This ensures high accuracy and reduces hallucinations common in standard LLMs.

The system is built using a modern AI stack:
* **LangChain:** For orchestrating the RAG pipeline.
* **FastAPI:** Serves the backend API.
* **NVIDIA NIM & Cohere:** For high-performance LLM inference and embeddings.
* **ReactJS:** Provides a responsive, chat-interface frontend.

---

## 📂 Project Structure

```text
root/
├── cricket_bot_api/       # Backend (FastAPI & Logic)
│   ├── cricket_bot_api.py     # Main Server File
│   ├── cricket_bot_data.py    # Data Processing Script
│   └── requirements.txt       # Python Dependencies
│
├── frontend/              # Frontend (ReactJS)
│   ├── public/
│   ├── src/
│   └── package.json
│
├── .env                   # API Keys (NVIDIA & Cohere)
├── .gitignore             # Files to ignore in Git
├── cricket_bot.ipynb      # Jupyter Notebook for testing/experiments
└── README.md              # Project Documentation
```
## 🚀 Installation & Setup Guide

Follow these steps to run the project locally.

### Prerequisites
* **Python 3.8+**
* **Node.js & npm** (for the frontend)
* **API Keys:**
    * Cohere API Key (Free tier available)
    * NVIDIA NIM API Key (Free tier available)

### Step 1: Configuration
1. Open the `.env` file in the main folder.
2. Add your API keys inside it:
    ```env
    NVIDIA_API_KEY=nvapi-your-key-here
    COHERE_API_KEY=your-cohere-key-here
    ```

### Step 2: Backend Setup
1. Open a terminal and navigate to the backend folder:
    ```bash
    cd cricket_bot_api
    ```
2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Start the Backend Server:
    ```bash
    uvicorn cricket_bot_api:app --reload
    ```
    *Wait until you see "Application startup complete". The first run will download Wikipedia data.*

### Step 3: Frontend Setup
1. Open a **new terminal** and navigate to the frontend folder:
    ```bash
    cd frontend
    ```
2. Install Node dependencies:
    ```bash
    npm install
    ```
3. Start the React App:
    ```bash
    npm start
    ```
    *This will automatically open the chat interface in your browser at `http://localhost:3000`.*

---

## 🧪 How to Use
1. Ensure both the **Backend** (port 8000) and **Frontend** (port 3000) are running.
2. Go to your browser at `http://localhost:3000`.
3. Type a question in the chat box. Examples:
    * *"Who won the 1992 Cricket World Cup?"*
    * *"Explain the LBW rule."*
    * *"Who is the highest run scorer in Test cricket?"*
4. The bot will retrieve the relevant context from its vector store and generate a precise answer.

---

## 🔮 Future Improvements
* **Persistent Database:** Save chat history using PostgreSQL or MongoDB.
* **Live Score Integration:** Connect to a live cricket API for real-time match updates.
* **Voice Support:** Add Speech-to-Text to allow voice queries.
---
---