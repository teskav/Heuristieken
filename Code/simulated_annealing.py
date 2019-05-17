# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
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
    """
    The simulated annealing algorithm swapping
    """
    count = 0
    # starting solution -> buiten hill climber
    current_solution = random_all_parcels()

    # select neighbouring solution
    while count < max_iterations:
        # Generate neighbour solution
        check, neighbour_solution = neighbour_random_parcel_switch(current_solution)
        # print(check)
        # print(neighbour_solution.costs)
        # print(current_solution.costs)

        # get the temperature and the acceptatie kans and generate a random number
        temperature, acceptatie_kans = acceptatie(current_solution, neighbour_solution, count, max_iterations)
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

        dataframe_row = spacefreight.save_iteration_SA(current_solution, count, temperature, acceptatie_kans)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)
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
            check, neighbour_solution = neighbour_random_spacecraft_switch(current_solution)
        else:
            print('Neighbor: parcel')
            check, neighbour_solution = neighbour_random_parcel_switch(current_solution)
        print(check)
        print(neighbour_solution.costs)
        print(current_solution.costs)

        # get the temperature and the acceptatie kans and generate a random number
        temperature, acceptatie_kans = acceptatie(current_solution, neighbour_solution, count, max_iterations)
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

        dataframe_row = spacefreight.save_iteration_SA(current_solution, count, temperature, acceptatie_kans)
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
    elif spacecraft_new.payload_vol < spacecraft_new.packed_vol or spacecraft_new.payload_mass < spacecraft_new.packed_mass:
        return False, current_solution

def acceptatie(current_solution, neighbour_solution, count, max_iterations):
    """
    Returns True if neighbour solution gets accepted, False if not
    """
    # bereken verkorting
    verkorting = current_solution.costs - neighbour_solution.costs
    # bereken temperature
    temperature = cooling_scheme(count, max_iterations)

    # bereken acceptatiekans
    acceptatie_kans = math.exp(verkorting/temperature)

    return temperature, acceptatie_kans

    # # random number between 0 and 1
    # random_number = random.random()
    # # if random number
    # if random_number < acceptatie_kans:
    #     return True
    # else:
    #     return False


def cooling_scheme(count, max_iterations):
    """
    Returns the temperature
    """

    # set begin temperature and end temperature
    # heb nu temperatuur bepaald over wat ze in college zeiden
    T_0 = 15000
    T_N = 1

    # LINEAIR
    # T_i = T_0 - count * ( T_0 - T_N ) / max_iterations

    # EXPONENTIAL
    # T_i = T_0 * (T_N / T_0) ** (count / max_iterations)

    # SIGMOIDAL
    T_i = T_N + (T_0 - T_N) / (1 + math.exp(0.3 * (count - max_iterations / 2)))

    return T_i
