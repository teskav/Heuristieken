# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script contains the different versions (functions)
of the HILL CLIMBER algorithms
"""

from spacefreight import SpaceFreight
from random_algorithms_new import *
from helpers import *
import random
import numpy as np
import copy

spacefreight = SpaceFreight()

def hill_climber(iterations_dataframe, max_iterations):
    """
    The hill climber algorithm swapping parcels.
    """
    count = 0
    costs_per_run = []

    # starting solution -> buiten hill climber
    current_solution = random_all_parcels()
    start_solution = copy.copy(current_solution)

    # select neighbouring solution
    while count < max_iterations:

        check, neighbour_solution = \
            neighbour_random_parcel_switch(current_solution)

        # compare costs & check if no error
        if neighbour_solution.costs < current_solution.costs and check == True:
            current_solution = neighbour_solution

        # save iteration to dataframe
        dataframe_row = spacefreight.save_iteration(current_solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, \
                                ignore_index=True)

        # save list with development of the costs per run
        costs_per_run.append(current_solution.costs)

        count += 1

    end_solution = current_solution

    return iterations_dataframe, start_solution, end_solution, costs_per_run

def hill_climber_spacecrafts(iterations_dataframe, max_iterations):
    """
    The hill climber algorithm swapping spacecrafts
    """
    count = 0
    costs_per_run = []

    # starting solution -> buiten hill climber
    current_solution = random_all_parcels()
    start_solution = copy.copy(current_solution)

    # select neighbouring solution
    while count < max_iterations:

        check, neighbour_solution = \
            neighbour_random_spacecraft_switch(current_solution)

        # compare costs & check of hij geen error geeft
        if neighbour_solution.costs < current_solution.costs and check == True:
            current_solution = neighbour_solution

        # save iteration to dataframe
        dataframe_row = spacefreight.save_iteration(current_solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, \
                                ignore_index=True)

        # save list with development of the costs per run
        costs_per_run.append(current_solution.costs)
        count += 1

    end_solution = current_solution

    return iterations_dataframe, start_solution, end_solution, costs_per_run

def hill_climber_combined(iterations_dataframe, max_iterations):
    """
    The hill climber algorithm swapping spacecrafts and parcels
    """
    count = 0
    solutions = []
    # starting solution -> buiten hill climber
    current_solution = random_all_parcels()

    # select neighbouring solution
    while count < max_iterations:

        # generate neighbour solution
        random_number = random.random()
        if random_number < 0.5:
            check, neighbour_solution = \
                neighbour_random_spacecraft_switch(current_solution)
        else:
            check, neighbour_solution = \
                neighbour_random_parcel_switch(current_solution)

        # compare costs & check of hij geen error geeft
        if neighbour_solution.costs < current_solution.costs and check == True:
            current_solution = neighbour_solution

        dataframe_row = spacefreight.save_iteration(current_solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, \
                                ignore_index=True)
        solutions.append(current_solution.costs)
        count += 1

    return iterations_dataframe, count, current_solution, solutions
