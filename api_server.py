from fastapi import FastAPI, Request
from pydantic import BaseModel
from advancedchatbot.chatbot_core import ChatbotCore

app = FastAPI()
bot = ChatbotCore()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    responses = bot.chat([req.message])
    return {"reply": responses[0]}

@app.get("/")
async def root():
    return {"message": "AdvancedChatbot API is running"}
