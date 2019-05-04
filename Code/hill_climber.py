#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script contains the different versions (functions) of the HILL CLIMBER algorithms
"""
from spacefreight import SpaceFreight
from random_algorithms_new import *
import random
import numpy as np
import copy

spacefreight = SpaceFreight()


def hill_climber():

    # starting solution
    current_solution = random_greedy()

    # while count < ITER:
        # select neighbouring solution
    neighbour = neighbour_random_parcel_switch(current_solution)

        #copare costs & check of hij geen error geeft
        # if cost(neig) < cost (current) and not neighbour == 'error':
        #     current sol = neighbour



def neighbour_random_parcel_switch(current_solution):
    """
    Returns the neighbouring solution in a Solution class
    """
    # select the spacecrafts random
    spacecraft_random_1 = random.randrange(4) # kan ook gelijk in onderstaande line
    spacecraft_random_2 = random.randrange(4)

    # selecting the spacecrafts
    spacecraft_1_name = spacefreight.spacecrafts_names[spacecraft_random_1]
    spacecraft_2_name = spacefreight.spacecrafts_names[spacecraft_random_2]

    spacecraft_1_packed = getattr(current_solution, spacecraft_1_name)
    spacecraft_2_packed = getattr(current_solution, spacecraft_2_name)

    # select the parcels from the spacecrafts random
    parcel_random_1 = random.randrange(len(spacecraft_1_packed))
    parcel_random_2 = random.randrange(len(spacecraft_2_packed))

    # switch parcels in spacecraft
    temp = current_solution[spacecraft_1_name][parcel_random_1]
    current_solution[spacecraft_1_name][parcel_random_1] = current_solution[spacecraft_2_name][parcel_random_2]
    current_solution[spacecraft_2_name][parcel_random_2] = temp

    # if # check of de massa en volume van de spacecrafts wordt overschreden
    # return 'error' # als wel overschreden, niet de swap uitvoeren en error geven zodat hij doorkan naar volgende neighbour
    # else:
        # swap
