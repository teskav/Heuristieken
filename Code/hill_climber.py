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
    solutions = []
    # starting solution -> buiten hill climber
    current_solution = random_all_parcels()

    # select neighbouring solution
    while count < max_iterations:

        check, neighbour_solution = neighbour_random_parcel_switch(current_solution)

        # compare costs & check of hij geen error geeft
        if neighbour_solution.costs < current_solution.costs and check == True:
            current_solution = neighbour_solution

        dataframe_row = spacefreight.save_iteration(current_solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)
        solutions.append(current_solution.costs)
        count += 1

    return iterations_dataframe, count, current_solution, solutions


def neighbour_random_parcel_switch(current_solution):
    """
    Returns the neighbouring solution in a Solution class
    """
    neighbour_solution = copy.copy(current_solution)
    # selecting the spacecrafts
    spacecraft_1 = random.choice(neighbour_solution.used_spacecrafts)
    spacecraft_2 = random.choice(neighbour_solution.used_spacecrafts)

    # select the parcels from the spacecrafts random
    parcel_1 = random.choice(spacecraft_1.packed_parcels)
    parcel_2 = random.choice(spacecraft_2.packed_parcels)

    # check if the to swap parcels are not the same
    if spacecraft_1 == spacecraft_2 and parcel_1 == parcel_2:
        return False, current_solution
    else:
        check = spacefreight.swap_parcel(spacecraft_1, spacecraft_2, parcel_1, parcel_2)
        # update costs
        neighbour_solution.costs = spacefreight.calculate_costs(neighbour_solution)


    # switch parcels in spacecraft
    return check, neighbour_solution
