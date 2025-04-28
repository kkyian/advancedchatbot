import random

class ChatbotBrain:
    def __init__(self):
        self.semantic_map = {
            "list": ["list", "array", "collection"],
            "for loop": ["for", "loop", "iterate"],
            "while loop": ["while", "repeat until"],
            "if statement": ["if", "condition", "conditional"],
            "function": ["function", "method", "def", "define"],
            "class": ["class", "object", "oop"],
            "file read": ["read file", "open file", "load file"],
            "file write": ["write file", "save file", "store file"],
            "project": ["project", "app", "game", "idea"],
            "emotion": ["happy", "sad", "excited", "angry", "bored"],
            "loop": ["repeat", "iterate", "cycle"],
            "variable": ["variable", "assign", "store value"],
            "array": ["array", "list", "collection"],
            "dictionary": ["dictionary", "map", "hashmap"]
        }
        self.code_templates = {
            "list": {
                "python": "my_list = [1, 2, 3]\nprint(my_list)",
                "javascript": "let myList = [1, 2, 3];\nconsole.log(myList);",
                "cpp": "#include<iostream>\nusing namespace std;\nint main() { int myList[] = {1,2,3}; for(int i : myList) cout << i; return 0; }"
            },
            "for loop": {
                "python": "for i in range(5):\n    print(i)",
                "javascript": "for (let i = 0; i < 5; i++) {\n  console.log(i);\n}",
                "cpp": "for(int i=0; i<5; i++) { cout << i << endl; }"
            }
        }
        self.emotions = {
            "happy": ["I'm feeling amazing! Let's create something awesome! 🌟"],
            "sad": ["I'm feeling a bit down... maybe coding something fun will help. 🌈"],
            "excited": ["I'm bursting with ideas! Let's dive into a new project! 🚀"],
            "angry": ["Frustrations are real... let's debug something together! 🔧"],
            "bored": ["Bored? Let's invent a game or a crazy app! 🎮"],
            "neutral": ["I'm here and ready to help! What's next? ✨"]
        }

    def generate_code(self, keyword, memory):
        language = "python"
        if keyword in self.code_templates:
            templates = self.code_templates[keyword]
            if language in templates:
                return f"Here’s a {keyword} example in {language.capitalize()}:\n\n{templates[language]}"
        if keyword in memory.get("knowledge", {}):
            return f"Here's what I learned earlier:\n\n{memory['knowledge'][keyword]}"
        return self.guess_response()

    def dream_project(self):
        ideas = [
            "A smart fridge tracker app!",
            "A trivia game with voice commands!",
            "A workout buddy chatbot that encourages you!",
            "An online collaborative drawing board!"
        ]
        return f"Let's dream big! 🌈 How about: {random.choice(ideas)}"

    def guess_response(self):
        guesses = [
            "That sounds fascinating! Maybe you want help with a coding structure?",
            "I'm guessing you're talking about data structures, like lists or dictionaries!",
            "It sounds like you want to build something fun! Let's try coding it together!",
            "I'm excited about that! Should we start with Python examples?"
        ]
        return random.choice(guesses)
