# SkyHigh Airline Assistant ✈️

A modern, interactive conversational AI assistant built with **Python**, **Streamlit**, and the **Google GenAI SDK (Gemini)**. This application acts as an Airline Policy Expert, designed to explain airline policies clearly and consistently to passengers with a professional and helpful tone.

## 🌟 Features

- **Generative AI Integration:** Powered by Google's Gemini models (`gemini-flash-latest`) using the modern `google-genai` Python SDK.
- **Custom System Instructions:** The AI is strictly guided by system prompts to act as a specialized Airline Policy Expert Assistant, ensuring responses are professional, concise, and polite.
- **Engaging UI/UX:** Features a custom frontend built over Streamlit using injected CSS:
  - **Glassmorphism Design:** Semi-transparent, blurred containers for a sleek, modern look.
  - **Dynamic Animations:** Floating headers and smooth fade-in effects for chat messages.
  - **Custom Assets:** Supports background images and custom avatars for the AI bot.
- **Stateful Conversations:** Maintains context throughout the chat session using Streamlit's `session_state`, allowing for natural, multi-turn conversations.

## 🛠️ Tech Stack

- **Language:** Python 3
- **Framework:** Streamlit (for rapid UI development and web hosting)
- **AI/LLM:** Google GenAI API (Gemini Flash)
- **Styling:** Custom HTML/CSS (embedded within Streamlit)

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- A Google Gemini API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd google_genai_test
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API Key:**
   Create a `.env` file in the root directory (you can copy `.env.example`) and add your actual Google Gemini API key:
   ```bash
   GEMINI_API_KEY="your_actual_api_key_here"
   ```
   *(Note: For production, it is highly recommended to use environment variables or Streamlit secrets instead of hardcoding the API key).*

### Running the App

Execute the following command in your terminal:
```bash
streamlit run app.py
```
The app will automatically open in your default web browser at `http://localhost:8501`.

## 💡 What I Learned (Resume Highlights)

- **AI Integration:** Gained hands-on experience integrating Large Language Models (LLMs) into applications using the latest Google GenAI SDK.
- **Prompt Engineering:** Used System Instructions to define the AI's persona, scope, and tone of voice.
- **Frontend Customization:** Bypassed standard Streamlit UI limitations by injecting custom CSS to achieve a modern "glassmorphism" aesthetic and CSS keyframe animations.
- **State Management:** Effectively managed chat history and user sessions using Streamlit's internal state mechanism to pass full context to the AI model.
