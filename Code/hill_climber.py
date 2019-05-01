#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script contains the different versions (functions) of the HILL CLIMBER algorithms
"""
from spacefreight import SpaceFreight
from random_algorithms import *
import random
import numpy as np
import copy

spacefreight = SpaceFreight()

 # allowed number of parcels to leave behind
TARGETI = 4

def hill_climber_random():

    # starting solution
    allocate_random()
    print(spacefreight.spacecrafts['cygnus'].packed_parcels)


    # select the switching parcels and spacecrafts random
    spacecraft_random_1 = random.randrange(4)
    spacecraft_random_2 = random.randrange(4)
    spacecraft_1 = spacefreight.spacecrafts[spacefreight.spacecrafts_names[spacecraft_random_1]]
    spacecraft_2 = spacefreight.spacecrafts[spacefreight.spacecrafts_names[spacecraft_random_2]]
    print(spacecraft_1.mass)

    parcel_random_1 = random.randrange(len(spacecraft_1.packed_parcels))
