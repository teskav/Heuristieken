#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script contains the different versions (functions) of the SIMULATED ANNEALING algorithms
"""
from spacefreight import SpaceFreight
from random_algorithms_new import *
import random
import numpy as np
import copy
import math

spacefreight = SpaceFreight()


def simulated_annealing(iterations_dataframe, max_iterations):
    count = 0
    # starting solution -> buiten hill climber
    current_solution = random_all_parcels()

    # select neighbouring solution
    while count < max_iterations:

        check, neighbour_solution = neighbour_random_parcel_switch(current_solution)
        print(check)
        print(neighbour_solution.costs)
        print(current_solution.costs)
        # compare costs & check of hij geen error geeft
        if neighbour_solution.costs < current_solution.costs and check == True:
            print('Hoi')
            current_solution = neighbour_solution
        elif acceptatie(current_solution, neighbour_solution, count, max_iterations):
            current_solution = neighbour_solution

        dataframe_row = spacefreight.save_iteration(current_solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)
        count += 1

    return iterations_dataframe, count, current_solution


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

def acceptatie(current_solution, neighbour_solution, count, max_iterations):
    """
    Returns True if neighbour solution gets accepted, False if not
    """
    # bereken verkorting
    verkorting = -1 * (neighbour_solution.costs - current_solution.costs)
    # bereken temperature
    temperature = cooling_scheme(count, max_iterations)

    # bereken acceptatiekans
    acceptatie_kans = math.exp(verkorting/temperature)
    # random number between 0 and 1
    random_number = random.random()
    # if random number
    if random_number < acceptatie_kans:
        return True
    else:
        return False


def cooling_scheme(count, max_iterations):
    """
    Returns the temperature
    """
    # LINEAIR

    # set begin temperature
    # heb nu aantal iteraties maar idk???
    T_0 = max_iterations
    T_N = 0

    T_i = T_0 - count * ( T_0 - T_N ) / max_iterations

    return T_i
