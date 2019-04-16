#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script contains the different versions (functions) of the random algorithms
"""
from spacefreight import SpaceFreight
import random

spacefreight = SpaceFreight()

def allocate_pseudo_random():
    """
    Random allocate the parcels in spacecrafts
    """
    # list with random numbers: order in which the parcels are being added
    parcel_randoms = random.sample(range(100), 100)
    # every single run of the function sets unpacked_parcels at starting point
    spacefreight.unpacked_parcels = []
    for p in spacefreight.all_parcels:
        spacefreight.unpacked_parcels.append(p.ID)

    # allocating the parcels
    for spacecraft in spacefreight.spacecrafts:
        spacecraft = spacefreight.spacecrafts[spacecraft]
        # set variables at 0 after run for every spacecraft
        spacecraft.packed_parcels = []
        spacecraft.packed_mass = 0
        spacecraft.packed_vol = 0
        for item in parcel_randoms:
            parcel = spacefreight.all_parcels[item]
            if spacefreight.check_mass(spacecraft, parcel) and spacefreight.check_vol(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacecraft, parcel)

    return len(spacefreight.unpacked_parcels)

def allocate_random():
    """
    Random allocate the parcels in spacecrafts
    """
    # list with random numbers: order in which the parcels and spacecrafts are being added
    parcel_randoms = random.sample(range(100), 100)
    spacecraft_randoms = random.sample(range(4), 4)
    # every single run of the function: set unpacked_parcels at starting point
    spacefreight.unpacked_parcels = []
    for p in spacefreight.all_parcels:
        spacefreight.unpacked_parcels.append(p.ID)

    for spacecraft_number in spacecraft_randoms:
        spacecraft_name = spacefreight.spacecrafts_names[spacecraft_number]
        spacecraft = spacefreight.spacecrafts[spacecraft_name]
        # set variables at 0
        spacecraft.packed_parcels = []
        spacecraft.packed_mass = 0
        spacecraft.packed_vol = 0
        for parcel_number in parcel_randoms:
            parcel = spacefreight.all_parcels[parcel_number]
            if spacefreight.check_mass(spacecraft, parcel) and spacefreight.check_vol(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacecraft, parcel)

    return len(spacefreight.unpacked_parcels)