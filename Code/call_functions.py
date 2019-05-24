# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script is used for calling functions from the main
"""

from spacefreight import SpaceFreight
from random_algorithms_new import *
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

def call_random_all():
    """
    Calls the random algorithm, taking all parcels
    """
    column_names = ['algorithm_name', 'costs_solution', 'fleet', \
                    'costs_spacecraft', 'packed_mass_vol', 'packed_parcels']
    runs_dataframe = pd.DataFrame()

    max_runs = 1
    # run all parcels random
    best_solution = random_all_parcels()
    count = 0
    dataframe_row = spacefreight.save_run_random(best_solution)
    runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

    while count < max_runs:
        solution = random_all_parcels()

        # save to dataframe
        dataframe_row = spacefreight.save_run_random(solution)
        runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

        # check if costs better
        if solution.costs < best_solution.costs:
            best_solution = solution

        count += 1

    # plot if more than 1 run
    if max_runs > 1:
        plot_costs(runs_dataframe)

    spacefreight.printing(best_solution)

    # set column names
    runs_dataframe.columns = column_names

    return runs_dataframe

def call_pseudo_greedy_random_all():
    """
    Calls the constrained algorithm, taking all parcels
    """
    iterations_dataframe = pd.DataFrame()
    max_iterations = 1000
    # run all parcels constrained
    best_solution = pseudo_greedy_random_all()
    count = 0
    dataframe_row = spacefreight.save_iteration(best_solution, count)
    iterations_dataframe = iterations_dataframe.append(dataframe_row, \
                            ignore_index=True)

    while count < max_iterations:
        count += 1
        solution = pseudo_greedy_random_all()

        # save to dataframe
        dataframe_row = spacefreight.save_iteration(solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, \
                                ignore_index=True)

        # check if costs better
        if solution.costs < best_solution.costs:
            best_solution = solution

    # plot if more than 1 run
    if max_runs > 1:
        plot_costs(runs_dataframe)        

    spacefreight.printing(best_solution)

    return iterations_dataframe

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
    max_runs = 3

    # set lists for plots
    costs_runs = []

    # HILL CLIMBER max_runs aantal keer en per running max_iterations
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

    # plot
    plot_iterative(max_iterations, costs_runs)

    # set column names
    runs_dataframe.columns = column_names_runs
    iterations_dataframe.columns = column_names_iterations

    spacefreight.printing(end_solution)

    return iterations_dataframe, runs_dataframe

def call_hill_climber_spacecrafts():
    """
    Calls the hill climber algorithm SWAP SPACECRAFTS
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
    max_runs = 30

    # set lists for plots
    costs_runs = []
    x = list(range(max_iterations))


    # HILL CLIMBER max_runs aantal keer en
    # per running max_iterations aantal iteraties
    while runs < max_runs:

        iterations_dataframe, start_solution, end_solution, costs_per_run = \
            hill_climber_spacecrafts(iterations_dataframe, max_iterations)

        # save run
        dataframe_row = spacefreight.save_run_hill_climber(start_solution, \
                        end_solution, max_iterations)
        runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

        # data for plots
        costs_runs.append(costs_per_run)

        runs += 1

    # plot & print
    plot_iterative(max_iterations, costs_runs)
    spacefreight.printing(end_solution)

    # set column names
    runs_dataframe.columns = column_names_runs
    iterations_dataframe.columns = column_names_iterations

    return iterations_dataframe, runs_dataframe

def call_hill_climber_combined():
    """
    Calls the hill climber swapping spacecrafts and parcels
    """
    iterations_dataframe = pd.DataFrame()
    max_iterations = 2000

    # HILL CLIMBER max_runs aantal keer en
    # per running max_iterations aantal iteraties
    runs = 0
    max_runs = 2
    solutions_runs = []
    solutions = []
    x = list(range(max_iterations))
    while runs < max_runs:
        iterations_dataframe, count, current_solution, solution = \
            hill_climber_combined(iterations_dataframe, max_iterations)
        solutions_runs.append(current_solution.costs)
        solutions.append(solution)
        runs += 1

    print("Iterations:", count)
    spacefreight.printing(current_solution)

    # plot & print
    plot_iterative(max_iterations, costs_runs)
    spacefreight.printing(end_solution)

    return iterations_dataframe

def call_simulated_annealing():
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
    max_runs = 30

    # set lists for plots
    costs_runs = []
    x = list(range(max_iterations))

    # SIMULATED ANNEALING max_runs aantal keer en per running max_iterations
    while runs < max_runs:

        iterations_dataframe, start_solution, end_solution, costs_per_run = \
            simulated_annealing(iterations_dataframe, max_iterations)

        # save run
        dataframe_row = spacefreight.save_run_hill_climber(start_solution, \
                        end_solution, max_iterations)
        runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

        # data for plots
        costs_runs.append(costs_per_run)

        runs += 1

    # plot & print
    plot_iterative(max_iterations, costs_runs)
    spacefreight.printing(end_solution)

    # set column names
    runs_dataframe.columns = column_names_runs
    iterations_dataframe.columns = column_names_iterations

    # plot_cooling(iterations_dataframe)
    # plot_acceptatie(iterations_dataframe)

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

    while count < max_runs:

        # set up dataframe with all countries and number of spacecrafts used
        data = [['USA', 0], ['Russia', 0], ['Japan', 0], ['China', 0], \
                ['Europe', 0]]
        countries = pd.DataFrame(data, columns = ['country', 'spacecrafts'])

        solution, countries = political_constraints(countries)

        # save run data and put in runs dataframe
        dataframe_row = spacefreight.save_run_political(solution, countries)
        runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

        count +=1

    # set column names
    runs_dataframe.columns = column_names

    # plot if more than 1 run
    if max_runs > 1:
        plot_costs(runs_dataframe)

    spacefreight.printing(solution)

    return runs_dataframe
