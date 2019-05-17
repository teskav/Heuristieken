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
    dataframe = call_random()

if algorithm == 'pseudo greedy random':
    dataframe = call_pseudo_greedy_random()

if algorithm == 'random all':
    dataframe = call_random_all()

if algorithm == 'pseudo greedy random all':
    dataframe = call_pseudo_greedy_random_all()

if algorithm == 'hill climber':
    iterations_dataframe, runs_dataframe = call_hill_climber()

if algorithm == 'hill climber spacecrafts':
    iterations_dataframe, runs_dataframe = call_hill_climber_spacecrafts()

if algorithm == 'hill climber combined':
    dataframe = call_hill_climber_combined()

if algorithm == 'simulated annealing':
    iterations_dataframe = call_simulated_annealing()

if algorithm == 'simulated annealing combined':
    dataframe = call_simulated_annealing_combined()

if algorithm == 'political constraints':
    dataframe = call_political_constraints()

# RANDOM ALL
# iterations_dataframe.to_csv(r'../Heuristieken/Outputs/Random/test.csv')

# HILL CLIMBER (SPECIFY PARCEL OR SPACECRAFT SWITCH)
# iterations_dataframe.to_csv(r'../Heuristieken/Outputs/Hill_Climber/iterations_spacecrafts.csv')
# runs_dataframe.to_csv(r'../Heuristieken/Outputs/Hill_Climber/runs_spacecrafts.csv')


# SIMULATED ANNEALING (nog geen runs dataframe)
iterations_dataframe.to_csv(r'../Heuristieken/Outputs/Simulated_Annealing/iterations.csv')
