# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script contains the different versions (functions)
of the first fit algorithms.
"""

from spacefreight import SpaceFreight
from helpers import *

spacefreight = SpaceFreight()

def first_fit(heuristic):
    """
    Allocates the parcels in spacecrafts with the first fit algorithm.
    """
    if heuristic == 'normal':
        cargolist = spacefreight.all_parcels
    elif heuristic == 'sorted mass':
        # sort the list by mass (reverse=true if you want big to small)
        cargolist = sorted(spacefreight.all_parcels, key=lambda x: x.mass)
    elif heuristic == 'sorted vol':
        # sort the list by volume (reverse=true if you want big to small)
        cargolist = sorted(spacefreight.all_parcels, key=lambda x: x.volume, \
                           reverse=True)

    # set starting
    used_spacecrafts = []
    total_costs = 0

    # every single run of the function: set unpacked_parcels at starting point
    spacefreight.unpacked_parcels = set_up_unpacked()

    while len(spacefreight.unpacked_parcels) > 0:
        # go over list of spacecrafts and parcels and pack or not
        for spacecraft_number in range(len(spacefreight.spacecrafts)):
            # spacecraft = spacefreight.spacecrafts[spacecraft_number]
            spacecraft = copy.copy(spacefreight.spacecrafts[spacecraft_number])

            # set variables at 0
            empty_single_spacecraft(spacecraft)

            for parcel in cargolist:
                # parcel = spacefreight.all_parcels[parcel_number]
                if (spacefreight.check(spacecraft, parcel) and
                        parcel.ID in spacefreight.unpacked_parcels):
                    spacefreight.update(spacecraft, parcel)

            # calculate costs spacecraft
            spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
            total_costs += spacecraft.costs

            # add spacecraft to used_spacecrafts
            used_spacecrafts.append(spacecraft)

            # stop if all parcels are packed
            if len(spacefreight.unpacked_parcels) == 0:
                break

    # save solution
    current_solution = Solution('random', len(spacefreight.unpacked_parcels), \
    spacefreight.unpacked_parcels, total_costs, used_spacecrafts)

    return current_solution
