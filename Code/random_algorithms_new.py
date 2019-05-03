#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script contains the different versions (functions) of the random algorithms
"""
from spacefreight import SpaceFreight
from solution import Solution
import random
import numpy as np
import copy

 # allowed number of parcels to leave behind
TARGETR = 4

spacefreight = SpaceFreight()

# the means of the volumes and the masses
mean_mass = np.mean([parcel.mass for parcel in spacefreight.all_parcels])
mean_vol = np.mean([parcel.volume for parcel in spacefreight.all_parcels])

def random_greedy():
    """
    Random allocate the parcels in spacecrafts
    """
    used_spacecrafts = []
    total_costs = 0
    # list with random numbers: order in which the parcels and spacecrafts are being added
    parcel_randoms = random.sample(range(100), 100)
    spacecraft_randoms = random.sample(range(4), 4)
    # every single run of the function: set unpacked_parcels at starting point
    spacefreight.unpacked_parcels = []
    for p in spacefreight.all_parcels:
        spacefreight.unpacked_parcels.append(p.ID)

    for spacecraft_number in spacecraft_randoms:
        spacecraft = spacefreight.spacecrafts[spacecraft_number]

        # set variables at 0
        spacecraft.packed_parcels = []
        spacecraft.packed_mass = 0
        spacecraft.packed_vol = 0
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
    current_solution = Solution(len(spacefreight.unpacked_parcels), spacefreight.unpacked_parcels, total_costs, used_spacecrafts)

    if len(spacefreight.unpacked_parcels) <= TARGETR:
        spacefreight.printing(current_solution)

    return current_solution

def random_constraints():
    """
    Random allocate the parcels in random spacecrafts with constraints
    """
    used_spacecrafts = []
    total_costs = 0

    spacecraft_randoms = random.sample(range(4), 4)

    # set variables at 0 after run for every spacecraft
    for spacecraft_number in spacecraft_randoms:
        spacecraft = spacefreight.spacecrafts[spacecraft_number]
        spacecraft.packed_parcels = []
        spacecraft.packed_mass = 0
        spacecraft.packed_vol = 0

    # list with random numbers: order in which the parcels are being added
    parcel_randoms = random.sample(range(100), 100)
    # every single run of the function sets unpacked_parcels at starting point
    spacefreight.unpacked_parcels = []
    for p in spacefreight.all_parcels:
        spacefreight.unpacked_parcels.append(p.ID)

    # allocate parcels with iterative constraints
    for parcel_number in parcel_randoms:
        parcel = spacefreight.all_parcels[parcel_number]
        if (parcel.mass < mean_mass) and (parcel.volume > mean_vol):
            if spacefreight.check(spacefreight.spacecrafts[0], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts[0], parcel)
        if (parcel.mass < (mean_mass / 2)) and (parcel.volume < mean_vol):
            if spacefreight.check(spacefreight.spacecrafts[1], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts[1], parcel)
        if (parcel.mass > mean_mass) and (parcel.volume > mean_vol):
            if spacefreight.check(spacefreight.spacecrafts[2], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts[2], parcel)
        if (parcel.mass > mean_mass) and (parcel.volume < mean_vol):
            if spacefreight.check(spacefreight.spacecrafts[3], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts[3], parcel)

    # allocating the rest of the parcels random
    for spacecraft_number in spacecraft_randoms:
        spacecraft = spacefreight.spacecrafts[spacecraft_number]
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
    current_solution = Solution(len(spacefreight.unpacked_parcels), spacefreight.unpacked_parcels, total_costs, used_spacecrafts)

    if len(spacefreight.unpacked_parcels) <= TARGETR:
        spacefreight.printing(current_solution)

    return current_solution

def random_all_parcels():
    """
    Random allocate the parcels in spacecrafts
    """
    used_spacecrafts = []
    total_costs = 0
    # list with random numbers: order in which the parcels and spacecrafts are being added
    parcel_randoms = random.sample(range(100), 100)
    spacecraft_randoms = random.sample(range(4), 4)
    # every single run of the function: set unpacked_parcels at starting point
    spacefreight.unpacked_parcels = []
    for p in spacefreight.all_parcels:
        spacefreight.unpacked_parcels.append(p.ID)

    while len(spacefreight.unpacked_parcels) > 0:
        spacecraft = copy.copy(random.choice(spacefreight.spacecrafts))

        # set variables at 0
        spacecraft.packed_parcels = []
        spacecraft.packed_mass = 0
        spacecraft.packed_vol = 0
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
    current_solution = Solution(len(spacefreight.unpacked_parcels), spacefreight.unpacked_parcels, total_costs, used_spacecrafts)

    return current_solution

def random_constraints_all():
    """
    Random allocate the parcels in random spacecrafts with constraints
    """
    used_spacecrafts = []
    total_costs = 0

    spacecraft_randoms = random.sample(range(4), 4)

    # set variables at 0 after run for every spacecraft
    for spacecraft_number in spacecraft_randoms:
        spacecraft = spacefreight.spacecrafts[spacecraft_number]
        spacecraft.packed_parcels = []
        spacecraft.packed_mass = 0
        spacecraft.packed_vol = 0

    # list with random numbers: order in which the parcels are being added
    parcel_randoms = random.sample(range(100), 100)
    # every single run of the function sets unpacked_parcels at starting point
    spacefreight.unpacked_parcels = []
    for p in spacefreight.all_parcels:
        spacefreight.unpacked_parcels.append(p.ID)

    # allocate parcels with iterative constraints
    for parcel_number in parcel_randoms:
        parcel = spacefreight.all_parcels[parcel_number]
        if (parcel.mass < mean_mass) and (parcel.volume > mean_vol):
            if spacefreight.check(spacefreight.spacecrafts[0], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts[0], parcel)
        if (parcel.mass < (mean_mass / 2)) and (parcel.volume < mean_vol):
            if spacefreight.check(spacefreight.spacecrafts[1], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts[1], parcel)
        if (parcel.mass > mean_mass) and (parcel.volume > mean_vol):
            if spacefreight.check(spacefreight.spacecrafts[2], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts[2], parcel)
        if (parcel.mass > mean_mass) and (parcel.volume < mean_vol):
            if spacefreight.check(spacefreight.spacecrafts[3], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts[3], parcel)

    # allocating the rest of the parcels random
    for spacecraft_number in spacecraft_randoms:
        spacecraft = spacefreight.spacecrafts[spacecraft_number]
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
        spacecraft.packed_parcels = []
        spacecraft.packed_mass = 0
        spacecraft.packed_vol = 0
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
    current_solution = Solution(len(spacefreight.unpacked_parcels), spacefreight.unpacked_parcels, total_costs, used_spacecrafts)

    return current_solution
