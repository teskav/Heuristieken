# Heuristieken
# April - May 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script contains the different versions (functions) of the
SIMULATED ANNEALING algorithms.
"""

from spacefreight import SpaceFreight
from random_algorithms import *
from helpers import *
import random
import numpy as np
import copy
import math

spacefreight = SpaceFreight()


def simulated_annealing(iterations_dataframe, max_iterations, heuristic, cooling):
    """
    The simulated annealing algorithm swapping parcels.
    """
    # Set start variables
    count = 0
    costs_per_run = []

    # starting solution -> use random algorithm
    current_solution = random_algorithm()
    start_solution = copy.copy(current_solution)

    # select neighbouring solution
    while count < max_iterations:
        # generate neighbour solution
        if heuristic == 'parcels':
            check, neighbour_solution = \
                neighbour_random_parcel_switch(current_solution)
        elif heuristic == 'combined':
            # generate random number
            random_number = random.random()
            if random_number < 0.3:
                check, neighbour_solution = \
                    neighbour_random_spacecraft_switch(current_solution)
            else:
                check, neighbour_solution = \
                    neighbour_random_parcel_switch(current_solution)
        else:
            print("The neighbour solution is not an option.")
            exit()

        # get the temperature and the acceptance and generate a random number
        temperature, acceptance = acceptance_SA(current_solution, \
                                        neighbour_solution, count, \
                                        max_iterations, cooling)
        random_number = random.random()

        # compare costs & check if it is feasible solution
        if neighbour_solution.costs <= current_solution.costs and check == True:
            current_solution = neighbour_solution
            acceptance = 1
        elif random_number < acceptance and check == True:
            current_solution = neighbour_solution

        # save the iterations
        dataframe_row = spacefreight.save_iteration_SA(current_solution, count,\
                        temperature, acceptance)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, \
                                ignore_index=True)

        # save list with development of the costs per run
        costs_per_run.append(current_solution.costs)

        count += 1

    end_solution = current_solution

    return iterations_dataframe, start_solution, end_solution, costs_per_run

def simulated_annealing_fleet(iterations_dataframe, max_iterations, heuristic, cooling):
    """
    The simulated annealing algorithm swapping parcels.
    """
    # Set start variables
    count = 0
    costs_per_run = []

    # starting solution -> use random algorithm
    hoi = False
    while hoi == False:
        current_solution, hoi = random_fleet_algorithm()

    start_solution = copy.copy(current_solution)

    # select neighbouring solution
    while count < max_iterations:
        # generate neighbour solution
        if heuristic == 'parcels':
            check, neighbour_solution = \
                neighbour_random_parcel_switch(current_solution)
        elif heuristic == 'combined':
            # generate random number
            random_number = random.random()
            if random_number < 0.3:
                check, neighbour_solution = \
                    neighbour_random_spacecraft_switch(current_solution)
            else:
                check, neighbour_solution = \
                    neighbour_random_parcel_switch(current_solution)
        else:
            print("The neighbour solution is not an option.")
            exit()

        # get the temperature and the acceptance and generate a random number
        temperature, acceptance = acceptance_SA(current_solution, \
                                        neighbour_solution, count, \
                                        max_iterations, cooling)
        random_number = random.random()

        # compare costs & check if it is feasible solution
        if neighbour_solution.costs <= current_solution.costs and check == True:
            current_solution = neighbour_solution
            acceptance = 1
        elif random_number < acceptance and check == True:
            current_solution = neighbour_solution

        # save the iterations
        dataframe_row = spacefreight.save_iteration_SA(current_solution, count,\
                        temperature, acceptance)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, \
                                ignore_index=True)

        # save list with development of the costs per run
        costs_per_run.append(current_solution.costs)

        count += 1

    end_solution = current_solution

    return iterations_dataframe, start_solution, end_solution, costs_per_run
