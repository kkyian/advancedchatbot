import pytest
from advancedchatbot import ChatbotCore

@pytest.mark.emotion
def test_happy_emotion(tmp_path, monkeypatch):
    # work within a temporary directory to avoid polluting real memory files
    monkeypatch.chdir(tmp_path)
    bot = ChatbotCore()
    bot.chat(["I am happy"])
    assert bot.memory["mood"] == "happy"

