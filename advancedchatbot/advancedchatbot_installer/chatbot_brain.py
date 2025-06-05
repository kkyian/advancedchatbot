import random

class ChatbotBrain:
    def __init__(self):
        self.semantic_map = {
            "list": ["list", "array", "collection", "sequence"],
            "loop": ["for", "while", "repeat", "iterate"],
            "conditional": ["if", "condition", "branch", "decision"],
            "function": ["function", "method", "def", "procedure"],
            "class": ["class", "object", "blueprint"],
            "file read": ["read file", "open file", "load file"],
            "file write": ["write file", "save file", "store file"],
            "project": ["project", "app", "build", "create"],
            "emotion": ["happy", "sad", "excited", "angry", "bored"],
            "variable": ["variable", "assign", "store"],
            "dictionary": ["dictionary", "map", "hashmap"]
        }

        self.code_templates = {
            "list": {
                "py": "my_list = [1, 2, 3, 4, 5]  # This is how you define a list in Python."
            },
            "loop": {
                "py": "for i in range(5):\n    print(i)  # A simple loop example"
            },
            "conditional": {
                "py": "if x > 0:\n    print(\"Positive\")  # Conditional check"
            },
            "function": {
                "py": "def greet(name):\n    return f\"Hello, {name}!\""
            },
            "class": {
                "py": "class Dog:\n    def __init__(self, name):\n        self.name = name\n    def bark(self):\n        return \"Woof!\""
            }
        }

    def get_semantic_topic(self, text):
        text = text.lower()
        for topic, keywords in self.semantic_map.items():
            for keyword in keywords:
                if keyword in text:
                    return topic
        return None

    def get_code_template(self, topic):
        return self.code_templates.get(topic, {}).get("py", "Sorry, I don't have an example for that.")

    def generate_response(self, topic):
        responses = [
            f"You seem to be interested in {topic}. Here's a Python example:",
            f"Let's look at how {topic} works in code:",
            f"I think you're asking about {topic}. This might help:",
        ]
        intro = random.choice(responses)
        code = self.get_code_template(topic)
        return f"{intro}\n\n{code}"
