import streamlit as st
from google import genai
from google.genai import types
import base64
import os

# --- Configuration ---
API_KEY = "Replace - Your - Google - Gemini - API - Key "
MODEL_NAME = "models/gemini-flash-latest"
SYSTEM_INSTRUCTION = """
You are an Airline Policy Expert Assistant.
Your goal is to explain airline policies clearly and consistently to passengers.

**Tone:**
*   Professional, helpful, concise, and polite.
"""

st.set_page_config(
    page_title="SkyHigh Airline Assistant",
    page_icon="✈️",
    layout="wide"
)

# --- Assets & Styling ---
def get_base64_image(image_path):
    if not os.path.exists(image_path):
        return ""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Load assets
bg_image_base64 = get_base64_image("assets/sky_bg.png")
bot_icon_path = "assets/bot_icon.png"

def local_css():
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        /* General App Styling */
        .stApp {{
            background-image: url("data:image/png;base64,{bg_image_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: 'Poppins', sans-serif;
        }}
        
        /* Glassmorphism Container */
        .glass-container {{
            background: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            border: 1px solid rgba(255, 255, 255, 0.18);
            margin-top: 20px;
            animation: slideIn 1s ease-out;
        }}

        /* Header Animation */
        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
            100% {{ transform: translateY(0px); }}
        }}
        
        .floating-header {{
            animation: float 4s ease-in-out infinite;
            text-align: center;
            color: #0d47a1;
            font-weight: 600;
            font-size: 3rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}

        .sub-text {{
            text-align: center;
            color: #333;
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }}

        /* Chat Animations */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .stChatMessage {{
            animation: fadeIn 0.5s ease-out;
            border-radius: 12px;
            margin-bottom: 10px;
        }}

        /* Role-specific styling override (Streamlit classes are generic, but we can target specific elements if needed) */
        
        </style>
        """, unsafe_allow_html=True)

local_css()

# --- Initialization ---
client = genai.Client(api_key=API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- UI Layout ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<div class='glass-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='floating-header'>✈️ SkyHigh Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-text'>Your personal travel guide. Ask me anything!</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Add a spacer
st.markdown("<br>", unsafe_allow_html=True)

# --- Chat Interface ---
# We use a container for the chat area
chat_container = st.container()

with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=bot_icon_path if message["role"] == "assistant" else None):
            st.markdown(message["content"])

# --- User Input & Logic ---
if prompt := st.chat_input("Where can I fly?"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant", avatar=bot_icon_path):
        message_placeholder = st.empty()
        full_response = ""
        
        chat_history_for_api = [
             types.Content(
                role="user" if m["role"] == "user" else "model",
                parts=[types.Part.from_text(text=m["content"])]
            )
            for m in st.session_state.messages
        ]

        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION
                ),
                contents=chat_history_for_api
            )
            full_response = response.text
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"⚠️ Error: {e}"
            message_placeholder.error(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
