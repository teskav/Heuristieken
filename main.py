#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
Main script
"""
# set import location
import sys
sys.path[0] = sys.path[0] + '/Code'
# import
from spacefreight import SpaceFreight
import matplotlib.pyplot as plt
from call_functions import *

spacefreight = SpaceFreight()

text = input("Please give input: ")

# RUN NOT ALL PARCELS
if text == 'random':
    iterations_dataframe = call_random()

if text == 'constrained':
    iterations_dataframe = call_constrained()

if text == 'random all':
    iterations_dataframe = call_random_all()

if text == 'constrained all':
    iterations_dataframe = call_constrained_all()

if text == 'hill climber':
    iterations_dataframe = call_hill_climber()

if text == 'hill climber spacecrafts':
    iterations_dataframe = call_hill_climber_spacecrafts()

if text == 'hill climber combined':
    iterations_dataframe = call_hill_climber_combined()

if text == 'simulated annealing':
    iterations_dataframe = call_simulated_annealing()

if text == 'simulated annealing combined':
    iterations_dataframe = call_simulated_annealing_combined()

if text == 'political constraints':
    iterations_dataframe = call_political_constraints()

iterations_dataframe.to_csv(r'../Heuristieken/Outputs/political_constraints_CL1_1000.csv')

# plot costs of iterations FROM DATAFRAME
# plot_costs(iterations_dataframe)

# histogram of number of parcels packed -> nog niet als functie gemaakt
# plot_histogram()


# n_bins=max(plot_parcels)-min(plot_parcels)
# plt.hist(plot_parcels, bins=n_bins, align='left')
# plt.xticks(range(min(plot_parcels), max(plot_parcels)))
# plt.xlabel('Number of parcels packed')
# plt.ylabel('Times')
# plt.show()
