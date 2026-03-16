"""
Program: Match Coins Game - Coin Class
Name: Elijah Drakeford
Purpose: Defines the Coin class, which represents a single coin
that is tossed and keeps track of whether it lands on heads or tails.
Starter Code: N/A
Date: March 15, 2026
"""

import random

class Coin:
    def __init__(self):
        # Coin with random side
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def toss(self):
        # Simulate tossing the coin
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        # Return the value of the coin
        return self.__sideup
