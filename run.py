"""
This is a fun adventure game that will take the user through a series of 
choices to see how far they can get in the game!
"""
import gspread
from google.oauth2.service_account import Credentials

GOOGLE_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(GOOGLE_SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('adventure_scoreboard')

scores = SHEET.worksheet('scoreboard')

data = scores.get_all_values()

#print(data) ***confirmed spreadsheet is linked***

def start_game(username):
    """
    Begins the adventure game
    User must choose an option
    """
    output_str = '''
    Welcome to the end of the world as we know it.
    You have the option to either go to Mars and start a new world,
    or stay on Earth for it's final 5 years.

    Do you choose A= Go to Mars, or B= Stay on Earth?
    '''
    print(output_str)

    while True:
        try:
            location_choice = input("\nWhere do you want to go? ")

            if location_choice == "A":
                print("__________")
                print("You are going to Mars!")
                go_to_mars(username)
                break
            elif location_choice == "B":
                print("__________")
                print("Earth it is!")
                stay_on_earth(username)
                break
            else:
                print("_________________________")
                print("Invalid.\nPlease choose either capital A or B.")
        except ValueError:
            print("Invalid.\nPlease choose either capital A or B.")


def gain_one_point(username):
    """
    Function to add one point to score
    and update leaderboard
    """
    score = 0
    print("_________________________")
    print("*** You managed to stay alive. Earn one point. ***")
    print("_________________________")
    print(f"{username}, your score is now {score}.")


def lose_one_point(username):
    """
    Function to remove one point from score
    and update leaderboard. Game is over.
    """
    score = 0
    print("_________________________")
    print("*** You didn't make it... Lose one point. ***")
    print("_________________________")
    print("Sorry, game over.")
    print(f"{username}, your score is now {score}.")


def go_to_mars(username):
    """
    Users first option and since still alive,
    will gain 1 point towards scoreboard.
    """
    gain_one_point(username)

    output_str = '''
    Now, the thing about Mars is...
    No one knew there were already aliens living there!

    ... The next day you are packed onto a space shuttle
    and become one of the first people to land on Mars.

    The air is cold and damp and it's so dark you can barely
    make out shadows in the distance. There are strange, long
    creatures coming towards you at an alarming speed!\n
    You have one chance to change your mind.
    Do you... 
    A= Stay and wait to see what happens, or
    B= Sneak back on the space shuttle and go back to Earth?
    '''
    print(output_str)

    while True:
        try:
            decision_one = input("What do you want to do? ")

            if decision_one == "A":
                print("\nOh, how brave of you...")
                stay_on_mars(username)
                break
            elif decision_one == "B":
                print("\nEarth couldn't have gotten worse... could it?")
                stay_on_earth(username)
                break
            else:
                print("_________________________")
                print("Invalid.\nPlease choose either capital A or B.")
        except ValueError:
            print("Invalid.\nPlease choose either capital A or B.")


def stay_on_earth(username):
    """
    Users first option and since still alive,
    will gain 1 point towards scoreboard.
    """
    gain_one_point(username)

    output_str = '''
    So glad you chose Earth! Who knows WHAT's on Mars!
    The world is due to end in exactly 5 years.
    Who knows what you will encounter until then...

    Things have taken a turn for the worse and natural disasters
    are hitting every continent at once!
    Will you be able to survive Earth's final years if it's THIS bad?
    There is an underground bunker that was created to offer more
    peace for the final days...

    Do you...
    A= Move to the underground bunker, or
    B= Try to survive in the wild?
    '''
    print(output_str)

    while True:
        try:
            survival_location = input("Which do you choose? A or B? ")

            if survival_location == "A":
                print("\nIt was a trap! The bunker explodes.")
                lose_one_point(username)
                break
            elif survival_location == "B":
                print("\nThe whole bunker just exploded!")
                print("Whew! Good thing you chose to stay in the wild!")
                stay_in_wild(username)
                break
            else:
                print("_________________________")
                print("Invalid.\nPlease choose either capital A or B.")
        except ValueError:
            print("Invalid.\nPlease choose either capital A or B.")


def stay_in_wild(username):
    """
    Function called when user decides to stay in the wild,
    will gain 1 point towards scoreboard.
    """
    gain_one_point(username)

    output_str = '''
    The government has seized all properties still standing and
    you are thrown into the streets, literally into the wild!

    Uh oh, a virus has spread and everyone is turning into zombies!
    They are coming from all angles! 
    
    You have two choices...
    A= Let them attack and become a zombie, or
    B= Choose a weapon and fight! 
    
    Better choose quickly!
    '''
    print(output_str)

    while True:
        try:
            zombie_choice = input("A or B? ")

            if zombie_choice == "A":
                print("\nAll zombies have been wiped out by the A-Team!")
                lose_one_point(username)
                break
            elif zombie_choice == "B":
                print("\nThe zombies were wiped out! But now there are more")
                print("coming... Time to choose your weapon.")
                zombie_weapon_choice(username)
                break
            else:
                print("_________________________")
                print("Invalid.\nPlease choose either capital A or B.")
        except ValueError:
            print("Invalid.\nPlease choose either capital A or B.")


def zombie_weapon_choice(username):
    """
    Function called when user chooses a weapon against the zombies,
    will gain 1 point towards scoreboard.
    """
    gain_one_point(username)

    output_str = '''
    Zombies are close and you are unarmed!
    You manage to make it to the nearest weapons.

    Upon entering the large warehouse built just for this scenario,
    you see magical cloaks to your left.. cloaks of invisibility.

    To your right is a huge truck FULL of guns! The whole truck could
    be yours! 
    
    Do you want...
    A= the Cloak of invisibility, or
    B= the entire truck filled with guns?
    '''
    print(output_str)

    while True:
        try:
            truck_or_cloak = input("Which do you choose? A or B? ")

            if truck_or_cloak == "A":
                print("\nGood choice! The government just seized all ammunition!")
                print("The truck would have been no use.")
                cloak_weapon(username)
                break
            elif truck_or_cloak == "B":
                print("\nAll ammunition was seized by the government and you are")
                print("left with nothing. Zombies attack and you die.")
                lose_one_point(username)
                break
            else:
                print("_________________________")
                print("Invalid.\nPlease choose either capital A or B.")
        except ValueError:
            print("Invalid.\nPlease choose either capital A or B.")


def cloak_weapon(username):
    """
    Function called when user chooses the cloak against the zombies,
    will gain 1 point towards scoreboard.
    """
    gain_one_point(username)

    output_str = '''
    You managed to get away from the hoards of zombies, thanks to being
    invisible! As you take in your surroundings, from the safety of
    your cloak, you see buildings on fire, sinkholes swallowing up cars,
    people and everything in site.
    
    As you were searching through that warehouse, you overheard others talking
    about seeking refuge at the capital building... 
    
    You have to try to make it there, as it may be your last chance for survival. 
    The only problem is, this cloak is just so suffocating!

    Do you...
    A= Keep the cloak on, or
    B= Take the cloak off?
    '''
    print(output_str)

    while True:
        try:
            final_earth_decision = input("Which do you choose? A or B? ")

            if final_earth_decision == "A":
                print("\nYou managed to make it to the capital building alive!")
                #end game -- win!
                break
            elif final_earth_decision == "B":
                print("\nTurns out you weren't completely alone...")
                print("A group of zombies spot and kill you.")
                lose_one_point(username)
                break
            else:
                print("_________________________")
                print("Invalid.\nPlease choose either capital A or B.")
        except ValueError:
            print("Invalid.\nPlease choose either capital A or B.")


def stay_on_mars(username):
    """
    Function called when user decides to stay on Mars, 
    will gain 1 point towards scoreboard.
    """
    gain_one_point(username)

    output_str = '''
    Well then... here goes nothing!

    Rumour has it.. there is a safe, uninhabited part of Mars!
    The best chance you have is to find the secret passage there, and quickly,
    before the aliens catch you!

    The aliens are getting closer...
    You turn to run the opposite direction and trip over a bright, shiny gold box!
    Could this be a clue to the secret passage???
    This is tempting... What will you do?

    '''
    print(output_str)

    while True:
        try:
            gold_box = input("A= Open box, or B= Keep moving? ")

            if gold_box == "A":
                print("\nOh no! It was a trap! The box exploded and you die.")
                lose_one_point(username)
                break
            elif gold_box == "B":
                print("\nWise choice, that would have been too easy!")
                keep_moving(username)
                break
            else:
                print("_________________________")
                print("Invalid.\nPlease choose either capital A or B.")
        except ValueError:
            print("Invalid.\nPlease choose either capital A or B.")


def keep_moving(username):
    """
    Function called when user does not open gold box,
    will gain 1 point towards scoreboard.
    """
    gain_one_point(username)

    output_str = '''
    Let's get out of here!

    You encounter heavily armed aliens!
    They are coming at you from all angles!

    We have only 2 options here. 
    Would you ratherfight back and...
    A= Choose a weapon, or
    B= Surrender and try to make friends?

    What will you do? Can you trust them?
    '''
    print(output_str)

    while True:
        try:
            encounter_aliens = input("Please choose A or B: ")

            if encounter_aliens == "A":
                print("\nYou got this, let's go get 'em!!!")
                weapon_choice(username)
                break
            elif encounter_aliens == "B":
                print("\nIt was a trap! Humans can't be friends with Aliens.")
                lose_one_point(username)
                break
            else:
                print("_________________________")
                print("Invalid.\nPlease choose either capital A or B.")
        except ValueError:
            print("Invalid.\nPlease choose either capital A or B.")


def weapon_choice(username):
    """
    Function called when user decides to choose a weapon against
    aliens, will gain 1 point towards scoreboard.
    """
    gain_one_point(username)

    output_str = '''
    Good choice! Who ever thought humans could be friends with aliens??

    Now we need to think this through...
    What would be the most valuable weapon against the aliens?

    They have gotten closer and you are running out of time. 
    You must choose a weapon, and fast!
    The government has provided 2 options for those willing to fight.

    Which would be more useful..?
    A= a Lazer blaster, or
    B= a Cloak of invisibility?
    '''
    print(output_str)

    while True:
        try:
            choose_weapon = input("Hurry! What do you choose? ")

            if choose_weapon == "A":
                print("\nUh oh... The aliens shut down all technology from Earth!")
                lose_one_point(username)
                break
            elif choose_weapon == "B":
                print("\nWhew! Close one! All technology has been shut down!")
                invisible_cloak(username)
                break
            else:
                print("_________________________")
                print("Invalid.\nPlease choose either capital A or B.")
        except ValueError:
            print("Invalid.\nPlease choose either capital A or B.")


def invisible_cloak(username):
    """
    Function called when user chooses invisible cloak for a weapon,
    will gain 1 point towards scoreboard.
    """
    gain_one_point(username)

    output_str = '''
    You managed to get away with your cloak!

    Man... this thing is suffocating!!! 
    It looks like we lost the aliens!
    We must keep moving to find the secret passage.
    
    Do we dare take off the cloak? 
    There's no one around... what do you do?
    '''
    print(output_str)

    while True:
        try:
            cloak_decision = input("A= Keep the cloak on, or B= Take the cloak off? ")

            if cloak_decision == "A":
                print("\nYou managed to make it to the secret passage!")
                #end game -- win!
                break
            elif cloak_decision == "B":
                print("\nThe aliens can see everything! They spotted you")
                print("and now you are captured forever...")
                lose_one_point(username)
                break
            else:
                print("_________________________")
                print("Invalid.\nPlease choose either capital A or B.")
        except ValueError:
            print("Invalid.\nPlease choose either capital A or B.")


def rules_of_game(username):
    """
    Lists the rules of the game and 
    allows user to start game if chosen
    """
    output_str = '''
    Rules:

    You will be taken through a text-based, option-driven game.
    Please choose your desired option, either 'A' or 'B', when prompted.

    Each chosen response will accumulate a certain number of points.
    These points will be added to the leaderboard!

    If at any stage you wish to pause and save your progress,
    please type 'PAUSE' into the terminal.

    If at any stage you wish to end your adventure and restart the
    game, please type 'EXIT' into the terminal.
    
    Now...  do you dare play the game?
    '''
    print(output_str)

    while True:
        answer = input("Yes or No? ")

        if answer == "Yes":
            start_game(username)
            break
        elif answer == "No":
            print("\nI guess you'll never know how it ends!")
            print("Goodbye.")
            break
        else:
            print("_________________________")
            print("Please enter...")

def adventure_welcome():
    """
    This function is called when the program is run and 
    displays the welcome message with initial options.
    """
    print("\n\tWelcome to the adventure!")
    print("\n\tIt's almost the end of the world...\n")
    username = input("Who is playing? ")

    print("_________________________")
    print(f"Here we go, {username}! Please choose what you would like to do:\n")
    print("A - See rules of game")
    print("B - Start game")
    print("C - See scoreboard")

    while True:
        option = input("\nPlease choose A, B, or C: ")

        if option == "A":
            rules_of_game(username)
            break
        elif option == "B":
            print("Starting game...")
            start_game(username)
            break
        elif option == "C":
            print("Hang tight while we tally up the scoreboard...")
            print("Scoreboard (from google spreadsheet)")
            break
        else:
            print("_________________________")
            print("Sorry, invalid input.")


adventure_welcome()
