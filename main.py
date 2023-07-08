from typing import Annotated
from fastapi import FastAPI, Request,Form
from utilis import send_message
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()


@app.post("/message")
async def message(request: Request):
    try:
        form_data = await request.json()
        m = form_data["text"]
        z = f"{m}dddd"
        send_message(z)
    except Exception as e:
        print("ddfd")

    return ""
