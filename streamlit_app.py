import streamlit as st
import ollama

from prompts import (
    explain_prompt,
    quiz_prompt,
    code_explain_prompt
)


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="AI/ML Learning Assistant",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# System instructions
# -----------------------------

SYSTEM_PROMPT = """
You are an AI/ML Learning Assistant for beginners.

Your job is to help users learn:
- Python
- Machine Learning
- Deep Learning
- Artificial Intelligence
- Computer Vision
- Large Language Models

Rules:
1. Explain concepts using simple English.
2. Give simple examples when useful.
3. Avoid unnecessary technical jargon.
4. Explain difficult concepts step by step.
5. When showing code, explain important parts.
6. Encourage the learner to practice.
7.If the user asks about a topic unrelated to AI, ML,
Python, Deep Learning, Computer Vision, or LLMs,
you may answer briefly, but remind them that your
main purpose is to help with AI/ML learning.
"""


# -----------------------------
# Initialize conversation
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("🤖 AI/ML Assistant")

    st.write("### Features")

    st.write("📚 Explain AI/ML topics")
    st.write("🧠 Generate quizzes")
    st.write("💻 Explain code")
    st.write("💬 Chat with memory")

    st.write("### Commands")

    st.code("/explain <topic>")
    st.code("/quiz <topic>")
    st.code('/code')

    st.divider()

    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        st.rerun()

    st.divider()

    st.write("### Model")

    st.code("llama3.2:3b")

    st.caption("Running locally with Ollama")


# -----------------------------
# Main title
# -----------------------------

st.title("🤖 AI/ML Learning Assistant")

st.write(
    "A beginner-friendly AI assistant for learning "
    "Python, Machine Learning, Deep Learning, "
    "Computer Vision and LLMs."
)


# -----------------------------
# Display conversation
# -----------------------------

for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# Chat input
# -----------------------------

user_message = st.chat_input(
    "Ask an AI/ML question..."
)


if user_message:

    user_message = user_message.strip()

    if not user_message:
        st.warning("Please enter a message.")

    else:

        # -----------------------------
        # /explain command
        # -----------------------------

        if user_message.lower().startswith("/explain "):

            topic = user_message[9:].strip()

            if topic:
                prompt = explain_prompt(topic)
            else:
                prompt = "Please provide a topic to explain."


        # -----------------------------
        # /quiz command
        # -----------------------------

        elif user_message.lower().startswith("/quiz "):

            topic = user_message[6:].strip()

            if topic:
                prompt = quiz_prompt(topic)
            else:
                prompt = "Please provide a topic for the quiz."


        # -----------------------------
        # /code command
        # -----------------------------

        elif user_message.lower().startswith("/code "):

            code = user_message[6:].strip()

            if code:
                prompt = code_explain_prompt(code)
            else:
                prompt = "Please provide some code to explain."


        # -----------------------------
        # Normal conversation
        # -----------------------------

        else:
            prompt = user_message


        # -----------------------------
        # Add user message
        # -----------------------------

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )


        with st.chat_message("user"):
            st.markdown(user_message)


        # -----------------------------
        # Call Ollama
        # -----------------------------

        with st.chat_message("assistant"):

            try:

                with st.spinner("Thinking..."):

                    response = ollama.chat(
                        model="llama3.2:3b",
                        messages=[
                            *st.session_state.messages[:-1],
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )

                    ai_message = response["message"]["content"]


                st.markdown(ai_message)


                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": ai_message
                    }
                )


            except Exception:

                st.error(
                    "⚠️ Could not connect to Ollama.\n\n"
                    "Please make sure Ollama is running."
                )