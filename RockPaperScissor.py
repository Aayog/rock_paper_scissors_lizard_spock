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