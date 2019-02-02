'''
7 Days - The Game - Example Code
Text-based game where the user must survive their first 7 days on a foreign planet.
'''

import os
import random
import time    # add delay between events

# local imports
from title import display_title_screen

# add color output
# https://github.com/tartley/colorama
from colorama import init
init()

from colorama import Fore, Back, Style


def display_day01():
    '''
    Display day 01 in story
    '''
    clear_screen()
    # (Bright) Blue text
    print(Fore.BLUE + Style.BRIGHT + "DAY 1")
    print("===============")
    # create random delay between 0 and 1 seconds
    time.sleep(random.random())

    # Change the color back to normal
    print(Style.RESET_ALL + "")
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
    print("which you now see approximately 20 feet behind you.")
    time.sleep(random.random())

    # Get main character name (still day 01)
    # Add color: Yellow text for user input
    name = input(Fore.YELLOW + "What was your name again?: " + Style.RESET_ALL)

    # Use str.title method to capitalize first letter of user name
    print("\nWell,", name.title(), ", you tell yourself...")
    print("It's time to figure out what's going on.")

    # Give the user a decision to make. Depending on their answer,
    # the game either ends here or they continue on to day 2
    # Add color: Yellow text for user input
    answer = input(Fore.YELLOW + '''\nWould you like to
    [1] Go back to the spaceship to repair it or
    [2] go explore the forest?
    \nType 1 or 2 and press ENTER to continue:\
    ''' + Style.RESET_ALL)

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
    # (Bright) Blue text
    print(Fore.BLUE + Style.BRIGHT + "DAY 2")
    print("===============")
    # create random delay between 0 and 1 seconds
    time.sleep(random.random())

    # Change the color back to normal
    print(Style.RESET_ALL + "")
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
    answer = input(Fore.YELLOW + '''\nWould you like to
    [1] Eat the pizza. You're the master of danger! 🍕 + 🌳 = ❓
    [2] Try your hand at fishing instead 🐟 🐟 🐟
    \nType 1 or 2 and press ENTER to continue:\
    ''' + Style.RESET_ALL)

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
    # (Bright) Blue text
    print(Fore.BLUE + Style.BRIGHT + "DAY 3")
    print("===============")
    # create random delay between 0 and 1 seconds
    time.sleep(random.random())

    # Change the color back to normal
    print(Style.RESET_ALL + "")
    print("Welcome to day 3. You'll have to come back when this branch is finished!")


##############
# Run the game
# Add helper/utility functions
##############################


def start_game():
    '''
    Main function. This runs when the game is started or
    the player chooses to replay (after game over)
    '''
    display_title_screen()
    display_day01()

def clear_screen():
    '''
    Clear the terminal screen.
    '''
    os.system('clear')

def ask_play_again():
    '''
    Offer to play game again.
    '''
    answer = input(Fore.WHITE + Back.GREEN + "\nPlay again? (Y/N): " + Style.RESET_ALL)
    if answer.upper() == "Y":
        start_game()
    else:
        print("Thank you for playing!")

def game_over_because(reason):
    '''
    Display game over screen.
    '''
    print(Fore.RED + "\nGAME OVER\n===============\n" + reason  + "\nBetter luck next time!")
    # Ask if the user wants to play again
    ask_play_again()

start_game()
