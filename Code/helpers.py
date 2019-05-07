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

def empty_spacecrafts(spacecrafts_list):
    """
    Set variables at 0 after run for every spacecraft
    """
    for spacecraft_number in spacecrafts_list:
        spacecraft = copy.copy(spacefreight.spacecrafts[spacecraft_number])
        spacecraft.packed_parcels = []
        spacecraft.packed_mass = 0
        spacecraft.packed_vol = 0

def empty_single_spacecraft(spacecraft_item):
    """
    Set variables at 0 after run for one spacecraft
    """
    spacecraft_item.packed_parcels = []
    spacecraft_item.packed_mass = 0
    spacecraft_item.packed_vol = 0

# # Deze werkt niet in de algoritmes zoals die nu is geschreven
# # misschien kunnen we hier samen naar kijken
def set_up_unpacked():
    unpacked = []
    for p in spacefreight.all_parcels:
        unpacked.append(p.ID)

    return unpacked

# # Deze geldt hetzelfde voor
def set_up_random():
    used_spacecrafts = []
    total_costs = 0
    parcel_randoms = random.sample(range(100), 100)
    spacecraft_randoms = random.sample(range(4), 4)

    return used_spacecrafts, total_costs, parcel_randoms, spacecraft_randoms
