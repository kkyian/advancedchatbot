import json
import os
from .chatbot_brain import ChatbotBrain

class ChatbotCore:
    def __init__(self):
        self.memory = {"topics": [], "mood": "neutral", "history": []}
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
        greetings = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon"]
        farewells = ["bye", "goodbye", "see you", "farewell", "later", "see ya"]
        well_being = ["how are you", "how's it going", "what's up", "how do you feel", "are you okay"]
        thanks = ["thank you", "thanks", "thx", "much appreciated"]
        help = ["help", "support", "assist", "need help"]
        affirmation = ["ok", "okay", "alright", "fine", "sure"]

        if any(greet in text for greet in greetings):
            return "greeting", None
        if any(farewell in text for farewell in farewells):
            return "farewell", None
        if any(phrase in text for phrase in well_being):
            return "well_being", None
        if any(phrase in text for phrase in thanks):
            return "thanks", None
        if any(phrase in text for phrase in help):
            return "help", None
        if any(phrase in text for phrase in affirmation):
            return "affirmation", None

        topic = self.brain.get_semantic_topic(text)
        if topic:
            return "topic_query", topic

        return "unknown", None

    def chat(self, user_input):
        cleaned = self.preprocess(user_input)
        intent, data = self.detect_intent(cleaned)
        self.memory["history"].append(user_input)

        if intent == "greeting":
            response = "Hello there! How can I help you with Python today?"
        elif intent == "farewell":
            response = "Goodbye! Come back anytime you need help."
        elif intent == "well_being":
            response = "I'm just a bunch of Python code, but I'm running smoothly! How about you?"
        elif intent == "thanks":
            response = "You're welcome! Let me know if you have any other questions."
        elif intent == "help":
            response = "I'm here to assist! Ask me anything Python-related."
        elif intent == "affirmation":
            response = "Great! Let's continue."
        elif intent == "topic_query":
            self.memory["topics"].append(data)
            response = self.brain.generate_response(data)
        else:
            response = "I'm not sure how to help with that, but I'm learning!"

        self.save_memory()
        return response
