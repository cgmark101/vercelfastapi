from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello my friend"}