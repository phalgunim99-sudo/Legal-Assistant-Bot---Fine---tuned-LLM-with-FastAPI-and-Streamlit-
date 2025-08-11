import os
from typing import Optional

OPENAI_KEY = os.environ.get('OPENAI_API_KEY')

def generate_answer(prompt: str, context: Optional[str] = None) -> str:
    # Simple local stub: echo prompt + context. Replace this with model inference.
    out = "Answer stub.\nPrompt:\n" + prompt
    if context:
        out += "\nContext:\n" + context
    return out

if __name__ == '__main__':
    print(generate_answer("What is the speed limit in Germany?", "Traffic laws section..."))
