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
import pandas as pd

spacefreight = SpaceFreight()

# DATAFRAME
iterations_dataframe = pd.DataFrame()

# RANDOM
# start solution
max_iterations = 3
best_solution = random_all_parcels()
count = 0

# save to dataframe
dataframe_row = spacefreight.save_iteration(best_solution, count)
iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

# RUN NOT ALL PARCELS
while count < max_iterations:
    count += 1
    solution = random_all_parcels()

    # save to dataframe
    dataframe_row = spacefreight.save_iteration(solution, count)
    iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

    # check if costs better
    if solution.not_bring < best_solution.not_bring:
        best_solution = solution
    elif solution.not_bring == best_solution.not_bring and solution.costs < best_solution.costs:
        best_solution = solution

# RUN ALL PARCELS
# while count < max_iterations:
#     count += 1
#     solution = random_all_parcels()
#     # check if costs better
#     if solution.costs < best_solution.costs:
#         best_solution = solution

print("Iterations:", count)
spacefreight.printing_all(best_solution)

iterations_dataframe.to_csv(r'../Heuristieken/Outputs/Output3.csv')

# Minimale en maximale kosten printen
# maximum = spacefreight.max_costs()
# print("Maximal costs", maximum/1000000000, "billion")
# minimum = spacefreight.min_costs()
# print("Minimal costs", minimum/1000000000, "billion")

# HILL CLIMBER
# hill_climber_random()
