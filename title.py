'''
Title screen for 7 days game
'''

import time
import random

# add color output
# https://github.com/tartley/colorama
from colorama import init
init()

from colorama import Fore, Back, Style

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
        # Print each line in green text
        print(Fore.GREEN + line)
        # create random delay between 0 and 1 seconds
        time.sleep(random.random())

    # Change the color back to normal
    print(Style.RESET_ALL)
    # Pause until the user presses the enter key
    input("Press enter to begin...")
