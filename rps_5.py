#Rock, Paper, Scissors, Lizard, Spock
import random,os
def main():
    global opt,msg
    opt = ["Rock","Paper","Scissors","Lizard","Spock"]
    msg = ["\t\t\t Scissors cuts Paper","\t\t\t Paper covers Rock","\t\t\tRock crushes Lizard","\t\t\t Lizard poisons Spock","\t\t\t Spock smashes Scissors","\t\t\t Scissors decapitates Lizard","\t\t\tLizard eats Paper","\t\t\t Paper disproves Spock","\t\t\t Spock vaporizes Rock","\t\t\tRock crushes Scissors"]
    print "Rock, Paper, Scissors, Lizard, Spock is a variation of normal Rock, Paper, Scissors."
    game_help()
    while True:
        os.system('clear')
        choice = random.randrange(0,5)
        comp_opt = opt[choice]
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
        print "Computer's choice is {}".format(comp_opt)
        print who_win(comp_opt,ask_user)
        a = raw_input("Enter to continue.....")

def game_help():
    print "\n\n\t\t\t INSTRUCTIONS !! \n\n"
    help_msg = "\n".join(msg)
    print help_msg + "\n \n "
    raw_input("Enter to continue......")


def who_win(comp, user):
    flag = 0
    if comp == opt[user]:
        return "Draw!! "
    for mess in msg:
        if opt[user] in mess and comp in mess:
            message = mess
    print message
    user +=1
    if user == 1:
        if comp == opt[2] or comp == opt[3]:
            flag = 1
    if user == 2:
        if comp == opt[4] or comp == opt[0]:
            flag = 1
    if user == 3:
        if comp == opt[3] or comp == opt[1]:
            flag = 1
    if user== 4:
        if comp == opt[4] or comp == opt[1]:
            flag = 1
    if user == 5:
        if comp == opt[0] or comp == opt[2]:
            flag = 1
    if flag == 1:
        return "You win!! \n"
    else:
        return "Computer Wins!"
    a = raw_input("Enter to continue.....")

if __name__=="__main__":
    main()
