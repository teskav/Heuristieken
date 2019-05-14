#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
Script with plot functions
"""

import matplotlib.pyplot as plt

def plot_costs(iterations_dataframe):

    plt.plot(list(range(len(iterations_dataframe.iloc[:,2]))), iterations_dataframe.iloc[:,2])
    plt.xlabel('Iterations')
    plt.ylabel('Costs')
    plt.title('Distributions of solutions per run')
    plt.show()


def plot_histogram():
    n_bins=max(plot_parcels)-min(plot_parcels)
    plt.hist(plot_parcels, bins=n_bins, align='left')
    plt.xticks(range(min(plot_parcels), max(plot_parcels)))
    plt.xlabel('Number of parcels packed')
    plt.ylabel('Times')
    plt.show()

def plot_cooling(iterations_dataframe):
    "This function plots the cooling schedule (course of the temperature) of 1 run of the simulated annealing"
    plt.plot(list(range(len(iterations_dataframe.iloc[:,2]))), iterations_dataframe.iloc[:,5])
    plt.xlabel('Iterations')
    plt.ylabel('Temperature')
    plt.title('Cooling schedule')
    plt.show()

def plot_acceptatie(iterations_dataframe):
    "This function plots the course of the acceptation rate of 1 run of the simulated annealing"
    plt.plot(list(range(len(iterations_dataframe.iloc[:,2]))), iterations_dataframe.iloc[:,6])
    plt.xlabel('Iterations')
    plt.ylabel('Acceptatiekans')
    plt.title('Verloop acceptatiekans')
    plt.show()
