# Write your code to expect a terminal of 80 characters wide and 24 rows high

def start_game():
    """
    Begins the adventure game
    """
    print("\nWelcome to the end of the world as we know it.")
    print("You have the option to either go to Mars and start a new world\n")
    print("or stay on Earth for it's final 5 years.")
    print("Do you choose A= Go to Mars or B= Stay on Earth?")

    while True:
        location_choice = input("\nWhere do you want to go? ")

        if (location_choice == "A"):
            print("You are going to Mars!")
            break
        elif (location_choice == "B"):
            print("You are staying on Earth!")
            break
        else:
            print("Please choose either A or B.")


def rules_of_game():
    """
    Lists the rules of the game and 
    allows user to start game if chosen
    """

    print("\nRules:")
    print("\nYou will be taken through a text-based, option-driven game.")
    print("Please choose your desired option, either 'A' or 'B' when prompted.")
    print("Each chosen response will accumulate a certain number of points.")
    print("These points will be added to the leaderboard!")
    print("\nIf at any stage you wish to pause and save your progress,")
    print("please type 'PAUSE' into the terminal.")
    print("\nIf at any stage you wish to end your adventure and restart the")
    print("game, please type 'EXIT' into the terminal.")
    print("\nNow... would you like to play the game?")
    answer = input("Yes or No? ")

    if answer == "Yes":
        start_game()
    elif answer == "No":
        print("I guess you'll never know how it ends!")
    else:
        print("Please enter 'Yes' or 'No'.")


print("Welcome to the adventure!\n")
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
        print("Hang tight... we're getting the scoreboard!")
        print("Scoreboard (from google spreadsheet)")
        break
    else:
        print("Please choose A, B or C.")

