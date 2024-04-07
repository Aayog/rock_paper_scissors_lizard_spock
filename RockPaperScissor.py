import random

class RockPaperScissorsLizardSpock:
    def __init__(self):
        self.options = ["Rock", "Spock", "Paper", "Lizard", "Scissors"]
        self.messages = [
            "Scissors cuts Paper", "Paper covers Rock",
            "Rock crushes Lizard", "Lizard poisons Spock",
            "Spock smashes Scissors", "Scissors decapitates Lizard",
            "Lizard eats Paper", "Paper disproves Spock",
            "Spock vaporizes Rock", "Rock crushes Scissors"
        ]

    def get_user_choice(self):
        raise NotImplementedError("get_user_choice method must be implemented in a subclass")

    def get_computer_choice(self):
        return random.randrange(0, 5)

    def determine_winner(self, user_choice, computer_choice):
        difference = (computer_choice - user_choice) % 5
        if difference == 0:
            return "Draw", "No one wins!"
        for message in self.messages:
            if self.options[user_choice] in message and self.options[computer_choice] in message:
                if difference == 1 or difference == 2:
                    return "Computer", message
                else:
                    return "User", message

class CLIInterface(RockPaperScissorsLizardSpock):
    def get_user_choice(self):
        choices = {
            1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock", 6: "Help"
        }
        while True:
            choice = input("Your Choice: ? (Rock[1]/Paper[2]/Scissor[3]/Lizard[4]/Spock[5]/Help[6])\n")
            if choice.isdigit() and int(choice) in choices:
                choice = int(choice)
                if choice == 6:
                    self.display_help()
                else:
                    return choice - 1
            else:
                print("Invalid choice. Please try again.")

    def display_help(self):
        help_msg = "\n\n\t\t\t INSTRUCTIONS !! \n\n" + "\n".join(self.messages) + "\n \n "
        print(help_msg)

    def play(self):
        print("Rock, Paper, Scissors, Lizard, Spock is a variation of normal Rock, Paper, Scissors.")
        while True:
            user_choice = self.get_user_choice()
            if user_choice is None:
                break
            computer_choice = self.get_computer_choice()
            result, message = self.determine_winner(user_choice, computer_choice)
            print(f"Your choice is {self.options[user_choice]}")
            print(f"Computer's choice is {self.options[computer_choice]}")
            if result == "Draw":
                print("Draw!")
            else:
                print(f"{result} wins! {message}")