# Heuristieken
# April - May 2019
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
        \n hill climber \n simulated annealing")
# only print political constraint choice for cargolist 3
if list == '3':
    print(" political constraints")

algorithm = input("\nPlease give algorithm: ")

# set iterations dataframe to None and change if iterative algorithm
iterations_dataframe = None

# call right algorithm based on users input and save dataframe
if algorithm == 'first fit':
    print("\nHeuristic options: \n normal \n sorted mass \n sorted vol")
    heuristic = input("\nPlease give heuristic: ")
    runs_dataframe = call_first_fit(heuristic)

elif algorithm == 'random':
    runs_dataframe = call_random()

elif algorithm == 'random fleet':
    runs_dataframe = call_random_fleet()

elif algorithm == 'pseudo greedy random':
    runs_dataframe = call_pseudo_greedy_random()

elif algorithm == 'hill climber':
    print("\nNeighbour solution options: \n parcels \n spacecrafts \n combined")
    heuristic = input("\nPlease give neighbour solution: ")
    iterations_dataframe, runs_dataframe = call_hill_climber(heuristic)

elif algorithm == 'simulated annealing':
    print("\nNeighbour solution options: \n parcels \n combined")
    heuristic = input("\nPlease give neighbour solution: ")
    print("\nCooling scheme options: \n lineair \n exponential \n sigmoidal")
    cooling = input("\nPlease give cooling scheme: ")
    iterations_dataframe, runs_dataframe = call_simulated_annealing(heuristic, \
                                                                    cooling)

elif algorithm == 'political constraints' and list == '3':
    runs_dataframe = call_political_constraints()

elif algorithm == 'political constraints' and list != '3':
    print('Political constraint is only applicable to cargolist 3.')

else:
    print("This is not an option.")
    exit()

# check imput arguments
if len(sys.argv) > 1:
    if sys.argv[1] == 'save':
        # save runs
        runs_dataframe.to_csv(r'../Heuristieken/Outputs/Results_fleet/HC_runs_saved.csv')
        # if iterative, save iterations dataframe also
        if algorithm == 'hill climber' or algorithm == 'simulated annealing':
            iterations_dataframe.to_csv(r'../Heuristieken/Outputs/Results_fleet/HC_iterations_saved.csv')
