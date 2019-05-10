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
from plot import *
import pandas as pd
import matplotlib.pyplot as plt
from aanroepen import *

spacefreight = SpaceFreight()

text = input("Please give input: ")

# histogram plotten
# plot_parcels = []

# RUN NOT ALL PARCELS
if text == 'random':
    iterations_dataframe = aanroepen_random()

if text == 'constrained':
    iterations_dataframe = aanroepen_constrained()

if text == 'random all':
    iterations_dataframe = aanroepen_random_all()

if text == 'constrained all':
    iterations_dataframe = aanroepen_constrained_all()

if text == 'hill climber':
    iterations_dataframe = aanroepen_hill_climber()

if text == 'simulated annealing':
    iterations_dataframe = aanroepen_simulated_annealing()

iterations_dataframe.to_csv(r'../Heuristieken/Outputs/hillclimber_30x2000.csv')

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
