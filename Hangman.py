import random
import tkinter as tk
from tkinter import messagebox

WORDS = ["python", "java", "kotlin", "hangman", "developer",
         "function", "variable", "loop", "condition", "iterator"]
MAX_WRONG = 6

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman - Tkinter Version")

        self.secret_word = ""
        self.guessed_letters = set()
        self.wrong_guesses = 0

        # Widgets
        self.word_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=10)

        self.info_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.info_label.pack(pady=5)

        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="Enter a letter:").grid(row=0, column=0)
        self.entry = tk.Entry(frame, width=5, font=("Helvetica", 16))
        self.entry.grid(row=0, column=1)
        self.entry.bind("<Return>", lambda event: self.check_guess())

        self.guess_button = tk.Button(frame, text="Guess", command=self.check_guess)
        self.guess_button.grid(row=0, column=2, padx=5)

        self.new_button = tk.Button(root, text="New Game", command=self.new_game)
        self.new_button.pack(pady=5)

        self.status_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.status_label.pack(pady=5)

        self.new_game()

    def new_game(self):
        self.secret_word = random.choice(WORDS)
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.update_display()
        self.status_label.config(text="")
        self.entry.config(state="normal")
        self.guess_button.config(state="normal")

    def display_word(self):
        return " ".join(ch if ch in self.guessed_letters else "_" for ch in self.secret_word)

    def update_display(self):
        self.word_label.config(text=self.display_word())
        guessed = " ".join(sorted(self.guessed_letters)) or "None"
        info = f"Guessed: {guessed} | Wrong: {self.wrong_guesses}/{MAX_WRONG}"
        self.info_label.config(text=info)

    def check_guess(self):
        guess = self.entry.get().lower().strip()
        self.entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showinfo("Invalid", "Please enter a single letter.")
            return
        if guess in self.guessed_letters:
            messagebox.showinfo("Duplicate", "You already guessed that letter.")
            return

        self.guessed_letters.add(guess)
        if guess not in self.secret_word:
            self.wrong_guesses += 1

        self.update_display()
        self.check_game_over()

    def check_game_over(self):
        if all(ch in self.guessed_letters for ch in self.secret_word):
            self.status_label.config(text="You won! Click 'New Game' to play again.")
            self.entry.config(state="disabled")
            self.guess_button.config(state="disabled")
        elif self.wrong_guesses >= MAX_WRONG:
            self.status_label.config(text=f"You lost! Word was '{self.secret_word}'.")
            self.entry.config(state="disabled")
            self.guess_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
