from chatbot_core import ChatbotCore

if __name__ == "__main__":
    bot = ChatbotCore()
    print("AdvancedChatbot: Hello! (Type 'quit' to exit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("AdvancedChatbot: Goodbye!")
            break

        responses = bot.chat([user_input])
        for line in responses:
            print(line)
