#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script contains the different versions (functions) of the first fit algorithms
"""
from spacefreight import SpaceFreight

spacefreight = SpaceFreight()

def first_fit():
    """
    Allocate the parcels in spacecrafts
    """
    count = 0

    # go over list of spacecrafts and parcels and pack or not
    for spacecraft in spacefreight.spacecrafts:
        spacecraft = spacefreight.spacecrafts[spacecraft]
        for parcel in spacefreight.all_parcels:
            if spacefreight.check_mass(spacecraft, parcel) and spacefreight.check_vol(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacecraft, parcel)
                count += 1

def sorted_mass_first_fit():
    """
    Allocate the parcels in spacecrafts with a sorted list by mass
    """
    # sort the list by mass (reverse=true if you want big to small)
    sorted_mass = sorted(spacefreight.all_parcels, key=lambda x: x.mass)

    count = 0
    # go over list of spacecrafts and parcels and pack or not
    for spacecraft in spacefreight.spacecrafts:
        spacecraft = spacefreight.spacecrafts[spacecraft]
        for parcel in sorted_mass:
            if spacefreight.check_mass(spacecraft, parcel) and spacefreight.check_vol(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacecraft, parcel)
                count += 1

def sorted_vol_first_fit():
    """
    Allocate the parcels in spacecrafts with a sorted list by volume
    """
    # sort the list by mass (reverse=true if you want big to small)
    sorted_volume = sorted(spacefreight.all_parcels, key=lambda x: x.volume, reverse=True)

    count = 0
    # go over list of spacecrafts and parcels and pack or not
    for spacecraft in spacefreight.spacecrafts:
        spacecraft = spacefreight.spacecrafts[spacecraft]
        for parcel in sorted_volume:
            if spacefreight.check_mass(spacecraft, parcel) and spacefreight.check_vol(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacecraft, parcel)
                count += 1
