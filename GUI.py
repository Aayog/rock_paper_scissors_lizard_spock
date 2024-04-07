
from tkinter import messagebox
import tkinter as tk

from RockPaperScissor import RockPaperScissorsLizardSpock

class GUIInterface(RockPaperScissorsLizardSpock):
    def __init__(self, master):
        super().__init__()
        self.master = master
        master.title("Rock, Paper, Scissors, Lizard, Spock")

        self.user_choice = tk.StringVar()
        self.user_choice.set("Choose your option")

        options_menu = tk.OptionMenu(master, self.user_choice, *self.options)
        options_menu.pack()

        play_button = tk.Button(master, text="Play", command=self.play_game)
        play_button.pack()

    def get_user_choice(self):
        choice = self.user_choice.get()
        if choice in self.options:
            return self.options.index(choice)
        else:
            return None

    def play_game(self):
        user_choice = self.get_user_choice()
        if user_choice is not None:
            computer_choice = self.get_computer_choice()
            result, message = self.determine_winner(user_choice, computer_choice)
            result_msg = f"Your choice: {self.options[user_choice]}\n"
            result_msg += f"Computer's choice: {self.options[computer_choice]}\n"
            if result == "Draw":
                result_msg += "It's a Draw!"
            else:
                result_msg += f"{result} wins! {message}"
            messagebox.showinfo("Result", result_msg)

root = tk.Tk()
gui_game = GUIInterface(root)
root.mainloop()
