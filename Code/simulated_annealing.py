# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script contains the different versions (functions) of the
SIMULATED ANNEALING algorithms
"""

from spacefreight import SpaceFreight
from random_algorithms_new import *
from helpers import *
import random
import numpy as np
import copy
import math

spacefreight = SpaceFreight()


def simulated_annealing(iterations_dataframe, max_iterations):
    """
    The simulated annealing algorithm swapping parcels.
    """
    count = 0
    costs_per_run = []

    # starting solution -> buiten hill climber
    current_solution = random_all_parcels()
    start_solution = copy.copy(current_solution)

    # select neighbouring solution
    while count < max_iterations:
        # Generate neighbour solution
        check, neighbour_solution = \
            neighbour_random_parcel_switch(current_solution)
        # print(check)
        # print(neighbour_solution.costs)
        # print(current_solution.costs)

        # get the temperature and the acceptance and generate a random number
        temperature, acceptance = acceptance_SA(current_solution, \
                                        neighbour_solution, count, \
                                        max_iterations)
        random_number = random.random()
        # print('Random number: ', random_number)
        # print('Acceptatie kans: ', acceptatie_kans)
        # print('Temperatuur: ', temperature)

        # compare costs & check of hij geen error geeft
        if neighbour_solution.costs <= current_solution.costs and check == True:
            current_solution = neighbour_solution
            acceptance = 1
        elif random_number < acceptance and check == True:
            current_solution = neighbour_solution
        # elif acceptatie(current_solution, neighbour_solution, count, max_iterations):
        #     print('Doei')
        #     current_solution = neighbour_solution

        dataframe_row = spacefreight.save_iteration_SA(current_solution, count,\
                        temperature, acceptance)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, \
                                ignore_index=True)

        # save list with development of the costs per run
        costs_per_run.append(current_solution.costs)

        count += 1

    end_solution = current_solution

    return iterations_dataframe, start_solution, end_solution, costs_per_run
