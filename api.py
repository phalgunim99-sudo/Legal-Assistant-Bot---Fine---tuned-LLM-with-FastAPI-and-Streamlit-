from fastapi import FastAPI
from pydantic import BaseModel
from .inference import generate_answer
from .filters import legal_safety_filter

app = FastAPI(title='Legal Assistant Bot')

class Query(BaseModel):
    question: str
    context: str = ''

@app.post('/query')
async def query(q: Query):
    ans = generate_answer(q.question, q.context or None)
    ans = legal_safety_filter(ans)
    return {'answer': ans}
