#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
Script with plot functions
"""

import matplotlib.pyplot as plt

def plot_costs(iterations_dataframe):

    plt.plot(list(range(len(iterations_dataframe.iloc[:,2]))), iterations_dataframe.iloc[:,2])
    plt.xlabel('Iterations')
    plt.ylabel('Costs (in billion dollars)')
    plt.title('Distributions of costs over the solutions')
    plt.show()


def plot_histogram():
    n_bins=max(plot_parcels)-min(plot_parcels)
    plt.hist(plot_parcels, bins=n_bins, align='left')
    plt.xticks(range(min(plot_parcels), max(plot_parcels)))
    plt.xlabel('Number of parcels packed')
    plt.ylabel('Times')
    plt.show()
