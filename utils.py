'''
Utility functions for 7 days game
'''

import sys
import os
import random
import time


def clear_screen():
    '''
    Clear the terminal screen.
    '''
    os.system('clear')


def game_over_because(reason):
    '''
    Display game over screen.
    '''
    print("\nGAME OVER\n===============\n",reason, "\nBetter luck next time!")
