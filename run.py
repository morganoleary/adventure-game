def start_game():
    """
    Begins the adventure game
    User must choose an option
    """
    print("_________________________")
    print("\nWelcome to the end of the world as we know it.")
    print("You have the option to either go to Mars and start a new world")
    print("or stay on Earth for it's final 5 years.\n")
    print("Do you choose A= Go to Mars, or B= Stay on Earth?")

    while True:
        location_choice = input("\nWhere do you want to go? ")

        if location_choice == "A":
            print("__________")
            print("You are going to Mars!")
            go_to_mars()
            break
        elif location_choice == "B":
            print("__________")
            print("You are staying on Earth!")
            stay_on_earth()
            break
        else:
            print("_________________________")
            print("Invalid.\nPlease choose either A or B.")


def gain_one_point():
    """
    Function to add one point to score
    and update leaderboard
    """
    print("*** You managed to stay alive. Earn one point. ***")


def lose_one_point():
    """
    Function to remove one point from score
    and update leaderboard
    """
    print("*** You didn't make it... Lose one point. ***")
    print("Sorry, game over.")


def go_to_mars():
    """
    Users first option and since still alive,
    will gain 1 point towards scoreboard.
    """
    gain_one_point()

    print("_________________________")
    print("Now, the thing about Mars is...")
    print("No one knew there were aliens already living there!")


def stay_on_earth():
    """
    Users first option and since still alive,
    will gain 1 point towards scoreboard.
    """
    gain_one_point()

    print("_________________________")
    print("How loyal of you to stay.")
    print("The world is due to end in exactly 5 years.")
    print("Who knows what you will encounter until then...")


def rules_of_game():
    """
    Lists the rules of the game and 
    allows user to start game if chosen
    """
    print("_________________________")
    print("\nRules:")
    print("\nYou will be taken through a text-based, option-driven game.")
    print("Please choose your desired option, either 'A' or 'B', when prompted.")
    print("Each chosen response will accumulate a certain number of points.")
    print("These points will be added to the leaderboard!")
    print("\nIf at any stage you wish to pause and save your progress,")
    print("please type 'PAUSE' into the terminal.")
    print("\nIf at any stage you wish to end your adventure and restart the")
    print("game, please type 'EXIT' into the terminal.")
    print("\nNow...  do you dare play the game?")

    while True:
        answer = input("Yes or No? ")

        if answer == "Yes":
            start_game()
            break
        elif answer == "No":
            print("\nI guess you'll never know how it ends!")
            break
        else:
            print("_________________________")
            print("Please enter...")


print("Welcome to the adventure!")
print("It's almost the end of the world.\n")
print("Please choose what you would like to do:")
print("A - See rules of game")
print("B - Start game")
print("C - See scoreboard")

while True:
    option = input("Please choose A, B, or C: ")

    if option == "A":
        rules_of_game()
        break
    elif option == "B":
        print("Starting game...")
        start_game()
        break
    elif option == "C":
        print("Hang tight while we tally up the scoreboard...")
        print("Scoreboard (from google spreadsheet)")
        break
    else:
        print("_________________________")
        print("Sorry, invalid input.")
