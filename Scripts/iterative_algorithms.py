#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script contains the different versions (functions) of the random algorithms
Iteratief verbeterd
"""
from spacefreight import SpaceFreight
import random
import numpy as np
import copy

spacefreight = SpaceFreight()

 # allowed number of parcels to leave behind
TARGETI = 4

# the means of the volumes and the masses
mean_mass = np.mean([parcel.mass for parcel in spacefreight.all_parcels])
mean_vol = np.mean([parcel.volume for parcel in spacefreight.all_parcels])

def iterative_pseudo_random():
    """
    Random allocate the parcels in spacecrafts
    Optimize iterative
    """
    # set variables at 0 after run for every spacecraft
    for spacecraft in spacefreight.spacecrafts:
        spacecraft = spacefreight.spacecrafts[spacecraft]
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
    for item in parcel_randoms:
        parcel = spacefreight.all_parcels[item]
        if (parcel.mass < mean_mass) and (parcel.volume > mean_vol):
            if spacefreight.check_mass(spacefreight.spacecrafts['cygnus'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['cygnus'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts['cygnus'], parcel)
        if (parcel.mass > mean_mass) and (parcel.volume < mean_vol):
            if spacefreight.check_mass(spacefreight.spacecrafts['dragon'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['dragon'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts['dragon'], parcel)
        if (parcel.mass > mean_mass + 30) and (parcel.volume > mean_vol):
            if spacefreight.check_mass(spacefreight.spacecrafts['kounotori'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['kounotori'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts['kounotori'], parcel)
        if (parcel.mass < (mean_mass / 2)) and (parcel.volume < mean_vol):
            if spacefreight.check_mass(spacefreight.spacecrafts['progress'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['progress'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacefreight.spacecrafts['progress'], parcel)

    # allocating the rest of the parcels random
    for spacecraft in spacefreight.spacecrafts:
        spacecraft = spacefreight.spacecrafts[spacecraft]
        for item in parcel_randoms:
            parcel = spacefreight.all_parcels[item]
            if spacefreight.check_mass(spacecraft, parcel) and spacefreight.check_vol(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(spacecraft, parcel)

    if len(spacefreight.unpacked_parcels) <= TARGETI:
        spacefreight.printing()

    return len(spacefreight.unpacked_parcels)

def iterative_random():
        """
        Random allocate the parcels in random spacecrafts
        Optimize iterative
        """
        spacecraft_randoms = random.sample(range(4), 4)

        # set variables at 0 after run for every spacecraft
        for spacecraft_number in spacecraft_randoms:
            spacecraft_name = spacefreight.spacecrafts_names[spacecraft_number]
            spacecraft = spacefreight.spacecrafts[spacecraft_name]
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
            if (parcel.mass < (mean_mass / 2)) and (parcel.volume < mean_vol):
                if spacefreight.check_mass(spacefreight.spacecrafts['progress'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['progress'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                    spacefreight.update(spacefreight.spacecrafts['progress'], parcel)

        # sorted_vol = sorted(spacefreight.all_parcels, key=lambda x: x.volume)
        # sorted_mass = sorted(spacefreight.all_parcels,  key=lambda x: x.mass)

        # allocating the rest of the parcels random
        for spacecraft_number in spacecraft_randoms:
            spacecraft_name = spacefreight.spacecrafts_names[spacecraft_number]
            spacecraft = spacefreight.spacecrafts[spacecraft_name]
            for item in parcel_randoms:
                parcel = spacefreight.all_parcels[item]
                if spacefreight.check_mass(spacecraft, parcel) and spacefreight.check_vol(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                    spacefreight.update(spacecraft, parcel)

        if len(spacefreight.unpacked_parcels) <= TARGETI:
            spacefreight.printing()

        return len(spacefreight.unpacked_parcels)

def iterative_sorted():
        """
        Random allocate the parcels in random spacecrafts
        Optimize iterative
        """
        spacecraft_randoms = random.sample(range(4), 4)

        # set variables at 0 after run for every spacecraft
        for spacecraft_number in spacecraft_randoms:
            spacecraft_name = spacefreight.spacecrafts_names[spacecraft_number]
            spacecraft = spacefreight.spacecrafts[spacecraft_name]
            spacecraft.packed_parcels = []
            spacecraft.packed_mass = 0
            spacecraft.packed_vol = 0

        # list with random numbers: order in which the parcels are being added
        sorted_vol = sorted(spacefreight.all_parcels, key=lambda x: x.volume)

        # every single run of the function sets unpacked_parcels at starting point
        spacefreight.unpacked_parcels = []
        for p in spacefreight.all_parcels:
            spacefreight.unpacked_parcels.append(p.ID)

        # allocate parcels with iterative constraints
        for parcel in sorted_vol:
            if (parcel.mass < mean_mass / 2) and (parcel.volume < mean_vol):
                if spacefreight.check_mass(spacefreight.spacecrafts['progress'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['progress'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                    spacefreight.update(spacefreight.spacecrafts['progress'], parcel)
            if (parcel.mass > mean_mass) and (parcel.volume < mean_vol):
                if spacefreight.check_mass(spacefreight.spacecrafts['dragon'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['dragon'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                    spacefreight.update(spacefreight.spacecrafts['dragon'], parcel)
            if (parcel.mass > mean_mass) and (parcel.volume > mean_vol):
                if spacefreight.check_mass(spacefreight.spacecrafts['kounotori'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['kounotori'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                    spacefreight.update(spacefreight.spacecrafts['kounotori'], parcel)
            if (parcel.mass < mean_mass) and (parcel.volume > mean_vol):
                if spacefreight.check_mass(spacefreight.spacecrafts['cygnus'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['cygnus'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                    spacefreight.update(spacefreight.spacecrafts['cygnus'], parcel)



        # allocating the rest of the parcels random
        for spacecraft_number in spacecraft_randoms:
            spacecraft_name = spacefreight.spacecrafts_names[spacecraft_number]
            spacecraft = spacefreight.spacecrafts[spacecraft_name]
            for parcel in sorted_vol:
                if spacefreight.check_mass(spacecraft, parcel) and spacefreight.check_vol(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                    spacefreight.update(spacecraft, parcel)

        if len(spacefreight.unpacked_parcels) <= TARGETI:
            spacefreight.printing()

        return len(spacefreight.unpacked_parcels)

def sorted_mass_vol_iterative():
        """
        Sort first by mass, then by volume
        Heaviest in Dragon, biggest in Cygnus
        """
        spacecraft_randoms = random.sample(range(4), 4)

        # set variables at 0 after run for every spacecraft
        for spacecraft_number in spacecraft_randoms:
            spacecraft_name = spacefreight.spacecrafts_names[spacecraft_number]
            spacecraft = spacefreight.spacecrafts[spacecraft_name]
            spacecraft.packed_parcels = []
            spacecraft.packed_mass = 0
            spacecraft.packed_vol = 0

        # every single run of the function sets unpacked_parcels at starting point
        spacefreight.unpacked_parcels = []
        for p in spacefreight.all_parcels:
            spacefreight.unpacked_parcels.append(p.ID)


        # sort the list by mass (reverse=true if you want big to small)
        sorted_mass = sorted(spacefreight.all_parcels, key=lambda x: x.mass, reverse=True)

        # set variables
        dragon = spacefreight.spacecrafts['dragon']
        count = 0

        for parcel in sorted_mass:
            if spacefreight.check_mass(dragon, parcel) and spacefreight.check_vol(dragon, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(dragon, parcel)
                count += 1

        # sort the remaining list by volume (reverse=true if you want big to small)
        remaining = sorted_mass[count:]
        remaining = sorted(remaining, key=lambda x: x.volume, reverse=True)

        # set variables
        cygnus = spacefreight.spacecrafts['cygnus']
        count = 0

        for parcel in remaining:
            if spacefreight.check_mass(cygnus, parcel) and spacefreight.check_vol(cygnus, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                spacefreight.update(cygnus, parcel)
                count += 1

        remaining = remaining[count:]

        # allocate parcels with iterative constraints
        for parcel in remaining:
            if (parcel.mass > mean_mass) and (parcel.volume > mean_vol):
                if spacefreight.check_mass(spacefreight.spacecrafts['kounotori'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['kounotori'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                    spacefreight.update(spacefreight.spacecrafts['kounotori'], parcel)
            if (parcel.mass < mean_mass) and (parcel.volume < mean_vol):
                if spacefreight.check_mass(spacefreight.spacecrafts['progress'], parcel) and spacefreight.check_vol(spacefreight.spacecrafts['progress'], parcel) and parcel.ID in spacefreight.unpacked_parcels:
                    spacefreight.update(spacefreight.spacecrafts['progress'], parcel)

        # allocating the rest of the parcels random
        for spacecraft_number in spacecraft_randoms:
            spacecraft_name = spacefreight.spacecrafts_names[spacecraft_number]
            spacecraft = spacefreight.spacecrafts[spacecraft_name]
            for parcel in remaining:
                if spacefreight.check_mass(spacecraft, parcel) and spacefreight.check_vol(spacecraft, parcel) and parcel.ID in spacefreight.unpacked_parcels:
                    spacefreight.update(spacecraft, parcel)

        if len(spacefreight.unpacked_parcels) <= TARGETI:
            spacefreight.printing()


        return len(spacefreight.unpacked_parcels)
