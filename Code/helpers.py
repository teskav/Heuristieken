# HEURISTIEKEN
# April - May 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script contains helping functions for different algorithms
"""

from spacefreight import SpaceFreight
from solution import Solution
import random
import numpy as np
import copy
import math

spacefreight = SpaceFreight()

# the means of the volumes and the masses
mean_mass = np.mean([parcel.mass for parcel in spacefreight.all_parcels])
mean_vol = np.mean([parcel.volume for parcel in spacefreight.all_parcels])

def empty_single_spacecraft(spacecraft_item):
    """
    Sets variables at 0 after run for one spacecraft and returns spacecraft.
    """
    spacecraft_item.packed_parcels = []
    spacecraft_item.packed_mass = 0
    spacecraft_item.packed_vol = 0

    return spacecraft_item

def set_up_unpacked():
    """
    Updates and returns list of unpacked parcels.
    """
    unpacked = []
    for p in spacefreight.all_parcels:
        unpacked.append(p.ID)

    return unpacked

def set_up_random():
    """
    Sets up random algorithms, draws random numbers for spacecrafts and parcels.
    """
    used_spacecrafts = []
    total_costs = 0
    parcel_randoms = random.sample(range(len(spacefreight.all_parcels)), \
                        len(spacefreight.all_parcels))
    spacecraft_randoms = random.sample(range(len(spacefreight.spacecrafts)), \
                            len(spacefreight.spacecrafts))

    return used_spacecrafts, total_costs, parcel_randoms, spacecraft_randoms

def check_constraints_spacecraft(parcel, number):
    """
    Checks the constraint for respectively Cygnus, Progress, Kounotori, Dragon,
    TianZhou and Verne ATV
    """
    if number == 0:
        # very light-weight and very big
        return ((parcel.mass < (mean_mass/2)) and (parcel.volume > mean_vol*2))
    elif number == 1:
        # light-weight and very small
        return ((parcel.mass < mean_mass) and (parcel.volume < (mean_vol/2)))
    elif number == 2:
        # heavy and big
        return ((parcel.mass > mean_mass) and (parcel.volume > mean_vol))
    elif number == 3:
        # heavy and small
        return ((parcel.mass > mean_mass) and (parcel.volume < mean_vol))
    elif number == 4:
        # very heavy and big
        return ((parcel.mass > mean_mass*2) and (parcel.volume > mean_vol))
    elif number == 5:
        # very heavy and very big
        return ((parcel.mass > mean_mass*2) and (parcel.volume > mean_vol*2))

def check_constraints(parcel, spacefreight, number):
    """
    Checks if parcel fits in a particular spacecraft and is not yet packed
    """
    return (spacefreight.check(spacefreight.spacecrafts[number], parcel) and
            parcel.ID in spacefreight.unpacked_parcels)

def neighbour_random_parcel_switch(current_solution):
    """
    Returns the neighbouring solution of parcel swap in a Solution class.
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
        check = spacefreight.swap_parcel(spacecraft_1, spacecraft_2, \
                parcel_1, parcel_2)
        # update costs
        neighbour_solution.costs = \
            spacefreight.calculate_costs(neighbour_solution)

    # switch parcels in spacecraft
    return check, neighbour_solution

def neighbour_random_spacecraft_switch(current_solution):
    """
    Returns the neighbouring solution of spacecraft swap in a Solution class.
    """
    neighbour_solution = copy.deepcopy(current_solution)
    # selecting the spacecraft
    spacecraft_1 = random.choice(neighbour_solution.used_spacecrafts)
    spacecraft_2 = copy.copy(random.choice(spacefreight.spacecrafts))

    # swap the payload of spacecraft 1 to spacecraft 2
    spacecraft_new = spacefreight.swap_spacecraft(spacecraft_1, spacecraft_2)

    # check if the spacecrafts are not the same
    if spacecraft_1.name == spacecraft_new.name:
        return False, current_solution
    elif (spacecraft_new.payload_vol >= spacecraft_new.packed_vol and
            spacecraft_new.payload_mass >= spacecraft_new.packed_mass):
        check = True
        # Remove old spacecraft from used spacecrafts and add new spacecraft
        neighbour_solution.used_spacecrafts.remove(spacecraft_1)
        neighbour_solution.used_spacecrafts.append(spacecraft_new)
        # update costs
        neighbour_solution.costs = \
            spacefreight.calculate_costs(neighbour_solution)
        return check, neighbour_solution
    elif (spacecraft_new.payload_vol < spacecraft_new.packed_vol or
            spacecraft_new.payload_mass < spacecraft_new.packed_mass):
        return False, current_solution

def cooling_scheme(count, max_iterations, cooling):
    """
    Calculates and returns the temperature.
    """
    # set begin temperature based on mean difference in costs caused by a run
    # of parcel switches with hill climber
    T_0 = 325819
    T_N = 1

    if cooling == 'lineair':
        # LINEAIR
        T_i = T_0 - count * ( T_0 - T_N ) / max_iterations
    elif cooling == 'exponential':
        # EXPONENTIAL
        T_i = T_0 * (T_N / T_0) ** (count / max_iterations)
    elif cooling == 'sigmoidal':
        # SIGMOIDAL
        T_i = T_N + (T_0 - T_N) / (1 + math.exp(0.3 * (count - max_iterations / 2)))
    else:
        print("This is not an option.")
        exit()

    return T_i

def acceptance_SA(current_solution, neighbour_solution, count, max_iterations, cooling):
    """
    Calculates the acceptance probability of a neighbour solution.
    Returns the temperature and the acceptance probability.
    """
    # calculate change in costs
    change = current_solution.costs - neighbour_solution.costs

    # calculate temperature
    temperature = cooling_scheme(count, max_iterations, cooling)

    # calculate acceptance probability
    try:
        acceptance = math.exp(change/temperature)
    except OverflowError:
        acceptance = float('inf')

    return temperature, acceptance
