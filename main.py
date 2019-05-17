# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
Main script, used to process the call for functions in the terminal
"""

# set import location
import sys
sys.path[0] = sys.path[0] + '/Code'
# import
from spacefreight import SpaceFreight
import matplotlib.pyplot as plt
from call_functions import *

spacefreight = SpaceFreight()

algorithm = input("Please give algorithm: ")

if algorithm == 'random':
    iterations_dataframe = call_random()

if algorithm == 'pseudo greedy random':
    iterations_dataframe = call_pseudo_greedy_random()

if algorithm == 'random all':
    iterations_dataframe = call_random_all()

if algorithm == 'pseudo greedy random all':
    iterations_dataframe = call_pseudo_greedy_random_all()

if algorithm == 'hill climber':
    iterations_dataframe = call_hill_climber()

if algorithm == 'hill climber spacecrafts':
    iterations_dataframe = call_hill_climber_spacecrafts()

if algorithm == 'hill climber combined':
    iterations_dataframe = call_hill_climber_combined()

if algorithm == 'simulated annealing':
    iterations_dataframe = call_simulated_annealing()

if algorithm == 'simulated annealing combined':
    iterations_dataframe = call_simulated_annealing_combined()

if algorithm == 'political constraints':
    iterations_dataframe = call_political_constraints()

# iterations_dataframe.to_csv(r'../Heuristieken/Outputs/test.csv')

# plot costs of iterations FROM DATAFRAME
# plot_costs(iterations_dataframe)
