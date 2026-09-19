def explain_prompt(topic):
    return f"""
Explain the following topic to a beginner:

Topic: {topic}

Use this structure:

1. What is it?
2. How does it work?
3. Simple example
4. Real-world application
5. Short summary

Use simple English and avoid unnecessary technical jargon.
"""

def quiz_prompt(topic):
    return f"""
Create a beginner-level quiz about:

Topic: {topic}

Generate 5 multiple-choice questions.

For each question:
- Give 4 options: A, B, C, D.
- Clearly indicate the correct answer.
- Give a one-sentence explanation.

Use simple English.
"""

def code_explain_prompt(code):
    return f"""
You are a beginner-friendly programming tutor.

Explain the following code using simple English.

Code:
{code}

Use this structure:

1. What does this code do?
2. Explanation of each important line
3. Important concepts used
4. Example of the output
5. How could this code be improved?

Do not unnecessarily rewrite the entire code.
Keep the explanation beginner-friendly.
"""