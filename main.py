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

# first fit
# first_fit()

# random
number_unpacked_parcels = allocate_pseudo_random()
count = 0

while number_unpacked_parcels > target:
	number_unpacked_parcels = allocate_pseudo_random()
	count += 1

# spacefreight.sort(spacefreight.all_parcels)
