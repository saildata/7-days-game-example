'''
Title screen for 7 days game
'''

import time
import random

# local imports
from cprint import cprint

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
        cprint(line, fg='g')
        # create random delay between 0 and 1 seconds
        time.sleep(random.random())

    # Change the color back to normal
    cprint("")
    # Pause until the user presses the enter key
    input("Press enter to begin...")
