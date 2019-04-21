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

# FIRST FIT
# first_fit()

# SORTED
# sorted_mass_first_fit()
# sorted_vol_first_fit()
# sorted_mass_random()
# sorted_vol_random()
# spacefreight.printing()

# JONGENS LET OP DAT JE TARGET IN ITERATIVE EN RANDOM ALLEBEI HETZELFDE DOET
# ANDERS GAAT HIJ SPACEN

# RANDOM
# number_unpacked_parcels = allocate_random()
# count = 0
#
# while number_unpacked_parcels > TARGET:
# 	number_unpacked_parcels = allocate_random()
# 	count += 1

# spacefreight.printing()

# ITERATIVE
number_unpacked_parcels = 100
count = 0

while number_unpacked_parcels > TARGET:
	count += 1
	number_unpacked_parcels = iterative_pseudo_random()

print("Iterations:", count)
