# Legal Assistant Bot - Project Skeleton
Minimal project skeleton for a fine-tuned LLM served via FastAPI with a Streamlit UI.

## Quick start (development)
1. Create a virtualenv and install requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Set OPENAI_API_KEY if using OpenAI models (optional for dev).
3. Run FastAPI backend:
   ```bash
   uvicorn src.api:app --reload --port 8000
   ```
4. Run Streamlit UI:
   ```bash
   streamlit run src/ui.py
   ```

This skeleton includes placeholder scripts for fine-tuning and inference.
Replace model paths and keys with real values before production.
