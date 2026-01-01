import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
from dotenv import load_dotenv

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="TechGadget Support", page_icon="🛍️", layout="wide")

# --- 2. SETUP API ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("⚠️ API Key not found! Check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# Precision Settings
generation_config = {
    "temperature": 0.3,
    "max_output_tokens": 2000, 
}

model = genai.GenerativeModel(
    model_name='gemini-flash-latest',
    generation_config=generation_config
)

# --- 3. CUSTOM UI ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .main-header {
        font-size: 2.5rem; color: #4CAF50; text-align: center; font-weight: 700; margin-bottom: 1rem;
    }
    .stChatMessage { border-radius: 15px; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- 4. LOAD KNOWLEDGE BASE ---
@st.cache_data
def load_all_data():
    try:
        df = pd.read_csv("data/dataset.csv")
        text_data = ""
        for index, row in df.iterrows():
            text_data += f"Q: {row['instruction']}\nA: {row['response']}\n---\n"
        return text_data
    except Exception as e:
        return ""

all_knowledge = load_all_data()

system_prompt = f"""
You are an advanced Customer Support AI for 'TechGadget Inc.'.
You have access to the following policy database.

DATABASE:
{all_knowledge}

RULES:
1. Answer using ONLY the database info.
2. If the answer isn't in the database, say "I don't have that info."
3. Maintain context.
4. Be professional but friendly. Use emojis occasionally.
"""

# --- 5. SIDEBAR UI ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100)
    st.title("TechGadget Support")
    st.markdown("---")
    st.write("👋 **Welcome!**")
    st.caption("📦 Order Tracking")
    st.caption("💸 Refunds & Returns")
    
    if st.button("🗑️ Reset Chat", type="primary"):
        st.session_state.messages = []
        st.rerun()
        
    st.markdown("---")
    st.caption("Powered by Gemini Flash")

# --- 6. MAIN CHAT INTERFACE ---
st.markdown('<div class="main-header">🛍️ Customer Support Center</div>', unsafe_allow_html=True)
st.caption("Ask me about your orders, refunds, or account settings!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your question here..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Memory Logic
    chat_history_text = ""
    for msg in st.session_state.messages[-6:]: 
        role = "User" if msg["role"] == "user" else "Agent"
        chat_history_text += f"{role}: {msg['content']}\n"

    final_prompt = f"{system_prompt}\n\nCONVERSATION HISTORY:\n{chat_history_text}\n\nUser: {prompt}\nAgent:"

    try:
        with st.spinner("Thinking..."):
            response = model.generate_content(final_prompt)
            bot_reply = response.text

        with st.chat_message("assistant"):
            st.markdown(bot_reply)
        
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        st.error(f"⚠️ Error: {e}")