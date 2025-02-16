import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# Updated CSS styling for a modern look with a white background
st.markdown("""
<style>
    /* Overall page background */
    body {
        background: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main {
        background-color: white;
        color: #000;
    }
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #f0f0f0;
    }
    /* Chat input styling */
    .stTextInput textarea {
        color: #000 !important;
        background-color: #f8f8f8 !important;
        border: none;
    }
    /* Chat bubble styling */
    .chat-message {
        border-radius: 10px;
        padding: 10px 15px;
        margin: 10px 0;
        max-width: 80%;
        line-height: 1.5;
    }
    .chat-message.user {
        background-color: #4a90e2;
        color: #fff;
        align-self: flex-end;
        margin-left: auto;
    }
    .chat-message.ai {
        background-color: #f0f0f0;
        color: #000;
        align-self: flex-start;
        margin-right: auto;
    }
    /* Selectbox styling */
    .stSelectbox div[data-baseweb="select"] {
        color: black !important;
        background-color: #f8f8f8 !important;
    }
    .stSelectbox svg {
        fill: black !important;
    }
    .stSelectbox option {
        background-color: #f0f0f0 !important;
        color: black !important;
    }
    div[role="listbox"] div {
        background-color: #f0f0f0 !important;
        color: black !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 Your Personal Coding Assistant")

# Sidebar configuration with an updated header
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: black;'>Model Configuration</h2>", unsafe_allow_html=True)
    selected_model = st.selectbox(
        "Choose Your Model",
        ["deepseek-r1:1.5b", "deepseek-r1:3b"],
        index=0
    )
    
# Initiate the chat engine
llm_engine = ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",
    temperature=0.3
)

# System prompt configuration
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions "
    "with strategic print statements for debugging. Always respond in English."
)

# Session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]

# Chat container
chat_container = st.container()

# Display chat messages with custom chat bubbles
with chat_container:
    for message in st.session_state.message_log:
        role = message["role"]
        content = message["content"]
        bubble_class = "ai" if role == "ai" else "user"
        st.markdown(f"<div class='chat-message {bubble_class}'>{content}</div>", unsafe_allow_html=True)

# Chat input and processing
user_query = st.chat_input("Type your coding question here...")

def generate_ai_response(prompt_chain):
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

if user_query:
    # Add user message to log
    st.session_state.message_log.append({"role": "user", "content": user_query})
    
    # Generate AI response
    with st.spinner("🧠 Processing..."):
        prompt_chain = build_prompt_chain()
        ai_response = generate_ai_response(prompt_chain)
    
    # Add AI response to log
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    
    # Rerun to update chat display
    st.rerun()
