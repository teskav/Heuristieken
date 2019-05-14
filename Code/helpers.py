#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script contains helping functions for different algorithms
"""
from spacefreight import SpaceFreight
from solution import Solution
import random
import numpy as np
import copy

spacefreight = SpaceFreight()

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
    parcel_randoms = random.sample(range(len(spacefreight.all_parcels)), len(spacefreight.all_parcels))
    spacecraft_randoms = random.sample(range(len(spacefreight.spacecrafts)), len(spacefreight.spacecrafts))

    return used_spacecrafts, total_costs, parcel_randoms, spacecraft_randoms

def allocate_random(spacecraft_randoms, parcel_randoms, used_spacecrafts, total_costs):
    """
    Allocating the rest of the parcels random
    """
    for spacecraft_number in spacecraft_randoms:
        spacecraft = spacefreight.spacecrafts[spacecraft_number]
        print(spacecraft.packed_mass)
        for parcel_number in parcel_randoms:
            parcel = spacefreight.all_parcels[parcel_number]
            if spacefreight.check(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacecraft, parcel)
                # print(spacecraft.packed_mass)
        parcels = []
        for parcel in spacecraft.packed_parcels:
            parcels.append(parcel.ID)

        # print(parcels)
        # print(spacecraft.packed_parcels)
        # print(spacecraft.packed_mass)

        #calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    # for s in used_spacecrafts:
    #     print(s)

    return used_spacecrafts, total_costs

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
    return (spacefreight.check(spacefreight.spacecrafts[number], parcel) and parcel.ID in spacefreight.unpacked_parcels)
