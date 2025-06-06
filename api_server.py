from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from advancedchatbot.chatbot_core import ChatbotCore

app = FastAPI()
bot = ChatbotCore()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins — or restrict to your domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    responses = bot.chat([req.message])
    return {"reply": responses[0]}

@app.get("/")
async def root():
    return {"message": "AdvancedChatbot API is running"}
