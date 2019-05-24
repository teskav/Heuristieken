# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
Script to sort and calculate differences
"""
import pandas as pd
import sys

# import csv data from algorithm
output_location = '/Simulated_Annealing/runs_SA_CL1_exp_30x2000.csv'
data = pd.read_csv('../Outputs' + output_location, index_col=0)

# check imput argument
if sys.argv[1] == 'sort':
    """
    Script to sort the solutions of the random algorithm and calculate how often
    a spacecraft is sent per solution
    """

    # only select the interesting columns
    random_costs_fleet = data[['costs_solution', 'fleet']]

    # sort the columns by fleet
    sorted = random_costs_fleet.sort_values(by='costs_solution')

    for s in sorted['fleet']:
        sorted.loc[sorted['fleet'] == s, 'Cygnus'] = s.count('Cygnus')
        sorted.loc[sorted['fleet'] == s, 'Progress'] = s.count('Progress')
        sorted.loc[sorted['fleet'] == s, 'Kounotori'] = s.count('Kounotori')
        sorted.loc[sorted['fleet'] == s, 'Dragon'] = s.count('Dragon')

    print(sorted)
    sorted.to_csv(r'../Outputs/Random/sorted_CL2_100000.csv')

elif sys.argv[1] == 'differences':
    """
    Script to calculate the costs improvements per hill climber or
    simulated annealing run.
    """

    # create dataframe with differences between the start and end costs per run
    differences = data['start_solution_costs']-data['end_solution_costs']

    # calculate the minimum, maximum and average costs
    min_difference = differences.min()
    max_difference = differences.max()
    mean_difference = differences.mean()

    print(differences)
    print('Minimal difference:', min_difference)
    print('Maximal difference:', max_difference)
    print('Average difference:', mean_difference)

elif sys.argv[1] == 'average':
    """
    Script to calculate the average costs per algorithm.
    """
    low = data['end_solution_costs'].min()
    average = data['end_solution_costs'].mean()

    print('The lowest costs are:', low)
    print('The average costs are:', average)

else:
    print('Please give imput argument:\n  sort \n  differences')
