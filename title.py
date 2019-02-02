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
    text = '''
    ███████╗    ██████╗  █████╗ ██╗   ██╗███████╗
    ╚════██║    ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
        ██╔╝    ██║  ██║███████║ ╚████╔╝ ███████╗
       ██╔╝     ██║  ██║██╔══██║  ╚██╔╝  ╚════██║
       ██║      ██████╔╝██║  ██║   ██║   ███████║
       ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
       '''
    # green text, blinking
    cprint(text, fg='g', style='x')

    # green text
    cprint("An exciting adventure game.", fg='g')

    # blank line
    print("")
    
    #Pause until the user presses the enter key
    input("Press enter to begin...")
