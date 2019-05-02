#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
Main script
"""
# set import location
import sys
sys.path[0] = sys.path[0] + '/Code'
# import
from parcel import Parcel
from spacecraft import Spacecraft
from spacefreight import SpaceFreight
from random_algorithms_new import *
from first_fit_algorithms import *
from hill_climber import *
import time

# FIRST FIT
# first_fit()

# SORTED
# sorted_mass_first_fit()
# sorted_vol_first_fit()
# sorted_mass_random()
# sorted_vol_random()
# spacefreight.printing()


# RANDOM
# number_unpacked_parcels = random_constraints().not_bring
# count = 0
#
# while number_unpacked_parcels > TARGETR:
# 	number_unpacked_parcels = random_constraints().not_bring
# 	count += 1

# spacefreight.printing()

# ALLE 100 MEE
random_all_parcels()






# # ITERATIVE
# number_unpacked_parcels = 100
# count = 0
# max_iterations = 2
#
# print(mean_mass)
# print(mean_vol)
#
# while number_unpacked_parcels > TARGETI and count < max_iterations:
# 	count += 1
# 	number_unpacked_parcels = iterative_random()
#
# print("Iterations:", count)


# HILL CLIMBER
# hill_climber_random()
