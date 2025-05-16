import tkinter as tk
from tkinter import scrolledtext
from advancedchatbot.chatbot_core import ChatbotCore

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Chatbot")
        self.bot = ChatbotCore()

        # Chat display
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=70, height=20)
        self.chat_display.pack(padx=10, pady=10)

        # User input
        self.entry = tk.Entry(root, width=60)
        self.entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
        self.entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return

        self.display_message("You", user_input)
        self.entry.delete(0, tk.END)

        bot_responses = self.bot.chat([user_input])
        for reply in bot_responses:
            self.display_message("Bot", reply)

    def display_message(self, sender, message):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.configure(state='disabled')
        self.chat_display.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()
