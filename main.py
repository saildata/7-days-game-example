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

    print("")
    print("You wake up.")
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
    cprint("\nWhat was your name again?: ", fg='y')
    name = input()

    # Use str.title method to capitalize first letter of user name
    print("\nWell,", name.title(), ", you tell yourself...")
    print("It's time to figure out what's going on.")
    time.sleep(random.randrange(1,2))

    # Give the user a decision to make. Depending on their answer,
    # the game either ends here or they continue on to day 2
    question = '''\nWould you like to
    [1] Go back to the spaceship to repair it 🛠  or
    [2] go explore the forest? 🌲 🌲 🌲
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
    # create random delay between 1 and 2 seconds
    time.sleep(random.randrange(1,2))

    print("")
    print("Forget the space ship! 🚀  ... ")
    time.sleep(random.randrange(1,2))

    print("")
    print("It's time that I live a little! 🎉")
    print("Let's see what this forest has to offer.")
    time.sleep(random.randrange(2,3))

    print("...")
    print("")
    print("As you stumble along in the forest, you come across a pizza! 🍕")
    time.sleep(random.randrange(2,3))

    print("...")
    print("")
    print("Wait a minute ... thinking outloud, you realize ...")
    time.sleep(random.randrange(1,2))

    print("...")
    print("")
    time.sleep(random.randrange(1,2))

    print("I am super hungry, but this seems too good to be true!")
    print("You have a decision to make:")
    time.sleep(random.randrange(2,3))

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
    # create random delay between 1 and 2 seconds
    time.sleep(random.randrange(1,2))

    print("")
    print("You continue on walking through the forest. 🌲 🌲 🌲")
    time.sleep(random.randrange(1,2))
    print("")
    print("Your mission is to find a stick so that you can make a fishing pole and finally eat! 🎣")
    time.sleep(random.randrange(2,3))
    print("")
    print("You manage to find 🔍 a stick and put together a simple, although functional fishing pole. 😎")
    time.sleep(random.randrange(3,4))
    print("")
    print("Luckily 🍀 you also come across a small lake")
    time.sleep(random.randrange(1,2))
    print("")
    print("Now, about to faint due to lack of food, you sit down and begin fishing.")
    print("")
    time.sleep(random.randrange(2,3))

    # Sun / lake with fish
    # sun copied from wego project https://github.com/schachmat/wego/blob/master/frontends/ascii-art-table.go

    cprint("                            \\   /  ", fg='y')
    cprint("                             .-.    ", fg='y')
    cprint("                          ‒ (   ) ‒ ", fg='y')
    cprint("                             `-᾿    ", fg='y')
    cprint("                            /   \\  ", fg='y')
    cprint("                                    ")
    cprint("\🐟/\  /\  /\🐟/\  /\  /\🐟/\  /\  /", fg='b', style='x')
    cprint(" \/  \/🐟\/  \/  \/🐟\/  \/  \/🐟\/ ", fg='b', style='x')
    time.sleep(4)
    clear_screen()

    # stop the blinking to avoid rage quit
    cprint("                            \\   /  ", fg='y')
    cprint("                             .-.    ", fg='y')
    cprint("                          ‒ (   ) ‒ ", fg='y')
    cprint("                             `-᾿    ", fg='y')
    cprint("                            /   \\  ", fg='y')
    cprint("                                    ")
    cprint("\🐟/\  /\  /\🐟/\  /\  /\🐟/\  /\  /", fg='b')
    cprint(" \/  \/🐟\/  \/  \/🐟\/  \/  \/🐟\/ ", fg='b')

    print("")
    print("After waiting about 10 minutes 🕑 you feel a tug on the line.")
    time.sleep(random.randrange(2,3))
    print("You caught a fish! Good job. 🏆")
    time.sleep(random.randrange(2,3))

    print("")
    print("You cook the fish over a fire and feel satisfied. 🔥 🐟")
    time.sleep(random.randrange(2,3))

    print("It's now almost night time. The sun begins to disappear into the horizon. 🌇")
    time.sleep(random.randrange(2,3))
    print("")
    print("You have a decision to make:")
    time.sleep(random.randrange(1,2))

    # Give the user a decision to make. Depending on their answer,
    # the game either ends here or they continue on to day 4
    question = '''\nWould you like to
    [1] Sleep on the lake shore under the stars. 🌃 ⛺
    [2] Go to the cave you see in the distance. That looks like a warm place to stay for the night. 👻
    \nType 1 or 2 and press ENTER to continue:\
    '''
    # Yellow text
    cprint(question, fg='y')
    answer = input()

    print("\n>> Your answer was: ", answer, "<<\n")
    time.sleep(random.randrange(1,2))

    if answer == "1":
        # Player decides to sleep on the lake shore and moves on to day 4.
        display_day04()
    else:
        # Player decides to go to the cave
        game_over_because("\nYour choice to sleep in a cave was not a wise one. You found a bear, and the bear found dinner. 🐻 \n")

def display_day04():
    '''
    Display day 04 in the story.
    '''
    clear_screen()
    # Blue text
    cprint("DAY 4", fg='b')
    cprint("===============", fg='b')
    # create random delay between 1 and 2 seconds
    time.sleep(random.randrange(1,2))

    print("")
    print("You wake up on day 4 and continue on your journey.")



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
