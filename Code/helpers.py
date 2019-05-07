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

def empty_single_spacecraft(spacecraft_item):
    """
    Set variables at 0 after run for one spacecraft
    """
    spacecraft_item.packed_parcels = []
    spacecraft_item.packed_mass = 0
    spacecraft_item.packed_vol = 0

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
        for parcel_number in parcel_randoms:
            parcel = spacefreight.all_parcels[parcel_number]
            if spacefreight.check(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacecraft, parcel)
        #calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    return used_spacecrafts

# def iterative_constraints():
#     pass
