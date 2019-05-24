# HEURISTIEKEN
# April - May 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script contains the different versions (functions)
of the HILL CLIMBER algorithms
"""

from spacefreight import SpaceFreight
from random_algorithms import *
from helpers import *
import random
import numpy as np
import copy

spacefreight = SpaceFreight()

def hill_climber(iterations_dataframe, max_iterations, heuristic):
    """
    The hill climber algorithm.
    """
    count = 0
    costs_per_run = []

    # starting solution is random
    current_solution = random_algorithm()
    start_solution = copy.copy(current_solution)

    # select neighbour solution
    while count < max_iterations:
        if heuristic == 'parcels':
            check, neighbour_solution = \
                neighbour_random_parcel_switch(current_solution)
        elif heuristic == 'spacecrafts':
            check, neighbour_solution = \
                neighbour_random_spacecraft_switch(current_solution)
        elif heuristic == 'combined':
            # generate random number
            random_number = random.random()
            if random_number < 0.5:
                check, neighbour_solution = \
                    neighbour_random_spacecraft_switch(current_solution)
            else:
                check, neighbour_solution = \
                    neighbour_random_parcel_switch(current_solution)
        else:
            print("This is not an option.")
            exit()

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
