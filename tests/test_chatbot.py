import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from advancedchatbot.chatbot_core import ChatbotCore

def test_greeting(tmp_path, monkeypatch):
    # use tmp dir for memory file
    memory_file = tmp_path/'chatbot_memory.json'
    monkeypatch.chdir(tmp_path)

    bot = ChatbotCore()
    # ensure memory file is created on chat
    response = bot.chat('hello')
    assert 'Hello' in response
    assert memory_file.exists()
