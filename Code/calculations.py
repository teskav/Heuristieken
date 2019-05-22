# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
Script to sort and calculate differences
"""
import pandas as pd
import sys

if sys.argv[1] == 'sort':
    """
    Script to sort the solutions of the random algorithm and calculate how often
    a spacecraft is sent per solution
    """
    # import csv data from algorithm
    output_location = '/Random/CL1_100000.csv'
    random = pd.read_csv('../Outputs' + output_location, index_col=0)

    # only select the interesting columns
    random_costs_fleet = random[['costs_solution', 'fleet']]

    # sort the columns by fleet
    sorted = random_costs_fleet.sort_values(by='costs_solution')

    for s in sorted['fleet']:
        sorted.loc[sorted['fleet'] == s, 'Cygnus'] = s.count('Cygnus')
        sorted.loc[sorted['fleet'] == s, 'Progress'] = s.count('Progress')
        sorted.loc[sorted['fleet'] == s, 'Kounotori'] = s.count('Kounotori')
        sorted.loc[sorted['fleet'] == s, 'Dragon'] = s.count('Dragon')

    print(sorted)
    sorted.to_csv(r'../Outputs/Random/sorted_part2.csv')

if sys.argv[1] == 'differences':
    """
    Script to calculate the costs improvements per hill climber run
    """
    output_location = '../Outputs/Hill_Climber/runs_spacecrafts_CL1_30x2000.csv'
    data = pd.read_csv(output_location, index_col=0)

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

else:
    print('Please give imput argument:\n  sort \n  differences')
