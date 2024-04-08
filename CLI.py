from RockPaperScissor import RockPaperScissorsLizardSpock

class CLIInterface(RockPaperScissorsLizardSpock):
    def get_user_choice(self):
        choices = {
            1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock", 6: "Help", 7: "Quit"
        }
        while True:
            # choice = input(f"Your Choice: ? (Rock[1]{' ':^2}Paper[2]{' ':^2}Scissor[3]{' ':^2}Lizard[4]{' ':^2}Spock[5]{' ':^2}Help[6]{' ':^2}Quit[7])\n")
            choice = input(f"Your Choice: ? {'    '.join([f'{v}[{k}]' for k, v in choices.items()])}\n")
            if choice.isdigit() and int(choice) in choices:
                choice = int(choice)
                if choice == 7:
                    return None
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