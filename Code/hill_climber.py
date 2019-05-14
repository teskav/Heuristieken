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

def hill_climber_spacecrafts(iterations_dataframe, max_iterations):
    count = 0
    solutions = []
    # starting solution -> buiten hill climber
    current_solution = random_all_parcels()

    # select neighbouring solution
    while count < max_iterations:

        check, neighbour_solution = neighbour_random_spacecraft_switch(current_solution)
        # print(check)
        # print(neighbour_solution.costs)
        # print(current_solution.costs)

        # compare costs & check of hij geen error geeft
        if neighbour_solution.costs < current_solution.costs and check == True:
            current_solution = neighbour_solution

        dataframe_row = spacefreight.save_iteration(current_solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)
        solutions.append(current_solution.costs)
        count += 1

        # print("Iterations:", count)
        # spacefreight.printing(current_solution)

    return iterations_dataframe, count, current_solution, solutions

def hill_climber_combined(iterations_dataframe, max_iterations):
    count = 0
    solutions = []
    # starting solution -> buiten hill climber
    current_solution = random_all_parcels()

    # select neighbouring solution
    while count < max_iterations:

        # generate neighbour solution
        random_number = random.random()
        if random_number < 0.5:
            print('Neighbour: spacecraft')
            check, neighbour_solution = neighbour_random_spacecraft_switch(current_solution)
        else:
            print('Neighbour: parcel')
            check, neighbour_solution = neighbour_random_parcel_switch(current_solution)

        print(check)
        print(neighbour_solution.costs)
        print(current_solution.costs)

        # compare costs & check of hij geen error geeft
        if neighbour_solution.costs < current_solution.costs and check == True:
            current_solution = neighbour_solution

        dataframe_row = spacefreight.save_iteration(current_solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)
        solutions.append(current_solution.costs)
        count += 1

        # print("Iterations:", count)
        # spacefreight.printing(current_solution)

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

    # check if the spacecrafts where the swap takes place are not the same
    if spacecraft_1 == spacecraft_2:
        return False, current_solution
    else:
        check = spacefreight.swap_parcel(spacecraft_1, spacecraft_2, parcel_1, parcel_2)
        # update costs
        neighbour_solution.costs = spacefreight.calculate_costs(neighbour_solution)

    # switch parcels in spacecraft
    return check, neighbour_solution

def neighbour_random_spacecraft_switch(current_solution):
    """
    Returns the neighbouring solution in a Solution class
    """
    neighbour_solution = copy.deepcopy(current_solution) # vgm moet dit dus deepcopy omdat we een lijst in een lijst gaan gebruiken
    # selecting the spacecraft
    spacecraft_1 = random.choice(neighbour_solution.used_spacecrafts)
    spacecraft_2 = copy.copy(random.choice(spacefreight.spacecrafts))

    # Swap the payload of spacecraft 1 to spacecraft 2
    spacecraft_new = spacefreight.swap_spacecraft(spacecraft_1, spacecraft_2)

    # check if the spacecrafts are not the same
    if spacecraft_1.name == spacecraft_new.name:
        return False, current_solution
    elif spacecraft_new.payload_vol >= spacecraft_new.packed_vol and spacecraft_new.payload_mass >= spacecraft_new.packed_mass:
        check = True
        # Remove old spacecraft from used spacecrafts and add the new spacecraft
        neighbour_solution.used_spacecrafts.remove(spacecraft_1)
        neighbour_solution.used_spacecrafts.append(spacecraft_new)
        # update costs
        neighbour_solution.costs = spacefreight.calculate_costs(neighbour_solution)
        return check, neighbour_solution
    # volgens mij kan dit gewoon zijn:
    # else:
    #     return False, current_solution
    elif spacecraft_new.payload_vol < spacecraft_new.packed_vol or spacecraft_new.payload_mass < spacecraft_new.packed_mass:
        return False, current_solution

    # else:
    #     check = spacefreight.swap_spacecraft(spacecraft_1, spacecraft_2)
    #     neighbour_solution.used_spacecrafts.remove(spacecraft_1)
    #     neighbour_solution.used_spacecrafts.add(spacecraft_2)
    #     neighbour_solution.costs = spacefreight.calculate_costs(neighbour_solution)
    #     return check, neighbour_solution

    # return neighbour solution
    # return check, neighbour_solution
