# 🤖 AI-Powered Customer Support Chatbot (Task 3)

## 📌 Project Overview
This project was developed as **Task 3** of my Machine Learning Internship. The objective was to design and deploy an **Intelligent Customer Support Chatbot** capable of handling real-time user queries.

Instead of relying on traditional rule-based logic or manual neural network training, this solution leverages **Generative AI (Google Gemini)** to provide natural, context-aware responses. The chatbot utilizes `dataset.csv` as a knowledge base to answer user questions accurately and is deployed using **Streamlit** for a clean, interactive web interface.

---

## ✨ Key Features

### 🧠 Generative AI Integration
Powered by **Google's Gemini model**, the chatbot understands complex queries and conversational context without needing manual rule definitions. It can summarize data, answer specific questions, and handle follow-ups naturally.

### 📊 Data-Driven Responses
The application utilizes **Pandas** to load and process a structured dataset (`dataset.csv`). This allows the AI to ground its answers in specific business data rather than generating generic responses.

### 🌐 Streamlit Web Interface
The chatbot is deployed as a **Streamlit web application**, simulating a real-world customer support chat widget. This allows easy testing, demonstration, and interaction directly from the browser.

---

## 🛠️ Technologies Used
* **Python 3.x**
* **Streamlit** (User Interface)
* **Google Generative AI** (LLM / Chatbot Logic)
* **Pandas** (Data Handling & CSV Processing)
* **Python-dotenv** (Environment Variable Management)

---

## ⚙️ Architecture & Methodology

### 📂 Data Ingestion
- **Pandas** is used to load structured support data from the local `dataset.csv` file.
- The system prepares this data to be used as context for the AI model.

### 🤖 LLM Response Generation
- **Model:** Google Gemini (via `google.generativeai` API).
- **Process:** User queries are combined with relevant dataset context and sent to the API. The model generates a coherent, human-like response based on the provided data.

---

## 🚀 Installation & Usage

```bash
git clone https://github.com/SiddheshMurkute/FUTURE_ML_03.git
cd customer-support-chatbot

pip install -r requirements.txt

streamlit run app.py