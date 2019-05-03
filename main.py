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

spacefreight = SpaceFreight()

# RANDOM
# start solution
best_solution = random_constraints()
count = 0
max_iterations = 3900

# RUN NOT ALL PARCELS
while count < max_iterations:
    count += 1
    solution = random_constraints()
    # check if costs better
    if solution.not_bring < best_solution.not_bring:
        best_solution = solution
    elif solution.not_bring == best_solution.not_bring and solution.costs < best_solution.costs:
        best_solution = solution

# RUN ALL PARCELS
while count < max_iterations:
    count += 1
    solution = random_constraints()
    # check if costs better
    if solution.costs < best_solution.costs:
        best_solution = solution

print("Iterations:", count)

spacefreight.printing_all(best_solution)

# HILL CLIMBER
# hill_climber_random()
