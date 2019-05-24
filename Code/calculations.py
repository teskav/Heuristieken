# Heuristieken
# April - May 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
Script to sort and calculate differences
"""
import pandas as pd
import sys

# check input argument
if len(sys.argv) != 3:
    print('Please give input arguments: file name followed by \
            \n  sort \n  differences (only use for iterative algorithms) \
            \n  average \nExample input argument: example.csv sort')
else:
    # import csv data from algorithm
    output_location = sys.argv[1]
    data = pd.read_csv('../Outputs/' + output_location, index_col=0)

    if sys.argv[2] == 'sort':
        """
        Script to sort the solutions of the random algorithm and calculate
        how often a spacecraft is sent per solution
        """

        # only select the relevant columns
        if 'costs_solution' in data:
            random_costs_fleet = data[['costs_solution', 'fleet']]

            # sort the columns by fleet
            sorted = random_costs_fleet.sort_values(by='costs_solution')

            for s in sorted['fleet']:
                sorted.loc[sorted['fleet'] == s, 'Cygnus'] = \
                    s.count('Cygnus')
                sorted.loc[sorted['fleet'] == s, 'Progress'] = \
                    s.count('Progress')
                sorted.loc[sorted['fleet'] == s, 'Kounotori'] = \
                    s.count('Kounotori')
                sorted.loc[sorted['fleet'] == s, 'Dragon'] = \
                    s.count('Dragon')
        else:
            random_costs_fleet = data[['end_solution_costs', 'end_fleet']]

            # sort the columns by fleet
            sorted = random_costs_fleet.sort_values(by='end_solution_costs')

            for s in sorted['end_fleet']:
                sorted.loc[sorted['end_fleet'] == s, 'Cygnus'] = \
                    s.count('Cygnus')
                sorted.loc[sorted['end_fleet'] == s, 'Progress'] = \
                    s.count('Progress')
                sorted.loc[sorted['end_fleet'] == s, 'Kounotori'] = \
                    s.count('Kounotori')
                sorted.loc[sorted['end_fleet'] == s, 'Dragon'] = \
                    s.count('Dragon')

        sorted.to_csv(r'../Outputs/' + output_location + '_sorted')

    elif sys.argv[2] == 'differences':
        """
        Script to calculate the costs improvements per hill climber or
        simulated annealing run.
        """

        # create dataframe with differences between the start and end costs
        # per run
        differences = data['start_solution_costs']-data['end_solution_costs']

        # calculate and print the minimum, maximum and average costs
        print('Minimal difference:', differences.min())
        print('Maximal difference:', differences.max())
        print('Average difference:', differences.mean())

    elif sys.argv[2] == 'average':
        """
        Script to calculate the average costs per algorithm.
        """
        if 'costs_solution' in data:
            # calculate and print
            print('The lowest costs are:', data['costs_solution'].min())
            print('The average costs are:', data['costs_solution'].mean())
        else:
            # calculate and print
            print('The lowest costs are:', data['end_solution_costs'].min())
            print('The average costs are:', data['end_solution_costs'].mean())

    else:
        print('Please give input argument:\n  sort \n  differences')
