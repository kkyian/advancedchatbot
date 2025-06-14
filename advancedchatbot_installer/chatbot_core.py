import random
import json
import os
import urllib.request
from chatbot_brain import ChatbotBrain

class ChatbotCore:
    def __init__(self):
        self.memory = {"topics": [], "mood": "neutral", "knowledge": {}}
        self.brain = ChatbotBrain()
        self.load_memory()

    def preprocess(self, text):
        return text.lower().strip()

    def load_memory(self):
        if os.path.exists("chatbot_memory.json"):
            with open("chatbot_memory.json", "r") as file:
                self.memory = json.load(file)

    def save_memory(self):
        with open("chatbot_memory.json", "w") as file:
            json.dump(self.memory, file)

    def detect_intent(self, text):
        greetings = ["hello", "hi", "hey", "greetings"]
        farewells = ["bye", "goodbye", "see you", "farewell"]

        if any(greet in text for greet in greetings):
            return "greeting", None
        if any(farewell in text for farewell in farewells):
            return "farewell", None

        for concept, keywords in self.brain.semantic_map.items():
            if any(word in text for word in keywords):
                if concept == "emotion":
                    for kw in keywords:
                        if kw in text:
                            return "emotion", kw
                else:
                    return "code", concept

        if "project" in text or "idea" in text:
            return "project", None

        return "search", text

    def update_emotion(self, emotion_word):
        if emotion_word in self.brain.emotions:
            self.memory["mood"] = emotion_word
            self.save_memory()

    def browse_web(self, query):
        try:
            url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')

            start = html.find('result__a')
            if start != -1:
                link_start = html.find('href="', start) + 6
                link_end = html.find('"', link_start)
                link = html[link_start:link_end]

                if link.startswith("//"):
                    full_link = "https:" + link
                elif link.startswith("/"):
                    full_link = "https://duckduckgo.com" + link
                else:
                    full_link = link

                return f"I found something! Here is a good link: {full_link}"
            else:
                return f"I searched but couldn't find a direct link. Try here: https://duckduckgo.com/?q={query.replace(' ', '+')}"
        except Exception as e:
            return f"Browsing error: {str(e)}"

    def generate_response(self, intent, keyword=None):
        mood = self.memory.get("mood", "neutral")
        if intent == "greeting":
            return random.choice(self.brain.emotions[mood])
        if intent == "farewell":
            return "Goodbye! Stay awesome! 🌟"
        if intent == "code" and keyword:
            return self.brain.generate_code(keyword, self.memory)
        if intent == "project":
            return self.brain.dream_project()
        if intent == "emotion":
            self.update_emotion(keyword if keyword else "")
            return random.choice(self.brain.emotions[self.memory.get("mood", "neutral")])
        if intent == "search" and keyword:
            return self.browse_web(keyword)
        return self.brain.guess_response()

    def learn(self, topic, example):
        self.memory.setdefault("knowledge", {})
        self.memory["knowledge"][topic] = example
        self.save_memory()

    def chat(self, conversation_inputs):
        responses = []
        for user_input in conversation_inputs:
            processed = self.preprocess(user_input)
            intent, keyword = self.detect_intent(processed)
            reply = self.generate_response(intent, keyword)
            responses.append(f"AdvancedChatbot [{self.memory.get('mood', 'neutral')}]: {reply}")
        return responses
