'''
7 Days - The Game - Example Code
Text-based game where the user must survive their first 7 days on a foreign planet.
'''

import os
import random
import time    # add delay between events

# local imports
from cprint import cprint
from title import display_title_screen
import art

def display_day01():
    '''
    Display day 01 in story
    '''

    clear_screen()

    # Spaceship ASCII art
    # Add animation "effect" using
    # decreasing image width - see art.py file
    cprint(art.ASCII_SPACESHIP_01, fg='g')
    time.sleep(1)
    clear_screen()
    cprint(art.ASCII_SPACESHIP_02, fg='g')
    time.sleep(1)
    clear_screen()
    cprint(art.ASCII_SPACESHIP_03, fg='g')
    time.sleep(2)
    clear_screen()

    # Blue text
    cprint("DAY 1", fg='b')
    cprint("===============", fg='b')
    # create random delay between 1 and 2 seconds
    time.sleep(random.randrange(1,2))

    print("You wake up.")
    print("")
    time.sleep(random.randrange(1,2))
    print("Looking down at your watch, you notice that it's 8 AM. ⏰")
    print("...")
    time.sleep(random.randrange(1,2))

    print("You are not sure where you are, 🗺")
    print("but you begin to remember a crash landing in your space vehicle,")
    print("")
    time.sleep(random.randrange(1,2))
    print("🚀")
    time.sleep(random.randrange(1,2))
    print("🌠")
    time.sleep(random.randrange(1,2))
    print("🔥 🔥 🔥")
    time.sleep(random.randrange(1,2))
    print("")
    print("which you now see approximately 20 feet behind you.")
    time.sleep(random.randrange(1,2))

    # Get main character name (still day 01)
    # Add color: Yellow text for user input
    cprint("What was your name again?: ", fg='y')
    name = input()

    # Use str.title method to capitalize first letter of user name
    print("\nWell,", name.title(), ", you tell yourself...")
    print("It's time to figure out what's going on.")
    time.sleep(random.randrange(1,2))

    # Give the user a decision to make. Depending on their answer,
    # the game either ends here or they continue on to day 2
    question = '''\nWould you like to
    [1] Go back to the spaceship to repair it or
    [2] go explore the forest?
    \nType 1 or 2 and press ENTER to continue:\
    '''
    # Yellow text
    cprint(question, fg='y')
    answer = input()

    print("\n>> Your answer was: ", answer, "<<\n")
    time.sleep(random.randrange(1,2))

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
    # Blue text
    cprint("DAY 2", fg='b')
    cprint("===============", fg='b')
    # create random delay between 0 and 1 seconds
    time.sleep(random.randrange(1,2))

    print("")
    print("Forget the space ship! ... ")
    time.sleep(random.randrange(1,2))

    print("")
    print("It's time that I live a little!")
    print("Let's see what this forest has to offer.")
    time.sleep(random.randrange(1,2))

    print("...")
    print("")
    print("As you stumble along in the forest, you come across a pizza!")
    time.sleep(random.randrange(1,2))

    print("...")
    print("")
    print("Wait a minute... thinking outloud, you realize ...")
    time.sleep(random.randrange(1,2))

    print("...")
    print("")
    time.sleep(random.randrange(1,2))

    print("I am super hungry, but this seems too good to be true!")
    print("You have a decision to make:")
    time.sleep(random.randrange(1,2))

    # Give the user a decision to make. Depending on their answer,
    # the game either ends here or they continue on to day 3
    question = '''\nWould you like to
    [1] Eat the pizza. You're the master of danger! 🍕 + 🌳 = ❓
    [2] Try your hand at fishing instead 🐟 🐟 🐟
    \nType 1 or 2 and press ENTER to continue:\
    '''
    # Yellow text
    cprint(question, fg='y')
    answer = input()

    print("\n>> Your answer was: ", answer, "<<\n")
    time.sleep(random.randrange(1,2))

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
    # Blue text
    cprint("DAY 3", fg='b')
    cprint("===============", fg='b')
    # create random delay between 0 and 1 seconds
    time.sleep(random.randrange(1,2))
    print("Welcome to day 3. You'll have to come back when this branch is finished!")



##############
# Run the game
# Add helper/utility functions
##############################

def ask_play_again():
    '''
    Offer to play game again.
    '''
    print("")
    question = "Play again? (Y/N): "
    cprint(question, fg='g', bg='k')
    answer = input()
    if answer.upper() == "Y":
        start_game()
    else:
        print("Thank you for playing!")


def clear_screen():
    '''
    Clear the terminal screen.
    '''
    os.system('clear')


def game_over_because(reason):
    '''
    Display game over screen.
    '''
    cprint("\nGAME OVER\n===============\n" + reason  + "\nBetter luck next time!", fg='r')
    # Ask if the user wants to play again
    ask_play_again()


def start_game():
    '''
    Main function. This runs when the game is started or
    the player chooses to replay (after game over)
    '''
    clear_screen()
    display_title_screen()
    display_day01()


# Main loop
start_game()
