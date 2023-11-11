import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('adventure_scoreboard')

scores = SHEET.worksheet('scoreboard')

data = scores.get_all_values()

print(data)

def start_game():
    """
    Begins the adventure game
    User must choose an option
    """
    print("_________________________")
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
            print("Earth it is!")
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
    print("_________________________")
    print("*** You managed to stay alive. Earn one point. ***")
    print("_________________________")


def lose_one_point():
    """
    Function to remove one point from score
    and update leaderboard. Game is over.
    """
    print("_________________________")
    print("*** You didn't make it... Lose one point. ***")
    print("_________________________")
    print("Sorry, game over.")


def go_to_mars():
    """
    Users first option and since still alive,
    will gain 1 point towards scoreboard.
    """
    gain_one_point()

    print("_________________________")
    print("\nNow, the thing about Mars is...")
    print("No one knew there were already aliens living there!")
    print("\n... The next day you are packed onto a space shuttle")
    print("and become one of the first people to land on Mars.")
    print("_________________________")
    print("\nThe air is cold and damp and it's so dark you can barely")
    print("make out shadows in the distance. There are strange, long")
    print("creatures coming towards you at an alarming speed!\n")
    print("You have one chance to change your mind.")
    print("Do you A= Stay and wait to see what happens, or ")
    print("B= Sneak back on the space shuttle and go back to Earth?")
    
    while True:
        decision_one = input("What do you want to do? ")
        
        if decision_one == "A":
            print("\nOh, how brave of you...")
            stay_on_mars()
            break
        elif decision_one == "B":
            print("\nEarth couldn't have gotten worse... could it?")
            stay_on_earth()
            break
        else:
            print("_________________________")
            print("Invalid.\nPlease choose either A or B.")


def stay_on_earth():
    """
    Users first option and since still alive,
    will gain 1 point towards scoreboard.
    """
    gain_one_point()

    print("_________________________")
    print("\nSo glad you chose Earth! Who knows WHAT's on Mars!")
    print("The world is due to end in exactly 5 years.")
    print("Who knows what you will encounter until then...")
    print("_________________________")
    print("Things have taken a turn for the worse and natural disasters")
    print("are hitting every continent at once!")
    print("Will you be able to survive Earth's final years if it's THIS bad?")
    print("\nThere is an underground bunker that was created to offer more")
    print("peace for the final days...")
    print("Do you A= Move to the underground bunker or B= Try to survive")
    print("in the wild?")

    survival_location = input("Which do you choose? A or B? ")

    while True:
        if survival_location == "A":
            print("\nIt was a trap! The bunker explodes.")
            lose_one_point()
            break
        elif survival_location == "B":
            print("\nThe whole bunker just exploded!")
            print("Whew! Good thing you chose to stay in the wild!")
            stay_in_wild()
            break
        else:
            print("_________________________")
            print("Invalid.\nPlease choose either A or B.")


def stay_in_wild():
    """
    Function called when user decides to stay in the wild,
    will gain 1 point towards scoreboard.
    """
    gain_one_point()

    print("_________________________")
    print("\nThe government has seized all properties still standing and")
    print("you are thrown into the streets, literally into the wild!")
    print("_________________________")
    print("Uh oh, a virus has spread and everyone is turning into zombies!")
    print("They are coming from all angles! You have two choices...")
    print("\nA= Let them attack and become a zombie, or B= Choose a")
    print("weapon and fight! Better choose quickly!")

    zombie_choice = input("A or B? ")

    while True:
        if zombie_choice == "A":
            print("\nAll zombies have been wiped out by the A-Team!")
            lose_one_point()
            break
        elif zombie_choice == "B":
            print("\nThe zombies were wiped out! But now there are more")
            print("coming... Time to choose your weapon.")
            zombie_weapon_choice()
            break
        else:
            print("_________________________")
            print("Invalid.\nPlease choose either A or B.")


def zombie_weapon_choice():
    """
    Function called when user chooses a weapon against the zombies,
    will gain 1 point towards scoreboard.
    """
    print("_________________________")
    print("\nZombies are close and you are unarmed!")
    print("You manage to make it to the nearest weapons.")
    print("_________________________")
    print("Upon entering the large warehouse built for just this scenario,")
    print("you see magical cloaks to your left, cloaks of invisibility.")
    print("To your right is a huge truck FULL of guns! The whole truck could")
    print("be yours! Do you want A= the Cloak of invisibility, or B= the ")
    print("entire truck filled with guns?")

    truck_or_cloak = input("Which do you choose? A or B? ")

    while True:
        if truck_or_cloak == "A":
            print("\nGood choice! The government just seized all ammunition!")
            print("The truck would have been no use.")
            cloak_weapon()
            break
        elif truck_or_cloak == "B":
            print("\nAll ammunition was seized by the government and you are")
            print("left with nothing. Zombies attack and you die.")
            lose_one_point()
            break
        else:
            print("_________________________")
            print("Invalid.\nPlease choose either A or B.")


