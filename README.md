# Advanced Chatbot 🤖

This project is an advanced chatbot built entirely in Python!  
It can understand emotions, help you with coding, dream up project ideas, and even search the web when it doesn't know something.

## Features
- 🧠 **Memory** — remembers conversation moods
- 🔥 **Emotional understanding** — reacts based on how you feel
- 👨‍💻 **Code generation** — shows code examples for Python
- 🌍 **Web search engine** — finds answers online if it doesn’t know
- 🚀 **Project ideas** — suggests creative app or game ideas

## Folder Structure
advancedchatbot/ ├── chatbot_core.py ├── chatbot_brain.py ├── main.py ├── .gitignore └── README.md

## How to Run
1. Make sure you have **Python 3.8+** installed
2. Clone this repository
3. Open your terminal:
    ```bash
    cd advancedchatbot
    python -m advancedchatbot.main
    ```

## Future Ideas 💡
- Add natural language summarization
- Multi-language coding support (Python, JS, C++)
- Smarter AI memory (store facts learned during chats!)
## Api Endpoint
### `POST /chat`

Send a message to the chatbot and receive a reply.

#### Request body:
```json
{
  "message": "What is a Python list?"
}
```

Response:

```json
{
  "reply": "A Python list is a collection of ordered items..."
}
```
---

Made with ❤️ by **kkyian**  

