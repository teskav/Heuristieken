#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script contains the different versions (functions) of the random algorithms
Iteratief verbeterd
"""
from spacefreight import SpaceFreight
import random
import numpy as np

 # allowed number of parcels to leave behind
TARGET = 4

spacefreight = SpaceFreight()

def iterative_pseudo_random():
    """
    Random allocate the parcels in spacecrafts
    Optimize iterative
    """
    for spacecraft in spacefreight.spacecrafts:
        spacecraft = spacefreight.spacecrafts[spacecraft]
        # set variables at 0 after run for every spacecraft
        spacecraft.packed_parcels = []
        spacecraft.packed_mass = 0
        spacecraft.packed_vol = 0

    mean_mass = np.mean([parcel.mass for parcel in spacefreight.all_parcels])
    mean_vol = np.mean([parcel.volume for parcel in spacefreight.all_parcels])

    # list with random numbers: order in which the parcels are being added
    parcel_randoms = random.sample(range(100), 100)
    # every single run of the function sets unpacked_parcels at starting point
    spacefreight.unpacked_parcels = []
    for p in spacefreight.all_parcels:
        spacefreight.unpacked_parcels.append(p.ID)

    # allocate parcels with iterative constraints
    for item in parcel_randoms:
        parcel = spacefreight.all_parcels[item]
        if (parcel.mass < mean_mass) and (parcel.volume > mean_vol):
            if spacefreight.check_mass(spacefreight.spacecrafts['cygnus'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['cygnus'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts['cygnus'], parcel)
        if (parcel.mass > mean_mass) and (parcel.volume < mean_vol):
            if spacefreight.check_mass(spacefreight.spacecrafts['dragon'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['dragon'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts['dragon'], parcel)
        if (parcel.mass > mean_mass) and (parcel.volume > mean_vol):
            if spacefreight.check_mass(spacefreight.spacecrafts['kounotori'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['kounotori'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts['kounotori'], parcel)

    # allocating the rest of the parcels random
    for spacecraft in spacefreight.spacecrafts:
        spacecraft = spacefreight.spacecrafts[spacecraft]
        # set variables at 0 after run for every spacecraft
        # spacecraft.packed_parcels = []
        # spacecraft.packed_mass = 0
        # spacecraft.packed_vol = 0
        for item in parcel_randoms:
            parcel = spacefreight.all_parcels[item]
            if spacefreight.check_mass(spacecraft, parcel) and spacefreight.check_vol(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacecraft, parcel)

    if len(spacefreight.unpacked_parcels) <= TARGET:
        spacefreight.printing()
    # spacefreight.printing()

    return len(spacefreight.unpacked_parcels)
