import os
import re
from typing import List

def clean_text(text: str) -> str:
    text = text.replace('\n',' ').strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def chunk_text(text: str, chunk_size_words: int = 500) -> List[str]:
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size_words):
        chunks.append(' '.join(words[i:i+chunk_size_words]))
    return chunks

if __name__ == '__main__':
    s = "This is a test. " * 200
    print(len(chunk_text(clean_text(s))))
