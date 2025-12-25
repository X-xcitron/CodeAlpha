import tkinter as tk
from tkinter import scrolledtext
import datetime
import random

RULES = {
    "hello": ["Hello! How can I help you today?",
              "Hi there! What do you want to talk about?"],
    "how are you": ["I'm running in Python, so always good!",
                    "All systems operational. How are you?"],
    "name": ["I'm PyBot with a Tkinter GUI.", "You can call me PyBot."],
    "time": [],  # dynamic
    "date": [],  # dynamic
    "joke": ["Why do programmers prefer dark mode? Because light attracts bugs.",
             "There are 10 types of people: those who understand binary and those who don't."],
    "bye": ["Goodbye! Have a nice day.", "See you later, keep coding!"]
}

def get_response(user_msg: str) -> str:
    msg = user_msg.lower().strip()

    if "time" in msg:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {now}."
    if "date" in msg or "today" in msg:
        today = datetime.date.today().strftime("%Y-%m-%d")
        return f"Today's date is {today}."

    for key, responses in RULES.items():
        if key in msg and responses:
            return random.choice(responses)

    return "I didn't understand that. Try asking about time, date, joke, or say hello."

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rule-Based Chatbot")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state="disabled")
        self.chat_area.pack(padx=10, pady=10)

        bottom_frame = tk.Frame(root)
        bottom_frame.pack(padx=10, pady=5, fill="x")

        self.entry = tk.Entry(bottom_frame, width=50)
        self.entry.pack(side=tk.LEFT, padx=(0, 5), fill="x", expand=True)
        self.entry.bind("<Return>", lambda event: self.send_message())

        self.send_button = tk.Button(bottom_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT)

        self._insert_bot("Hello! I'm PyBot. Type something and press Enter.")

    def _insert_bot(self, text: str):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, f"Bot: {text}\n")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)

    def _insert_user(self, text: str):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, f"You: {text}\n")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)

    def send_message(self):
        user_text = self.entry.get().strip()
        if not user_text:
            return
        self.entry.delete(0, tk.END)

        self._insert_user(user_text)
        response = get_response(user_text)
        self._insert_bot(response)

        if "bye" in user_text.lower():
            self.entry.config(state="disabled")
            self.send_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()
