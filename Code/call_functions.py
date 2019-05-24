# HEURISTIEKEN
# April - May 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script is used for calling functions from the main
"""

from spacefreight import SpaceFreight
from random_algorithms import *
from first_fit_algorithms import *
from hill_climber import *
from simulated_annealing import *
from plot import *
import pandas as pd

spacefreight = SpaceFreight()

def call_first_fit(heuristic):
    """
    Calls the first fit algorithm
    """
    iterations_dataframe = pd.DataFrame()
    current_solution = first_fit(heuristic)

    # save to dataframe
    dataframe_row = spacefreight.save_iteration(current_solution, 0)
    iterations_dataframe = iterations_dataframe.append(dataframe_row, \
                            ignore_index=True)

    # print solution
    spacefreight.printing(current_solution)

    return iterations_dataframe

def call_random():
    """
    Calls the random algorithm.
    """
    column_names = ['algorithm_name', 'costs_solution', 'fleet', \
                    'costs_spacecraft', 'packed_mass_vol', 'packed_parcels']
    runs_dataframe = pd.DataFrame()

    max_runs = 10
    # run all parcels random
    best_solution = random_algorithm()
    count = 0
    dataframe_row = spacefreight.save_run_random(best_solution)
    runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

    while count < (max_runs - 1):
        solution = random_algorithm()

        # save to dataframe
        dataframe_row = spacefreight.save_run_random(solution)
        runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

        # check if costs better
        if solution.costs < best_solution.costs:
            best_solution = solution

        count += 1

    # print the best solution in terminal
    spacefreight.printing(best_solution)

    # set column names
    runs_dataframe.columns = column_names

    # plot if more than 1 run
    if max_runs > 1:
        plot_costs(runs_dataframe)

    return runs_dataframe

def call_pseudo_greedy_random():
    """
    Calls the pseudo greedy random algorithm (with constraints).
    """
    column_names = ['algorithm_name', 'costs_solution', 'fleet', \
                    'costs_spacecraft', 'packed_mass_vol', 'packed_parcels']
    runs_dataframe = pd.DataFrame()

    max_runs = 1
    # run all parcels random
    best_solution = pseudo_greedy_random()
    count = 0
    dataframe_row = spacefreight.save_run_random(best_solution)
    runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

    while count < (max_runs - 1):
        solution = pseudo_greedy_random()

        # save to dataframe
        dataframe_row = spacefreight.save_run_random(solution)
        runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

        # check if costs better
        if solution.costs < best_solution.costs:
            best_solution = solution

        count += 1

    # print the best solution in terminal
    spacefreight.printing(best_solution)

    # set column names
    runs_dataframe.columns = column_names

    # plot if more than 1 run
    if max_runs > 1:
        plot_costs(runs_dataframe)

    return runs_dataframe

def call_hill_climber(heuristic):
    """
    Calls the hill climber algorithm SWAP PARCELS
    """
    column_names_runs=['algorithm_name', 'iterations', 'start_solution_costs', \
                        'end_solution_costs', 'start_fleet', \
                        'start_costs_spacecraft', 'start_packed_mass_vol', \
                        'start_packed_parcels', 'end_fleet', \
                        'end_costs_spacecraft', 'end_packed_mass_vol', \
                        'end_packed_parcels']
    column_names_iterations=['algorithm_name', 'iteration', 'costs_solution', \
                            'fleet', 'costs_spacecraft', 'packed_mass_vol', \
                            'packed_parcels']
    iterations_dataframe = pd.DataFrame()
    runs_dataframe = pd.DataFrame()

    max_iterations = 2000
    runs = 0
    max_runs = 1

    # set lists for plots
    costs_runs = []

    # HILL CLIMBER max_runs number of times and max_iterations per run
    while runs < max_runs:

        iterations_dataframe, start_solution, end_solution, costs_per_run = \
            hill_climber(iterations_dataframe, max_iterations, heuristic)

        # save run
        dataframe_row = spacefreight.save_run_hill_climber(start_solution, \
                        end_solution, max_iterations)
        runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

        # data for plots
        costs_runs.append(costs_per_run)

        runs += 1

    # set column names
    runs_dataframe.columns = column_names_runs
    iterations_dataframe.columns = column_names_iterations

    # plot
    plot_iterative(max_iterations, costs_runs)

    # print the best solution in terminal
    spacefreight.printing(end_solution)

    return iterations_dataframe, runs_dataframe

def call_simulated_annealing(heuristic, cooling):
    """
    Calls the simulated annealing algorithm
    """
    column_names_runs=['algorithm_name', 'iterations', 'start_solution_costs', \
                        'end_solution_costs', 'start_fleet', \
                        'start_costs_spacecraft', 'start_packed_mass_vol', \
                        'start_packed_parcels', 'end_fleet', \
                        'end_costs_spacecraft', 'end_packed_mass_vol', \
                        'end_packed_parcels']
    column_names_iterations=['algorithm_name', 'iteration', 'costs_solution', \
                            'temperature', 'acceptance', 'fleet', \
                            'costs_spacecraft', 'packed_mass_vol', \
                            'packed_parcels']

    iterations_dataframe = pd.DataFrame()
    runs_dataframe = pd.DataFrame()

    max_iterations = 2000
    runs = 0
    max_runs = 1

    # set lists for plots
    costs_runs = []

    # SIMULATED ANNEALING max_runs number of times and max_iterations per run
    while runs < max_runs:

        iterations_dataframe, start_solution, end_solution, costs_per_run = \
            simulated_annealing(iterations_dataframe, max_iterations, \
                                 heuristic, cooling)

        # save run
        dataframe_row = spacefreight.save_run_hill_climber(start_solution, \
                        end_solution, max_iterations)
        runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

        # data for plots
        costs_runs.append(costs_per_run)

        runs += 1

    # set column names
    runs_dataframe.columns = column_names_runs
    iterations_dataframe.columns = column_names_iterations

    # plot & print the solution
    plot_iterative(max_iterations, costs_runs)
    spacefreight.printing(end_solution)

    return iterations_dataframe, runs_dataframe

def call_political_constraints():
    """
    Calls the random algorithm, considering the political constraint:
    The difference between the number of spacecrafts per country can be at most1
    """

    column_names = ['algorithm_name', 'costs_solution', 'distribution', \
                    'fleet', 'costs_spacecraft', 'packed_mass_vol', \
                    'packed_parcels']

    runs_dataframe = pd.DataFrame()
    max_runs = 1
    count = 0

    # set up dataframe with all countries and number of spacecrafts used
    data = [['USA', 0], ['Russia', 0], ['Japan', 0], ['China', 0], \
            ['Europe', 0]]
    countries = pd.DataFrame(data, columns = ['country', 'spacecrafts'])

    # set first run as intitial best run
    best_solution, countries = political_constraints(countries)
    dataframe_row = spacefreight.save_run_political(best_solution, countries)
    runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

    while count < (max_runs - 1):

        count += 1

        # set number of spacecrafts to 0 after every run
        countries['spacecrafts'] = 0

        solution, countries = political_constraints(countries)

        # save run data and put in runs dataframe
        dataframe_row = spacefreight.save_run_political(solution, countries)
        runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

        # check if costs better
        if solution.costs < best_solution.costs:
            best_solution = solution

    # set column names
    runs_dataframe.columns = column_names

    # plot if more than 1 run
    if max_runs > 1:
        plot_costs(runs_dataframe)

    spacefreight.printing(best_solution)

    return runs_dataframe
