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


def hill_climber(iterations_dataframe, max_iterations):
    count = 0
    # starting solution
    current_solution = random_greedy()

    # select neighbouring solution
    while count < max_iterations:

        check, neighbour_solution = neighbour_random_parcel_switch(current_solution)
        print(neighbour_solution.costs)

        # compare costs & check of hij geen error geeft
        if neighbour_solution.costs <= current_solution.costs and check == True:
            current_solution = neighbour_solution

        dataframe_row = spacefreight.save_iteration(current_solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)
        count += 1

    return iterations_dataframe


def neighbour_random_parcel_switch(current_solution):
    """
    Returns the neighbouring solution in a Solution class
    """

    # selecting the spacecrafts
    spacecraft_1 = random.choice(current_solution.used_spacecrafts)
    spacecraft_2 = random.choice(current_solution.used_spacecrafts)

    # select the parcels from the spacecrafts random
    parcel_1 = random.choice(spacecraft_1.packed_parcels)
    parcel_2 = random.choice(spacecraft_2.packed_parcels)

    # check if the to swap parcels are not the same
    if spacecraft_1 == spacecraft_2 and parcel_1 == parcel_2:
        return False, current_solution
    else:
        check = spacefreight.swap_parcel(spacecraft_1, spacecraft_2, parcel_1, parcel_2)
        print('hoi')
        # update costs
        current_solution.costs = spacefreight.calculate_costs(current_solution)


    # switch parcels in spacecraft
    return check, current_solution
