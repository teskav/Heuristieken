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
from iterative_algorithms_new import *
from hill_climber import *
import pandas as pd
import matplotlib.pyplot as plt

spacefreight = SpaceFreight()

text = input("Please give input: ")

# DATAFRAME & ITERATIONS (ALTIJD AAN)
iterations_dataframe = pd.DataFrame()
max_iterations = 100

# histogram plotten
# plot_parcels = []

# RUN NOT ALL PARCELS
if text == 'random':
    count = 0
    best_solution = random_greedy()
    dataframe_row = spacefreight.save_iteration(best_solution, count)
    iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

    while count < max_iterations:
        count += 1
        solution = random_greedy()

        # save to dataframe
        dataframe_row = spacefreight.save_iteration(solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

        # add number of packed parcels of solution to list to plot
        # plot_parcels.append(len(spacefreight.all_parcels)-solution.not_bring)

        # check if costs better
        if solution.not_bring < best_solution.not_bring:
            best_solution = solution
        elif solution.not_bring == best_solution.not_bring and solution.costs < best_solution.costs:
            best_solution = solution

    print("Iterations:", count)
    spacefreight.printing(best_solution)

if text == 'constrained':
    count = 0
    best_solution = random_constraints()
    dataframe_row = spacefreight.save_iteration(best_solution, count)
    iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

    while count < max_iterations:
        count += 1
        solution = random_constraints()

        # save to dataframe
        dataframe_row = spacefreight.save_iteration(solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

        # add number of packed parcels of solution to list to plot
        # plot_parcels.append(len(spacefreight.all_parcels)-solution.not_bring)

        # check if costs better
        if solution.not_bring < best_solution.not_bring:
            best_solution = solution
        elif solution.not_bring == best_solution.not_bring and solution.costs < best_solution.costs:
            best_solution = solution

    print("Iterations:", count)
    spacefreight.printing(best_solution)

if text == 'random all':
    # run all parcels random
    best_solution = random_all_parcels()
    count = 0
    dataframe_row = spacefreight.save_iteration(best_solution, count)
    iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

    while count < max_iterations:
        count += 1
        solution = random_all_parcels()

        # save to dataframe
        dataframe_row = spacefreight.save_iteration(solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

        # check if costs better
        if solution.costs < best_solution.costs:
            best_solution = solution

    print("Iterations:", count)
    spacefreight.printing(best_solution)

if text == 'constrained all':
    # run all parcels constrained
    best_solution = random_constraints_all()
    count = 0
    dataframe_row = spacefreight.save_iteration(best_solution, count)
    iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

    while count < max_iterations:
        count += 1
        solution = random_constraints_all()

        # save to dataframe
        dataframe_row = spacefreight.save_iteration(solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

        # check if costs better
        if solution.costs < best_solution.costs:
            best_solution = solution

    print("Iterations:", count)
    spacefreight.printing(best_solution)

if text == 'hill climber':
    # HILL CLIMBER
    iterations_dataframe, count, current_solution = hill_climber(iterations_dataframe, max_iterations)
    print("Iterations:", count)
    spacefreight.printing(current_solution)

# iterations_dataframe.to_csv(r'../Heuristieken/Outputs/Output5.csv')

# PLOT
# plot costs of iterations FROM DATAFRAME
plt.plot(list(range(len(iterations_dataframe.iloc[:,2]))), iterations_dataframe.iloc[:,2])
plt.xlabel('Iterations')
plt.ylabel('Costs (in billion dollars)')
plt.show()

# # histogram of number of parcels packed
# n_bins=max(plot_parcels)-min(plot_parcels)
# plt.hist(plot_parcels, bins=n_bins, align='left')
# plt.xticks(range(min(plot_parcels), max(plot_parcels)))
# plt.xlabel('Number of parcels packed')
# plt.ylabel('Times')
# plt.show()
