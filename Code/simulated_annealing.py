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
    The simulated annealing algorithm swapping
    """
    count = 0
    # starting solution -> buiten hill climber
    current_solution = random_all_parcels()

    # select neighbouring solution
    while count < max_iterations:
        # Generate neighbour solution
        check, neighbour_solution = \
            neighbour_random_parcel_switch_SA(current_solution)
        # print(check)
        # print(neighbour_solution.costs)
        # print(current_solution.costs)

        # get the temperature and the acceptatie kans and generate a random number
        temperature, acceptatie_kans = acceptatie(current_solution, \
                                        neighbour_solution, count, \
                                        max_iterations)
        random_number = random.random()
        # print('Random number: ', random_number)
        # print('Acceptatie kans: ', acceptatie_kans)
        # print('Temperatuur: ', temperature)

        # compare costs & check of hij geen error geeft
        if neighbour_solution.costs <= current_solution.costs and check == True:
            current_solution = neighbour_solution
            acceptatie_kans = None
        elif random_number < acceptatie_kans and check == True:
            current_solution = neighbour_solution
        # elif acceptatie(current_solution, neighbour_solution, count, max_iterations):
        #     print('Doei')
        #     current_solution = neighbour_solution

        dataframe_row = spacefreight.save_iteration_SA(current_solution, count,\
                        temperature, acceptatie_kans)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, \
                                ignore_index=True)
        count += 1

    return iterations_dataframe, count, current_solution

def simulated_annealing_combined(iterations_dataframe, max_iterations):
    count = 0
    # starting solution -> buiten hill climber
    current_solution = random_all_parcels()

    # select neighbouring solution
    while count < max_iterations:
        # Generate neighbour solution
        random_number = random.random()
        if random_number < 0.3:
            print('Neighbor: spacecraft')
            check, neighbour_solution = \
                neighbour_random_spacecraft_switch(current_solution)
        else:
            print('Neighbor: parcel')
            check, neighbour_solution = \
                neighbour_random_parcel_switch_SA(current_solution)
        print(check)
        print(neighbour_solution.costs)
        print(current_solution.costs)

        # get the temperature and the acceptatie kans and
        # generate a random number
        temperature, acceptatie_kans = acceptatie(current_solution, \
                                        neighbour_solution, count, \
                                        max_iterations)
        random_number = random.random()
        print('Random number: ', random_number)
        print('Acceptatie kans: ', acceptatie_kans)
        print('Temperatuur: ', temperature)

        # compare costs & check of hij geen error geeft
        if neighbour_solution.costs <= current_solution.costs and check == True:
            print('Hoi')
            current_solution = neighbour_solution
            acceptatie_kans = None
        elif random_number < acceptatie_kans and check == True:
            print('Doei')
            current_solution = neighbour_solution
        # elif acceptatie(current_solution, neighbour_solution, count, max_iterations):
        #     print('Doei')
        #     current_solution = neighbour_solution

        dataframe_row = spacefreight.save_iteration_SA(current_solution, \
                        count, temperature, acceptatie_kans)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, \
                                ignore_index=True)
        count += 1

    return iterations_dataframe, count, current_solution
