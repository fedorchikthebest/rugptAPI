from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = FastAPI()

@app.post('/question')
def generate_question(data = Body()):
    return JSONResponse(jsonable_encoder({"test": 123}))