from .chatbot_core import ChatbotCore

def run_chat_session():
    bot = ChatbotCore()
    print("LLMChatbot: Hello! Ask me something about Python. (Type 'quit' to exit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("LLMChatbot: Goodbye!")
            bot.save_memory()
            break

        response = bot.chat(user_input)
        print(f"LLMChatbot: {response}")

        bot.save_memory()

run_chat_session()
