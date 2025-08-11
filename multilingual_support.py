# Placeholder: integrate libraries like langdetect and googletrans or transformers for translation
def detect_language(text: str) -> str:
    # naive
    if any(ord(c) > 128 for c in text):
        return 'non-ascii'
    return 'en'
