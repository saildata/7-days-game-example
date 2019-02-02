'''
Title screen for 7 days game
'''

import time
import random

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
