'''
Title screen for 7 days game
'''

import time
import random

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
