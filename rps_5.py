#Rock, Paper, Scissors, Lizard, Spock
import random,os
def main():
    global opt,msg
    opt = ["Rock","Spock","Paper","Lizard","Scissors"]
    msg = ["\t\t\t Scissors cuts Paper","\t\t\t Paper covers Rock","\t\t\tRock crushes Lizard","\t\t\t Lizard poisons Spock","\t\t\t Spock smashes Scissors","\t\t\t Scissors decapitates Lizard","\t\t\tLizard eats Paper","\t\t\t Paper disproves Spock","\t\t\t Spock vaporizes Rock","\t\t\tRock crushes Scissors"]
    print "Rock, Paper, Scissors, Lizard, Spock is a variation of normal Rock, Paper, Scissors."
    game_help()
    while True:
        os.system('clear')
        choice = random.randrange(0,5)

        print "Type in any number you wish from 1 to 6 and any other number to exit."
        ask_user = int(raw_input("Your Choice: ? (Rock[1]/Paper[2]/Scissor[3]/Lizard[4]/Spock[5]/Help[6])\n"))
        if ask_user == 6:
            game_help()
            continue
        if ask_user < 1 or ask_user > 6:
            break
        ask_user -=1
        os.system('clear')
        print "Your choice is {} ".format(opt[ask_user])
        a = who_win(ask_user)
        if a == 0:
            print "Draw!"
        a = raw_input("Enter to continue.....")

def game_help():
    os.system('clear')
    print "\n\n\t\t\t INSTRUCTIONS !! \n\n"
    help_msg = "\n".join(msg)
    print help_msg + "\n \n "
    raw_input("Enter to continue......")


def who_win( user):
    comp_number = random.randrange(0,5)
    comp_opt = opt[comp_number]
    print "Computer's choice is {}".format(comp_opt)
    player_number = user
    mod = (comp_number-player_number) % 5
    if mod == 0:
        return 0
    for mess in msg:
        if opt[user] in mess and comp_opt in mess:
            message = mess
    print message
    if mod == 1 or mod == 2:
        print "Computer wins!"
    else:
        print "You win!"

if __name__=="__main__":
    main()
