# HEURISTIEKEN
# April - Mei 2019
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
    Set variables at 0 after run for one spacecraft
    """
    spacecraft_item.packed_parcels = []
    spacecraft_item.packed_mass = 0
    spacecraft_item.packed_vol = 0

    return spacecraft_item

def set_up_unpacked():
    """
    Update unpacked parcels
    """
    unpacked = []
    for p in spacefreight.all_parcels:
        unpacked.append(p.ID)

    return unpacked

def set_up_random():
    """
    Set up random algorithms, draws random numbers for spacecrafts and parcels
    """
    used_spacecrafts = []
    total_costs = 0
    parcel_randoms = random.sample(range(len(spacefreight.all_parcels)), \
                        len(spacefreight.all_parcels))
    spacecraft_randoms = random.sample(range(len(spacefreight.spacecrafts)), \
                            len(spacefreight.spacecrafts))

    return used_spacecrafts, total_costs, parcel_randoms, spacecraft_randoms

# deze gebruiken we (nog) niet
# def allocate_random(spacecraft_randoms, parcel_randoms, used_spacecrafts, \
#                     total_costs):
#     """
#     Allocating the rest of the parcels random
#     """
#     for spacecraft_number in spacecraft_randoms:
#         spacecraft = spacefreight.spacecrafts[spacecraft_number]
#         print(spacecraft.packed_mass)
#         for parcel_number in parcel_randoms:
#             parcel = spacefreight.all_parcels[parcel_number]
#             if (spacefreight.check(spacecraft, parcel) and
#                     parcel.ID in spacefreight.unpacked_parcels):
#                 spacefreight.update(spacecraft, parcel)
#                 # print(spacecraft.packed_mass)
#         parcels = []
#         for parcel in spacecraft.packed_parcels:
#             parcels.append(parcel.ID)
#
#         # print(parcels)
#         # print(spacecraft.packed_parcels)
#         # print(spacecraft.packed_mass)
#
#         #calculate costs spacecraft
#         spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
#         total_costs += spacecraft.costs
#
#         # add spacecraft to used_spacecrafts
#         used_spacecrafts.append(spacecraft)
#
#     # for s in used_spacecrafts:
#     #     print(s)
#
#     return used_spacecrafts, total_costs

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
    # bij simulated annealing is het dit
    # if spacecraft_1 == spacecraft_2 and parcel_1 == parcel_2:
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
    Returns the neighbouring solution in a Solution class
    """
    neighbour_solution = copy.deepcopy(current_solution)
    # selecting the spacecraft
    spacecraft_1 = random.choice(neighbour_solution.used_spacecrafts)
    spacecraft_2 = copy.copy(random.choice(spacefreight.spacecrafts))

    # Swap the payload of spacecraft 1 to spacecraft 2
    spacecraft_new = spacefreight.swap_spacecraft(spacecraft_1, spacecraft_2)

    # check if the spacecrafts are not the same
    if spacecraft_1.name == spacecraft_new.name:
        return False, current_solution
    elif (spacecraft_new.payload_vol >= spacecraft_new.packed_vol and
            spacecraft_new.payload_mass >= spacecraft_new.packed_mass):
        check = True
        # Remove old spacecraft from used spacecrafts and
        # add the new spacecraft
        neighbour_solution.used_spacecrafts.remove(spacecraft_1)
        neighbour_solution.used_spacecrafts.append(spacecraft_new)
        # update costs
        neighbour_solution.costs = \
            spacefreight.calculate_costs(neighbour_solution)
        return check, neighbour_solution
    elif (spacecraft_new.payload_vol < spacecraft_new.packed_vol or
            spacecraft_new.payload_mass < spacecraft_new.packed_mass):
        return False, current_solution

def cooling_scheme(count, max_iterations):
    """
    Returns the temperature
    """

    # Set begin temperature and end temperature based on maximal and minimal
    # differences in costs caused by a parcel switch with hill climber.
    # Instead of using the minimum of 0, we use the second minimum greater
    # than 0, since this is no improvement.
    T_0 = 12286
    T_N = 382

    # LINEAIR
    # T_i = T_0 - count * ( T_0 - T_N ) / max_iterations

    # EXPONENTIAL
    T_i = T_0 * (T_N / T_0) ** (count / max_iterations)

    # SIGMOIDAL
    # T_i = T_N + (T_0 - T_N) / (1 + math.exp(0.3 * (count - max_iterations / 2)))

    return T_i

def acceptance_SA(current_solution, neighbour_solution, count, max_iterations):
    """
    Returns True if neighbour solution gets accepted, False if not
    """
    # bereken verkorting
    verkorting = current_solution.costs - neighbour_solution.costs

    # bereken temperature
    temperature = cooling_scheme(count, max_iterations)

    # bereken acceptatiekans
    acceptance = math.exp(verkorting/temperature)

    return temperature, acceptance
