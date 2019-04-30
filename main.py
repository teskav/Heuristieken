#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
Main script
"""
# set import location
import sys
sys.path[0] = sys.path[0] + '/Scripts'
# import
from parcel import Parcel
from spacecraft import Spacecraft
from spacefreight import SpaceFreight
from random_algorithms import *
from first_fit_algorithms import *
from iterative_algorithms import *
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
# number_unpacked_parcels = allocate_random()
# count = 0
#
# while number_unpacked_parcels > TARGETR:
# 	number_unpacked_parcels = allocate_random()
# 	count += 1

# spacefreight.printing()

# ITERATIVE
number_unpacked_parcels = 100
count = 0
max_iterations = 2

print(mean_mass)
print(mean_vol)

while number_unpacked_parcels > TARGETI and count < max_iterations:
	count += 1
	number_unpacked_parcels = iterative_random()

print("Iterations:", count)

#
# number_unpacked_parcels = 100
# count = 0
#
# while number_unpacked_parcels > TARGETI:
# 	count += 1
# 	number_unpacked_parcels = sorted_mass_vol_iterative()
