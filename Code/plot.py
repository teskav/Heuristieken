# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
Script with plot functions
"""

import matplotlib.pyplot as plt

def plot_costs(dataframe):
    """
    This function plots the costs of multiple runs in 1 graph
    """
    plt.plot(list(range(len(dataframe['costs_solution']))), \
    dataframe['costs_solution'])
    plt.xlabel('Runs')
    plt.ylabel('Costs')
    plt.title('Distribution of the solutions')
    plt.show()


def plot_cooling(iterations_dataframe):
    """
    This function plots the cooling schedule (course of the temperature)
    of 1 run of the simulated annealing"
    """
    # x plot kan misschien ook wel index kolom voor dataframe voor
    # gebruikt worden
    plt.plot(list(range(len(iterations_dataframe['temperature']))), \
    iterations_dataframe['temperature'])
    plt.xlabel('Iterations')
    plt.ylabel('Temperature')
    plt.title('Cooling schedule')
    plt.show()

def plot_acceptatie(iterations_dataframe):
    """
    This function plots the course of the acceptation rate
    of 1 run of the simulated annealing"
    """
    plt.plot(list(range(len(iterations_dataframe['acceptance']))), \
    iterations_dataframe['acceptance'])
    plt.xlabel('Iterations')
    plt.ylabel('Acceptatiekans')
    plt.title('Verloop acceptatiekans')
    plt.show()
