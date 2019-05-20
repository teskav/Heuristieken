# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script contains the different versions (functions)
of the first fit algorithms
"""

from spacefreight import SpaceFreight
from helpers import *

spacefreight = SpaceFreight()

def first_fit():
    """
    Allocate the parcels in spacecrafts
    """

    # set starting
    used_spacecrafts = []
    total_costs = 0

    # every single run of the function: set unpacked_parcels at starting point
    spacefreight.unpacked_parcels = set_up_unpacked()

    # go over list of spacecrafts and parcels and pack or not
    for spacecraft_number in range(len(spacefreight.spacecrafts)):
        # spacecraft = spacefreight.spacecrafts[spacecraft_number]
        spacecraft = copy.copy(spacefreight.spacecrafts[spacecraft_number])

        # set variables at 0
        empty_single_spacecraft(spacecraft)

        for parcel_number in range(len(spacefreight.all_parcels)):
            parcel = spacefreight.all_parcels[parcel_number]
            if (spacefreight.check(spacecraft, parcel) and
                    parcel.ID in spacefreight.unpacked_parcels):
                spacefreight.update(spacecraft, parcel)

        # calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    # save solution
    current_solution = Solution('random', len(spacefreight.unpacked_parcels), \
    spacefreight.unpacked_parcels, total_costs, used_spacecrafts)

    return current_solution

def first_fit_sorted_mass():
    """
    Allocate the parcels in spacecrafts with a sorted list by mass
    """
    # sort the list by mass (reverse=true if you want big to small)
    sorted_mass = sorted(spacefreight.all_parcels, key=lambda x: x.mass)

    # set starting
    used_spacecrafts = []
    total_costs = 0

    # every single run of the function: set unpacked_parcels at starting point
    spacefreight.unpacked_parcels = set_up_unpacked()

    # go over list of spacecrafts and parcels and pack or not
    for spacecraft_number in range(len(spacefreight.spacecrafts)):
        # spacecraft = spacefreight.spacecrafts[spacecraft_number]
        spacecraft = copy.copy(spacefreight.spacecrafts[spacecraft_number])

        # set variables at 0
        empty_single_spacecraft(spacecraft)

        for parcel in sorted_mass:
            if (spacefreight.check(spacecraft, parcel) and
                    parcel.ID in spacefreight.unpacked_parcels):
                spacefreight.update(spacecraft, parcel)

        # calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    # save solution
    current_solution = Solution('random', len(spacefreight.unpacked_parcels), \
    spacefreight.unpacked_parcels, total_costs, used_spacecrafts)

    return current_solution

def first_fit_sorted_vol():
    """
    Allocate the parcels in spacecrafts with a sorted list by volume
    """
    # sort the list by mass (reverse=true if you want big to small)
    sorted_volume = sorted(spacefreight.all_parcels, key=lambda x: x.volume, \
                    reverse=True)

    # set starting
    used_spacecrafts = []
    total_costs = 0

    # every single run of the function: set unpacked_parcels at starting point
    spacefreight.unpacked_parcels = set_up_unpacked()

    # go over list of spacecrafts and parcels and pack or not
    for spacecraft_number in range(len(spacefreight.spacecrafts)):
        # spacecraft = spacefreight.spacecrafts[spacecraft_number]
        spacecraft = copy.copy(spacefreight.spacecrafts[spacecraft_number])

        # set variables at 0
        empty_single_spacecraft(spacecraft)

        for parcel in sorted_volume:
            if (spacefreight.check(spacecraft, parcel) and
                    parcel.ID in spacefreight.unpacked_parcels):
                spacefreight.update(spacecraft, parcel)

        # calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    # save solution
    current_solution = Solution('random', len(spacefreight.unpacked_parcels), \
    spacefreight.unpacked_parcels, total_costs, used_spacecrafts)

    return current_solution
