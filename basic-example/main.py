'''
7 Days - The Game - Example Code
Text-based game where the user must survive their first 7 days on a foreign planet.

Basic example - This version does not use color, animation, etc. It is meant to show
the basic requirements of the project.
'''

import os
import random
import time    # add delay between events

def display_title_screen():
    '''
    Display title screen with delay between typing
    '''
    text = '''
    ███████╗    ██████╗  █████╗ ██╗   ██╗███████╗
    ╚════██║    ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
        ██╔╝    ██║  ██║███████║ ╚████╔╝ ███████╗
       ██╔╝     ██║  ██║██╔══██║  ╚██╔╝  ╚════██║
       ██║      ██████╔╝██║  ██║   ██║   ███████║
       ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
       '''

    print(text)

    print("An exciting adventure game.")

    # blank line
    print("")

    #Pause until the user presses the enter key
    input("Press enter to begin...")

def display_day01():
    '''
    Display day 01 in story
    '''

    clear_screen()
    print("DAY 1")
    print("===============")
    # create random delay between 0 and 1 seconds
    time.sleep(random.random())

    print("You wake up.")
    print("")
    time.sleep(random.random())

    print("Looking down at your watch, you notice that it's 8 AM. ⏰")
    print("...")
    time.sleep(random.random())

    print("You are not sure where you are, 🗺")
    print("but you begin to remember a crash landing in your space vehicle,")
    print("")
    time.sleep(random.random())
    print("🚀")
    time.sleep(random.random())
    print("🌠")
    time.sleep(random.random())
    print("🔥 🔥 🔥")
    time.sleep(random.random())
    print("")
    print("which you now see approximately 20 feet behind you.")
    time.sleep(random.random())

    # Get main character name (still day 01)
    print("What was your name again?: ")
    name = input()

    # Use str.title method to capitalize first letter of user name
    print("\nWell,", name.title(), ", you tell yourself...")
    print("It's time to figure out what's going on.")

    # Give the user a decision to make. Depending on their answer,
    # the game either ends here or they continue on to day 2
    question = '''\nWould you like to
    [1] Go back to the spaceship to repair it or
    [2] go explore the forest?
    \nType 1 or 2 and press ENTER to continue:\
    '''

    print(question)
    answer = input()

    print("\n>> Your answer was: ", answer, "<<\n")

    if answer == "1":
        # Player is going back to the spaceship.. bad choice
        game_over_because("Your choice to go back to the spaceship was ultimately the wrong one.")
    else:
        # Player moves on to day 02
        display_day02()

def display_day02():
    '''
    Display day 02 in the story.
    '''
    clear_screen()
    print("DAY 2")
    print("===============")
    # create random delay between 0 and 1 seconds
    time.sleep(random.random())

    print("")
    print("Forget the space ship! ... you tell yourself. ")
    time.sleep(random.random())

    print("")
    print("It's time that I live a little!")
    print("Let's see what this forest has to offer.")
    time.sleep(random.random())

    print("...")
    print("")
    print("As you stumble along in the forest, you come across a pizza!")
    time.sleep(random.random())

    print("...")
    print("")
    # system sleep for 1 second
    time.sleep(1)
    print("Wait a minute... you tell yourself")

    print("...")
    print("")
    time.sleep(0.5)

    print("I am super hungry, but this seems too good to be true!")
    print("You have a decision to make:")

    # Give the user a decision to make. Depending on their answer,
    # the game either ends here or they continue on to day 2
    question = '''\nWould you like to
    [1] Eat the pizza. You're the master of danger!
    [2] Try your hand at fishing instead
    \nType 1 or 2 and press ENTER to continue:\
    '''

    print(question)
    answer = input()

    print("\n>> Your answer was: ", answer, "<<\n")

    if answer == "1":
        # Player decides to eat the forest pizza (gross!)
        game_over_because("\nYour choice to eat a random pizza that you found on the forest floor was a poor one. \nYou must suffer the consequences!\n")
    else:
        # Player moves on to day 02
        display_day03()

def display_day03():
    '''
    Display day 03 in the story.
    '''
    clear_screen()
    print("DAY 3")
    print("===============")
    # create random delay between 0 and 1 seconds
    time.sleep(random.random())
    print("Welcome to day 3. You'll have to come back when this branch is finished!")


##############
# Run the game
# Add helper/utility functions
##############################

def clear_screen():
    '''
    Clear the terminal screen.
    '''
    os.system('clear')

def ask_play_again():
    '''
    Offer to play game again.
    '''
    print("")
    question = "Play again? (Y/N): "
    print(question)
    answer = input()
    if answer.upper() == "Y":
        start_game()
    else:
        print("Thank you for playing!")

def game_over_because(reason):
    '''
    Display game over screen.
    '''
    print("\nGAME OVER\n===============\n" + reason  + "\nBetter luck next time!")
    # Ask if the user wants to play again
    ask_play_again()

def start_game(day=1):
    '''
    Main function. This runs when the game is started or
    the player chooses to replay (after game over)

    Default start day is 1, but can be changed by day= parameter. This is helpful
    when testing days further into the game so that you don't have to wait to
    get to the day you're working on.
    '''
    clear_screen()
    display_title_screen()

    if day == 1:
        display_day01()
    else:
        day_string = 'display_day0' + str(day)
        globals()[day_string]() # start_game(day=2) -> display_day02


# Main loop
start_game(day=1)
