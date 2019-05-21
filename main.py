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
from spacefreight import list
import matplotlib.pyplot as plt
from call_functions import *

spacefreight = SpaceFreight()

print("")
print("Algorithm options: \n first fit \n first fit sorted mass \
        \n first fit sorted vol \n random \n pseudo greedy random \
        \n random all \n pseudo greedy random all \n hill climber \
        \n hill climber spacecrafts \n hill climber combined \
        \n simulated annealing \n simulated annealing combined")
# only print political constraint choice for cargolist 3
if list == '3':
    print(" political constraints")

algorithm = input("\nPlease give algorithm: ")

if algorithm == 'first fit':
    dataframe = call_first_fit()

if algorithm == 'first fit sorted mass':
    dataframe = call_first_fit_sorted_mass()

if algorithm == 'first fit sorted vol':
    dataframe = call_first_fit_sorted_vol()

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

if algorithm == 'political constraints' and list == '3':
    dataframe = call_political_constraints()

if algorithm == 'political constraints' and list != '3':
    print('Political constraint is only applicable to cargolist 3.')

# RANDOM ALL
# dataframe.to_csv(r'../Heuristieken/Outputs/Random/random_all_CL3_100000.csv')

# HILL CLIMBER (SPECIFY PARCEL OR SPACECRAFT SWITCH)
# iterations_dataframe.to_csv(r'../Heuristieken/Outputs/Hill_Climber/iterations_spacecrafts30x2000.csv')
# runs_dataframe.to_csv(r'../Heuristieken/Outputs/Hill_Climber/runs_spacecrafts30x2000.csv')

# SIMULATED ANNEALING (nog geen runs dataframe)
# iterations_dataframe.to_csv(r'../Heuristieken/Outputs/Simulated_Annealing/iterations.csv')

# POLITICAL CONSTRAINTS
# dataframe.to_csv(r'../Heuristieken/Outputs/Random/political.csv')