def cloak_weapon():
    """
    Function called when user chooses the cloak against the zombies,
    will gain 1 point towards scoreboard.
    """
    gain_one_point()

    print("_________________________")
    print("\nYou managed to get away from the hoards of zombies, thanks to being")
    print("invisible! As you take in your surroundings, from the safety of")
    print("your cloak, you see buildings on fire, sinkholes swallowing up cars,")
    print("people and everything in site. As you were searching through that")
    print("warehouse, you overheard others talking about seeking refuge at ")
    print("the capital building... You have to try to make it there, as it")
    print("may be your last chance for survival. The only problem is, this")
    print("cloak is just so suffocating!")
    print("_________________________")
    print("Do you A= Keep the cloak on, or B= Take the cloak off?")
    
    final_earth_decision = input("Which do you choose? A or B? ")
    
    while True:
        if final_earth_decision == "A":
            print("\nYou managed to make it to the capital building alive!")
            #end game -- win!
            break
        elif final_earth_decision == "B":
            print("\nTurns out you weren't completely alone...")
            print("A group of zombies spot and kill you.")
            lose_one_point()
            break
        else:
            print("_________________________")
            print("Invalid.\nPlease choose either A or B.")


def stay_on_mars():
    """
    Function called when user decides to stay on Mars, 
    will gain 1 point towards scoreboard.
    """
    gain_one_point()

    print("_________________________")
    print("\nWell then... here goes nothing!\n")
    print("Rumour has it.. there is a safe, uninhabited part of Mars!")
    print("The best chance you have is to find the secret passage there, and")
    print("quickly, before the aliens catch you!")
    print("_________________________")
    print("The aliens are getting closer...")
    print("You turn to run the opposite direction and trip over")
    print("a bright, shiny gold box!\n")
    print("Could this be a clue to the secret passage???")
    print("This is tempting... What will you do?")

    gold_box = input("A= Open box, or B= Keep moving? ")

    while True:
        if gold_box == "A":
            print("\nOh no! It was a trap! The box exploded and you die.")
            lose_one_point()
            break
        elif gold_box == "B":
            print("\nWise choice, that would have been too easy!")
            keep_moving()
            break
        else:
            print("_________________________")
            print("Invalid.\nPlease choose either A or B.")


def keep_moving():
    """
    Function called when user does not open gold box,
    will gain 1 point towards scoreboard.
    """
    gain_one_point()

    print("_________________________")
    print("\nLet's get out of here!")
    print("_________________________")
    print("You encounter heavily armed aliens!")
    print("They are coming at you from all angles!")
    print("We have only 2 options here. Would you rather")
    print("fight back and A= Choose a weapon, or B= Surrender")
    print("and try to make friends?")
    print("\nWhat will you do? Can you trust them?")

    encounter_aliens = input("Please choose A or B: ")

    while True:
        if encounter_aliens == "A":
            print("\nYou got this, let's go get 'em!!!")
            weapon_choice()
            break
        elif encounter_aliens == "B":
            print("\nIt was a trap! Humans can't be friends with Aliens.")
            lose_one_point()
            break
        else:
            print("_________________________")
            print("Invalid.\nPlease choose either A or B.")


def weapon_choice():
    """
    Function called when user decides to choose a weapon against
    aliens, will gain 1 point towards scoreboard.
    """
    gain_one_point()

    print("_________________________")
    print("\nGood choice! Who ever thought humans could be friends with aliens??")
    print("_________________________")
    print("Now we need to think this through. What would be the most valuable")
    print("weapon against the aliens? They have gotten closer and you are")
    print("running out of time. You must choose a weapon, and fast!\n")
    print("The government has provided 2 options for those willing to fight.")
    print("Which would be more useful..?")
    print("A= a Lazer blaster, or B= a Cloak of invisibility?\n")

    choose_weapon = input("Hurry! What do you choose? ")

    while True:
        if choose_weapon == "A":
            print("\nUh oh... The aliens shut down all technology from Earth!")
            lose_one_point()
            break
        elif choose_weapon == "B":
            print("\nWhew! Close one! All technology has been shut down!")
            invisible_cloak()
            break
        else:
            print("_________________________")
            print("Invalid.\nPlease choose either A or B.")


def invisible_cloak():
    """
    Function called when user chooses invisible cloak for a weapon,
    will gain 1 point towards scoreboard.
    """
    gain_one_point()

    print("_________________________")
    print("\nYou managed to get away with your cloak!")
    print("_________________________")
    print("Man... this thing is suffocating!!! It looks like we lost the")
    print("aliens! We must keep moving to find the secret passage. Do we dare")
    print("take off the cloak? There's no one around... what do you do?")

    cloak_decision = input("A= Keep the cloak on, or B= Take the cloak off? ")

    while True:
        if cloak_decision == "A":
            print("\nYou managed to make it to the secret passage!")
            #end game -- win!
            break
        elif cloak_decision == "B":
            print("\nThe aliens can see everything! They spotted you")
            print("and now you are captured forever...")
            lose_one_point()
            break
        else:
            print("_________________________")
            print("Invalid.\nPlease choose either A or B.")


def rules_of_game():
    """
    Lists the rules of the game and 
    allows user to start game if chosen
    """
    print("_________________________")
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
            print("Goodbye.")
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