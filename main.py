# 7 Days
# Text-based game where the user must survive their first 7 days on a foreign planet.

import os      # used for os.system('clear')
import random
import time    # add delay between events

def clear_screen():
    '''
    Clear the terminal screen.
    '''

    os.system('clear')

def display_title_screen():
    '''
    Display title screen with delay between typing
    '''

    text = ['''
    ███████╗    ██████╗  █████╗ ██╗   ██╗███████╗
    ╚════██║    ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
        ██╔╝    ██║  ██║███████║ ╚████╔╝ ███████╗
       ██╔╝     ██║  ██║██╔══██║  ╚██╔╝  ╚════██║
       ██║      ██████╔╝██║  ██║   ██║   ███████║
       ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
       ''',
    "     An exciting adventure game.",
    "",
    ]

    # Loop over the text for the intro screen one
    # line at a time
    for line in text:
        print(line)
        # create random delay between 0 and 1 seconds
        time.sleep(random.random())

    # Pause until the user presses the enter key
    input("Press enter to begin...")

def game_over_because(reason):
    '''
    Display game over screen.
    '''

    print("\nGAME OVER\n===============\n",reason, "\nBetter luck next time!")

def display_day01():
    '''
    Display day 01 in story
    '''

    clear_screen()

    text = [
    "DAY 1\n===============",
    "You wake up.",
    "Looking down at your watch, you notice that it's 8 AM.",
    "You are not sure where you are ... ",
    "but you begin to remember a crash landing in your space vehicle,",
    "which you now see approximately 20 feet behind you."
    ]

    for i in text:
        print(i)
        # create random delay between 0 and 1 seconds
        time.sleep(random.random())
        # add line breaks
        print("\n")
        time.sleep(random.random())

    # Get main character name (still day 01)
    name = input("What was your name again?: ")

    print("\nWell,", name.title(), ", you tell yourself...")
    print("It's time to figure out what's going on.")

    # Give the user a decision to make. Depending on their answer,
    # the game either ends here or they continue on to day 2
    print("")
    answer = input("""
    Would you like to
    [1] Go back to the spaceship to repair it or
    [2] go explore the forest?
    \nType 1 or 2 and press enter to continue: """)

    #TODO: What if the player doesn't enter an appropriate answer??
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
    print("")
    print("Forget the space ship! ... you tell yourself. ")
    print("")
    print("It's time that I live a little!")
    print("Let's see what this forest has to offer.")

    print("...")
    print("")
    print("As you stumble along in the forest, you come across a pizza!")

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
    print("")
    answer = input("""
    Would you like to
    [1] Eat the pizza. You're the master of danger!
    [2] Try your hand at fishing instead
    \nType 1 or 2 and press enter to continue: """)

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
    print("Welcome to day 3. You'll have to come back when this branch is finished!")


########################
# Run the game
# Nothing should go below this other than the title screen
# and day 1. Days 2 - 7 should be called from the day before it.
# For example, day 2 should be called from day 1, not from here.
########################
display_title_screen()
display_day01()
