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
print("Algorithm options: \n first fit \n random \n pseudo greedy random \
        \n hill climber \n hill climber spacecrafts \n hill climber combined \
        \n simulated annealing")
# only print political constraint choice for cargolist 3
if list == '3':
    print(" political constraints")

algorithm = input("\nPlease give algorithm: ")

# set iterations dataframe to None and change if iterative algorithm
iterations_dataframe = None

# call right algorithm based on users input and save dataframe
if algorithm == 'first fit':
    print("Heuristic options: \n normal \n sorted mass \n sorted vol")
    heuristic = input("\nPlease give heuristic: ")
    dataframe = call_first_fit(heuristic)

if algorithm == 'random':
    runs_dataframe = call_random_all()

if algorithm == 'pseudo greedy random':
    runs_dataframe = call_pseudo_greedy_random_all()

if algorithm == 'hill climber':
    print("Neighbour solution options: \n parcels \n spacecrafts \n combined")
    heuristic = input("\nPlease give neighbour solution: ")
    iterations_dataframe, runs_dataframe = call_hill_climber(heuristic)

if algorithm == 'hill climber spacecrafts':
    iterations_dataframe, runs_dataframe = call_hill_climber_spacecrafts()

if algorithm == 'hill climber combined':
    runs_dataframe = call_hill_climber_combined()

if algorithm == 'simulated annealing':
    iterations_dataframe, runs_dataframe = call_simulated_annealing()

if algorithm == 'political constraints' and list == '3':
    runs_dataframe = call_political_constraints()

if algorithm == 'political constraints' and list != '3':
    print('Political constraint is only applicable to cargolist 3.')

# check imput arguments
if len(sys.argv) > 1:
    if sys.argv[1] == 'save':
        # save runs
        runs_dataframe.to_csv(r'../Heuristieken/Outputs/runs_saved.csv')
        # if iterative, save iterations dataframe also
        if not iterations_dataframe == None:
            iterations_dataframe.to_csv(r'../Heuristieken/Outputs/iterations_saved.csv')


# RANDOM convert dataframe to csv
# dataframe.to_csv(r'../Heuristieken/Outputs/Random/random_CL2_100000.csv')

# HILL CLIMBER (SPECIFY PARCEL OR SPACECRAFT SWITCH)
# iterations_dataframe.to_csv(r'../Heuristieken/Outputs/Hill_Climber/iterations_spacecrafts_CL1_30x2000.csv')
# runs_dataframe.to_csv(r'../Heuristieken/Outputs/Hill_Climber/runs_spacecrafts_CL1_30x2000.csv')

# SIMULATED ANNEALING
# iterations_dataframe.to_csv(r'../Heuristieken/Outputs/Simulated_Annealing/iterations_SA_CL1_lin_30x2000.csv')
# runs_dataframe.to_csv(r'../Heuristieken/Outputs/Simulated_Annealing/runs_SA_CL1_lin_30x2000.csv')

# POLITICAL CONSTRAINTS
# dataframe.to_csv(r'../Heuristieken/Outputs/Political_Constraints/CL3_10000.csv')
