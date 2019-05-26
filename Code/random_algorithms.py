# Heuristieken
# April - May 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit

"""
This script contains the different versions (functions)
of the random algorithms
"""

from spacefreight import SpaceFreight
from spacecraft import Spacecraft
from solution import Solution
from helpers import *
import random
import numpy as np
import copy

spacefreight = SpaceFreight()

spacecrafts_list = []
spacecrafts_list.append(Spacecraft('Progress', 2400, 7.6, 7020, \
                            175000000, 0.74, 'Russia'))
spacecrafts_list.append(Spacecraft('Progress', 2400, 7.6, 7020, \
                            175000000, 0.74, 'Russia'))
spacecrafts_list.append(Spacecraft('Progress', 2400, 7.6, 7020, \
                            175000000, 0.74, 'Russia'))
spacecrafts_list.append(Spacecraft('Progress', 2400, 7.6, 7020, \
                            175000000, 0.74, 'Russia'))
spacecrafts_list.append(Spacecraft('Progress', 2400, 7.6, 7020, \
                            175000000, 0.74, 'Russia'))
spacecrafts_list.append(Spacecraft('Progress', 2400, 7.6, 7020, \
                            175000000, 0.74, 'Russia'))
spacecrafts_list.append(Spacecraft('Dragon', 6000, 10, 12200, \
                            347000000, 0.72, 'USA'))

def random_algorithm():
    """
    Random allocate the parcels in spacecrafts
    """
    # set starting settings random
    used_spacecrafts,total_costs,parcel_randoms,spacecraft_randoms = \
        set_up_random()

    # every single run of the function sets unpacked_parcels at starting point
    spacefreight.unpacked_parcels = set_up_unpacked()

    while len(spacefreight.unpacked_parcels) > 0:
        spacecraft = copy.copy(random.choice(spacefreight.spacecrafts))

        # set variables at 0
        empty_single_spacecraft(spacecraft)

        for parcel_number in parcel_randoms:
            parcel = spacefreight.all_parcels[parcel_number]
            if (spacefreight.check(spacecraft, parcel) and
                    parcel.ID in spacefreight.unpacked_parcels):
                spacecraft = spacefreight.update(spacecraft, parcel)

        #calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    # save solution
    current_solution = Solution('random all', total_costs, used_spacecrafts)

    return current_solution

def random_fleet_algorithm():
    """
    Random allocate the parcels in spacecrafts
    """
    # set starting settings random
    parcel_randoms = random.sample(range(100), 100)
    spacecraft_randoms = random.sample(range(7),7)
    used_spacecrafts = []
    total_costs = 0

    # every single run of the function sets unpacked_parcels at starting point
    spacefreight.unpacked_parcels = set_up_unpacked()

    for spacecraft_number in spacecraft_randoms:
        spacecraft = copy.copy(spacecrafts_list[spacecraft_number])

        # set variables at 0
        empty_single_spacecraft(spacecraft)

        for parcel_number in parcel_randoms:
            parcel = spacefreight.all_parcels[parcel_number]
            if (spacefreight.check(spacecraft, parcel) and
                    parcel.ID in spacefreight.unpacked_parcels):
                spacecraft = spacefreight.update(spacecraft, parcel)

        #calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    # save solution
    current_solution = Solution('random all', total_costs, used_spacecrafts)

    if len(spacefreight.unpacked_parcels) > 0:
        return current_solution, False
    else:
        return current_solution, True


def pseudo_greedy_random():
    """
    Random allocate the parcels in random spacecrafts with constraints
    """
    # set starting settings random
    used_spacecrafts, total_costs, parcel_randoms, spacecraft_randoms = \
    set_up_random()

    # set variables at 0 after run for every spacecraft
    for spacecraft_number in spacecraft_randoms:
        spacecraft = spacefreight.spacecrafts[spacecraft_number]
        empty_single_spacecraft(spacecraft)

    # every single run of the function sets unpacked_parcels at starting point
    spacefreight.unpacked_parcels = set_up_unpacked()

    # allocate parcels with iterative constraints
    for parcel_number in parcel_randoms:
        parcel = spacefreight.all_parcels[parcel_number]
        for number in range(len(spacefreight.spacecrafts)):
            if (check_constraints_spacecraft(parcel, number) == True and
                    check_constraints(parcel, spacefreight, number) == True):
                spacefreight.update(spacefreight.spacecrafts[number], parcel)

    # allocating the rest of the parcels random
    for spacecraft_number in spacecraft_randoms:
        spacecraft = copy.copy(spacefreight.spacecrafts[spacecraft_number])
        for parcel_number in parcel_randoms:
            parcel = spacefreight.all_parcels[parcel_number]
            if (spacefreight.check(spacecraft, parcel) and
                    parcel.ID in spacefreight.unpacked_parcels):
                spacefreight.update(spacecraft, parcel)
        #calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    while len(spacefreight.unpacked_parcels) > 0:
        spacecraft = copy.copy(random.choice(spacefreight.spacecrafts))

        # set variables at 0
        empty_single_spacecraft(spacecraft)
        for parcel_number in parcel_randoms:
            parcel = spacefreight.all_parcels[parcel_number]
            if (spacefreight.check(spacecraft, parcel) and
                    parcel.ID in spacefreight.unpacked_parcels):
                spacecraft = spacefreight.update(spacecraft, parcel)

        #calculate costs spacecraft
        spacecraft.costs = spacefreight.calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    # save solution
    current_solution = Solution('constraints all', total_costs, used_spacecrafts)

    return current_solution

def political_constraints(countries):
    """
    Random allocate the parcels in spacecrafts with the political constraints
    The difference between the number of spacecrafts per country can be at most1
    """
    # set starting settings random
    used_spacecrafts, total_costs, parcel_randoms, spacecraft_randoms = \
        set_up_random()

    # every run of the function sets unpacked_parcels at starting point
    spacefreight.unpacked_parcels = set_up_unpacked()

    while len(spacefreight.unpacked_parcels) > 0:
        # select random spacecraft
        spacecraft = copy.copy(random.choice(spacefreight.spacecrafts))

        # add 1 to dataframe
        countries.loc[countries['country'] == spacecraft.country, \
            ['spacecrafts']] += 1

        # check if political constraints are not violated
        if not (countries['spacecrafts'].min() >=
                (countries['spacecrafts'].max() - 1)):
            # change number of spacecrafts back and
            # start over (choose new spacecrafts)
            countries.loc[countries['country'] == spacecraft.country, \
                ['spacecrafts']] -= 1
        else:
            # set variables at 0
            empty_single_spacecraft(spacecraft)

            for parcel_number in parcel_randoms:
                parcel = spacefreight.all_parcels[parcel_number]
                if (spacefreight.check(spacecraft, parcel) and
                        parcel.ID in spacefreight.unpacked_parcels):
                    spacecraft = spacefreight.update(spacecraft, parcel)

            #calculate costs spacecraft
            spacecraft.costs = \
                spacefreight.calculate_costs_spacecraft(spacecraft)
            total_costs += spacecraft.costs

            # add spacecraft to used_spacecrafts
            used_spacecrafts.append(spacecraft)

    # save solution
    current_solution = Solution('political constraints', total_costs, \
                        used_spacecrafts)

    return current_solution, countries
