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
ITER = 100
count = 0

def hill_climber():

    # starting solution
    current_solution = random_greedy()

    # while count < ITER:
        # select neighbouring solution
    while count < ITER:
        neighbour = neighbour_random_parcel_switch(current_solution)

        #compare costs & check of hij geen error geeft
        # if cost(neig) < cost (current) and not neighbour == 'error':
        #     current sol = neighbour
        if neighbour.costs < current_solution.costs and not neighbour ==


def neighbour_random_parcel_switch(current_solution):
    """
    Returns the neighbouring solution in a Solution class
    """
    number_used_spacecrafts = len(current_solution.used_spacecrafts)
    # select the spacecrafts random (jullie hadden hier 4, het aantal spacecrafts)
    # maar als we hillclimber ook willen toepassen op algoritmes waar spacecrafts
    # meerdere keren worden ingezet, lijkt dit me een goede manier
    spacecraft_random_1 = random.randrange(number_used_spacecrafts) # kan ook gelijk in onderstaande line
    spacecraft_random_2 = random.randrange(number_used_spacecrafts)

    # selecting the spacecrafts
    # spacecraft_1_name = spacefreight.spacecrafts_names[spacecraft_random_1]
    # spacecraft_2_name = spacefreight.spacecrafts_names[spacecraft_random_2]
    spacecraft_1_name = current_solution.used_spacecrafts[spacecraft_random_1]
    spacecraft_2_name = current_solution.used_spacecrafts[spacecraft_random_2]

    # vraag wies
    # heeft current solution een attribute met de naam spacecraft_1_name?
    # ik denk dat dit nog niet helemaal klopt, maar weet ook niet hoe het wel zou moeten
    spacecraft_1_packed = getattr(current_solution, spacecraft_1_name)
    spacecraft_2_packed = getattr(current_solution, spacecraft_2_name)

    # select the parcels from the spacecrafts random
    parcel_random_1 = random.randrange(len(spacecraft_1_packed))
    parcel_random_2 = random.randrange(len(spacecraft_2_packed))

    parcel_1_ID = current_solution[spacecraft_1_name][parcel_random_1]
    parcel_2_ID = current_solution[spacecraft_2_name][parcel_random_2]

    # switch parcels in spacecraft
    # temp = current_solution[spacecraft_1_name][parcel_random_1]
    # current_solution[spacecraft_1_name][parcel_random_1] = current_solution[spacecraft_2_name][parcel_random_2]
    # current_solution[spacecraft_2_name][parcel_random_2] = temp
    spacefreight.swap_parcel(spacecraft_1_name, spacecraft_2_name, parcel_1_ID, parcel_2_ID)

    # if # check of de massa en volume van de spacecrafts wordt overschreden
    # return 'error' # als wel overschreden, niet de swap uitvoeren en error geven zodat hij doorkan naar volgende neighbour
    # else:
        # swap
