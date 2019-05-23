# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
Main script, used to process the call for functions in the terminal
Main script, used to process the call for functions in the terminal.
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

# print the algorithm options
print("")
print("Algorithm options: \n first fit \n first fit sorted mass \
        \n first fit sorted vol \n random \n pseudo greedy random \
        \n hill climber \n hill climber spacecrafts \n hill climber combined \
        \n simulated annealing")
# only print political constraint choice for cargolist 3
if list == '3':
    print(" political constraints")

algorithm = input("\nPlease give algorithm: ")

# call right algorithm based on users input and save dataframe
if algorithm == 'first fit':
    dataframe = call_first_fit()

if algorithm == 'first fit sorted mass':
    dataframe = call_first_fit_sorted_mass()

if algorithm == 'first fit sorted vol':
    dataframe = call_first_fit_sorted_vol()

if algorithm == 'random':
    dataframe = call_random_all()

if algorithm == 'pseudo greedy random':
    dataframe = call_pseudo_greedy_random_all()

if algorithm == 'hill climber':
    iterations_dataframe, runs_dataframe = call_hill_climber()

if algorithm == 'hill climber spacecrafts':
    iterations_dataframe, runs_dataframe = call_hill_climber_spacecrafts()

if algorithm == 'hill climber combined':
    dataframe = call_hill_climber_combined()

if algorithm == 'simulated annealing':
    iterations_dataframe, runs_dataframe = call_simulated_annealing()

if algorithm == 'political constraints' and list == '3':
    dataframe = call_political_constraints()

if algorithm == 'political constraints' and list != '3':
    print('Political constraint is only applicable to cargolist 3.')

# RANDOM ALL
# dataframe.to_csv(r'../Heuristieken/Outputs/Random/random_CL1_100000.csv')
# RANDOM convert dataframe to csv
# dataframe.to_csv(r'../Heuristieken/Outputs/Random/random_CL2_100000.csv')

# HILL CLIMBER (SPECIFY PARCEL OR SPACECRAFT SWITCH)
# HILL CLIMBER (SPECIFY PARCEL OR SPACECRAFT SWITCH) convert dataframe to csv
# iterations_dataframe.to_csv(r'../Heuristieken/Outputs/Hill_Climber/iterations_parcels_CL1_10x2000.csv')
# runs_dataframe.to_csv(r'../Heuristieken/Outputs/Hill_Climber/runs_parcels_CL1_10x2000.csv')

# SIMULATED ANNEALING
# SIMULATED ANNEALING convert dataframe to csv
# iterations_dataframe.to_csv(r'../Heuristieken/Outputs/Simulated_Annealing/iterations_SA_CL1_lin_30x2000.csv')
# runs_dataframe.to_csv(r'../Heuristieken/Outputs/Simulated_Annealing/runs_SA_CL1_lin_30x2000.csv')

# POLITICAL CONSTRAINTS
# POLITICAL CONSTRAINTS convert dataframe to csv
# dataframe.to_csv(r'../Heuristieken/Outputs/Political_Constraints/CL3_10000.csv')
