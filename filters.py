def legal_safety_filter(text: str) -> str:
    # Basic filter - extend with real checks
    banned = ['do illegal things']
    for b in banned:
        text = text.replace(b, '[REDACTED]')
    return text
