import sys
import os
import re

# Fix import paths
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

import streamlit as st
from streamlit_mic_recorder import mic_recorder
from core.orchestrator import Orchestrator
from pydub import AudioSegment

st.set_page_config(page_title="OmniText AI", layout="wide")

st.title("🧠 OmniText AI")
st.write("An AI-powered multi-modal NLP platform that understands, analyzes, and generates human language from text, voice, and documents.")

orchestrator = Orchestrator()

# 🔥 Convert Markdown (**bold**) → HTML
def format_text(text):
    # Bold conversion
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)

    # Bullet points
    text = text.replace("•", "<br>•")
    text = text.replace("- ", "<br>• ")

    # Line breaks
    text = text.replace("\n", "<br>")

    return text

# 🔥 Clean Output Renderer
def render_output(text):
    formatted_text = format_text(text)

    st.markdown("### 🤖 AI Output")
    st.markdown(
        f"""
<div style="
    padding: 15px;
    border-radius: 10px;
    background-color: transparent;
    border: 1px solid #444;
    font-size: 16px;
    line-height: 1.6;
">
{formatted_text}
</div>
""",
        unsafe_allow_html=True
    )

# Input modes
mode = st.radio("Choose Input Mode:", ["Text", "Voice", "PDF"])

# ======================
# TEXT INPUT
# ======================
if mode == "Text":
    user_input = st.text_area("Enter your request:")

    if st.button("Run"):
        if user_input.strip():
            result = orchestrator.run(user_input)
            render_output(result)
        else:
            st.markdown("⚠️ Please enter some text.")

# ======================
# VOICE INPUT
# ======================
elif mode == "Voice":
    st.subheader("🎙️ Record your voice")

    audio = mic_recorder(
        start_prompt="🎤 Start Recording",
        stop_prompt="⏹️ Stop Recording",
        just_once=True
    )

    if audio:
        try:
            with open("temp_audio.webm", "wb") as f:
                f.write(audio["bytes"])

            sound = AudioSegment.from_file("temp_audio.webm")
            sound.export("temp_audio.wav", format="wav")

            from llm.whisper_client import transcribe_audio
            text = transcribe_audio("temp_audio.wav")

            st.markdown(f"**📝 Transcribed:** {text}")

            if text.strip():
                result = orchestrator.run(text)
                render_output(result)
            else:
                st.markdown("❌ No speech detected. Try speaking clearly.")

        except Exception as e:
            st.markdown(f"❌ Voice processing failed: {str(e)}")

# ======================
# PDF INPUT (RAG)
# ======================
elif mode == "PDF":
    st.markdown("### 📄 Upload PDF for Q&A")

    pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
    question = st.text_input("Ask a question about PDF:")

    if pdf_file and question.strip():
        from retrieval.retriever import process_pdf_query

        answer = process_pdf_query(pdf_file, question)
        render_output(answer)