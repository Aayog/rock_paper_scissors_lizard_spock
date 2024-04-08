import sys
from CLI import CLIInterface
from GUI import GUIInterface


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "cli":
            cli_game = CLIInterface()
            cli_game.play()
        elif sys.argv[1] == "gui":
            gui_game = GUIInterface()
            gui_game.play()
        else:
            print("Usage: python main.py [cli|gui]")
            sys.exit(1)
    else:
        print("Usage: python main.py [cli|gui]")
        sys.exit(1)