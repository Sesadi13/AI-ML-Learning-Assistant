import ollama
from prompts import explain_prompt, quiz_prompt, code_explain_prompt

print("🤖 AI/ML Learning Assistant")
print("Commands:")
print("  /explain <topic>  - Explain an AI/ML topic")
print("  /quiz <topic>     - Create a quiz")
print("  /code             - Explain Python code")
print("  /clear            - Clear conversation")
print("  exit              - Exit chatbot\n")

conversation = [
    {
        "role": "system",
        "content": """
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
    }
]

while True:

    user_message = input("You: ")

    if not user_message.strip():
        print("AI: Please enter a message.\n")
        continue

    if user_message.lower() == "exit":
        print("Goodbye!")
        break

    if user_message.lower() == "/clear":
        conversation = [conversation[0]]
        print("AI: Conversation cleared.\n")
        continue
    
    if user_message.lower().startswith("/explain "):
        topic = user_message[9:].strip()

        if not topic:
            print("AI: Please provide a topic.")
            continue

        prompt = explain_prompt(topic)

    elif user_message.lower().startswith("/quiz "):
        topic = user_message[6:].strip()

        if not topic:
            print("AI: Please provide a topic.")
            continue

        prompt = quiz_prompt(topic)

    elif user_message.lower() == "/code":
        print("\nPaste your code below.")
        print("Type END on a new line when finished.\n")

        code_lines = []

        while True:
           line = input()

           if line == "END":
            break

           code_lines.append(line)

        code = "\n".join(code_lines)

        if not code.strip():
           print("AI: No code was provided.\n")
           continue

        prompt = code_explain_prompt(code)
    
    else:
        prompt = user_message

    conversation.append({
        "role": "user",
        "content": prompt
    })

    try:
        response = ollama.chat(
            model="llama3.2:3b",
            messages=conversation
        )

        ai_message = response["message"]["content"]

    except Exception as e:
        print("\n⚠️ Error: Could not connect to Ollama.")
        print("Please make sure Ollama is running.\n")
        continue

    conversation.append({
        "role": "assistant",
        "content": ai_message
    })

    print("\nAI:", ai_message)
    print()