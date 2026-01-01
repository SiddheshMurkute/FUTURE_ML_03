# 🤖 AI-Powered Customer Support Chatbot (Task 3)

## 📌 Project Overview
This project was developed as **Task 3** of my Machine Learning Internship. The objective was to design and deploy an **intelligent customer support chatbot** capable of handling real-time user queries using **Deep Learning and Natural Language Processing (NLP)** instead of traditional rule-based logic.

The chatbot understands user intent, responds to Frequently Asked Questions (FAQs), guides users through predefined support flows, and gracefully handles unknown or ambiguous queries. The application is deployed using **Streamlit**, providing a clean and interactive web-based interface for real-time interaction.

---

## ✨ Key Features

### 🔍 Intelligent Intent Recognition
The chatbot uses a trained **neural network classifier** to identify user intent rather than relying on simple keyword matching. This enables it to correctly interpret different phrasings of the same query (e.g., *“Where is my order?”* vs. *“Track my shipment”*).

### 🛡️ Smart Fallback Handling
To ensure robustness, the system includes a confidence-based fallback mechanism. If the predicted intent confidence is low, the chatbot responds politely, informs the user that it did not understand the request, and suggests alternative topics or escalation to human support.

### 🌐 Streamlit Web Interface
The chatbot is deployed as a **Streamlit web application**, simulating a real-world customer support chat widget. This allows easy testing, demonstration, and interaction directly from the browser.

---

## 🛠️ Technologies Used
- **Python 3.x**
- **TensorFlow & Keras**
- **NLTK**
- **Streamlit**
- **Pickle**

---

## 🧠 Model Architecture & Methodology

### 📊 Data Preprocessing
- Text cleaning and normalization  
- Tokenization  
- Lemmatization  
- Vocabulary creation  
- Bag-of-Words feature vectors  

### 🧩 Neural Network Architecture
- **Input Layer:** Vocabulary size  
- **Hidden Layers:** Dense + ReLU + Dropout  
- **Output Layer:** Softmax activation  

### ⚙️ Optimization
- **Optimizer:** Stochastic Gradient Descent (SGD)  
- **Loss Function:** Categorical Cross-Entropy  

---

## 🚀 Installation & Usage

```bash
git clone https://github.com/your-username/customer-support-chatbot.git

pip install -r requirements.txt

streamlit run app.py

