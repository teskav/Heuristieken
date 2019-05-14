# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit

"""
This script contains the different versions (functions) of the random algorithms
"""

from spacefreight import SpaceFreight
from solution import Solution
from helpers import *
import random
import numpy as np
import copy

 # allowed number of parcels to leave behind
TARGETR = 4

spacefreight = SpaceFreight()

def random_greedy():
    """
    Random allocate the parcels in spacecrafts
    """
    # set starting settings random
    used_spacecrafts, total_costs, parcel_randoms, spacecraft_randoms = set_up_random()

    # every single run of the function: set unpacked_parcels at starting point
    spacefreight.unpacked_parcels = set_up_unpacked()

    for spacecraft_number in spacecraft_randoms:
        spacecraft = copy.copy(spacefreight.spacecrafts[spacecraft_number])

        # set variables at 0
        empty_single_spacecraft(spacecraft)

        for parcel_number in parcel_randoms:
            parcel = spacefreight.all_parcels[parcel_number]
            if spacefreight.check(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacecraft, parcel)

        # calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    # save solution
    current_solution = Solution('random', len(spacefreight.unpacked_parcels), spacefreight.unpacked_parcels, total_costs, used_spacecrafts)

    return current_solution

def random_constraints():
    """
    Random allocate the parcels in random spacecrafts with constraints
    """
    # set starting settings random
    used_spacecrafts, total_costs, parcel_randoms, spacecraft_randoms = set_up_random()

    # set variables at 0 after run for every spacecraft
    for spacecraft_number in spacecraft_randoms:
        spacecraft = spacefreight.spacecrafts[spacecraft_number]
        spacefreight.spacecrafts[spacecraft_number] = empty_single_spacecraft(spacecraft)

    # every single run of the function sets unpacked_parcels at starting point
    spacefreight.unpacked_parcels = set_up_unpacked()

    # allocate parcels with iterative constraints
    for parcel_number in parcel_randoms:
        parcel = spacefreight.all_parcels[parcel_number]
        for number in range(len(spacefreight.spacecrafts)):
            if check_constraints_spacecraft(parcel, number) == True and check_constraints(parcel, spacefreight, number) == True:
                spacefreight.update(spacefreight.spacecrafts[number], parcel)

    # allocating the rest of the parcels random
    for spacecraft_number in spacecraft_randoms:
        spacecraft = copy.copy(spacefreight.spacecrafts[spacecraft_number])
        # spacecraft = spacefreight.spacecrafts[spacecraft_number]
        for parcel_number in parcel_randoms:
            parcel = spacefreight.all_parcels[parcel_number]
            if spacefreight.check(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacecraft, parcel)
        #calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    # save solution
    current_solution = Solution('random constrained', len(spacefreight.unpacked_parcels), spacefreight.unpacked_parcels, total_costs, used_spacecrafts)

    return current_solution

def random_all_parcels():
    """
    Random allocate the parcels in spacecrafts
    """
    # set starting settings random
    used_spacecrafts, total_costs, parcel_randoms, spacecraft_randoms = set_up_random()

    # every single run of the function sets unpacked_parcels at starting point
    spacefreight.unpacked_parcels = set_up_unpacked()

    while len(spacefreight.unpacked_parcels) > 0:
        spacecraft = copy.copy(random.choice(spacefreight.spacecrafts))

        # set variables at 0
        empty_single_spacecraft(spacecraft)

        for parcel_number in parcel_randoms:
            parcel = spacefreight.all_parcels[parcel_number]
            if spacefreight.check(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacecraft = spacefreight.update(spacecraft, parcel)

        #calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    # save solution
    current_solution = Solution('random all', len(spacefreight.unpacked_parcels), spacefreight.unpacked_parcels, total_costs, used_spacecrafts)

    return current_solution

def random_constraints_all():
    """
    Random allocate the parcels in random spacecrafts with constraints
    """
    # set starting settings random
    used_spacecrafts, total_costs, parcel_randoms, spacecraft_randoms = set_up_random()

    # set variables at 0 after run for every spacecraft
    for spacecraft_number in spacecraft_randoms:
        spacecraft = spacefreight.spacecrafts[spacecraft_number]
        empty_single_spacecraft(spacecraft)

    # every single run of the function sets unpacked_parcels at starting point
    spacefreight.unpacked_parcels = set_up_unpacked()

    # allocate parcels with iterative constraints
    for parcel_number in parcel_randoms:
        parcel = spacefreight.all_parcels[parcel_number]
        for number in range(len(spacefreight.spacecrafts)):
            if check_constraints_spacecraft(parcel, number) == True and check_constraints(parcel, spacefreight, number) == True:
                spacefreight.update(spacefreight.spacecrafts[number], parcel)

    # allocating the rest of the parcels random
    for spacecraft_number in spacecraft_randoms:
        spacecraft = copy.copy(spacefreight.spacecrafts[spacecraft_number])
        for parcel_number in parcel_randoms:
            parcel = spacefreight.all_parcels[parcel_number]
            if spacefreight.check(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacecraft, parcel)
        #calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    while len(spacefreight.unpacked_parcels) > 0:
        spacecraft = copy.copy(random.choice(spacefreight.spacecrafts))

        # set variables at 0
        empty_single_spacecraft(spacecraft)
        for parcel_number in parcel_randoms:
            parcel = spacefreight.all_parcels[parcel_number]
            if spacefreight.check(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacecraft = spacefreight.update(spacecraft, parcel)

        #calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    # save solution
    current_solution = Solution('constraints all', len(spacefreight.unpacked_parcels), spacefreight.unpacked_parcels, total_costs, used_spacecrafts)

    return current_solution
