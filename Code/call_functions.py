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

def call_random():
    """
    Calls the random algorithm, not taking all parcels
    """
    iterations_dataframe = pd.DataFrame()
    max_iterations = 1000
    count = 0
    best_solution = random_algorithm()
    dataframe_row = spacefreight.save_iteration(best_solution, count)
    iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

    while count < max_iterations:
        count += 1
        solution = random_algorithm()

        # save to dataframe
        dataframe_row = spacefreight.save_iteration(solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

        # check if costs better
        if solution.not_bring < best_solution.not_bring:
            best_solution = solution
        elif solution.not_bring == best_solution.not_bring and solution.costs < best_solution.costs:
            best_solution = solution

    print("Iterations:", count)
    spacefreight.printing(best_solution)

    return iterations_dataframe

def call_pseudo_greedy_random():
    """
    Calls the constrained algorithm, not taking all parcels
    """
    iterations_dataframe = pd.DataFrame()
    max_iterations = 1000
    count = 0
    best_solution = pseudo_greedy_random()
    dataframe_row = spacefreight.save_iteration(best_solution, count)
    iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

    while count < max_iterations:
        count += 1
        solution = pseudo_greedy_random()

        # save to dataframe
        dataframe_row = spacefreight.save_iteration(solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

        # check if costs better
        if solution.not_bring < best_solution.not_bring:
            best_solution = solution
        elif solution.not_bring == best_solution.not_bring and solution.costs < best_solution.costs:
            best_solution = solution

    print("Iterations:", count)
    spacefreight.printing(best_solution)

    return iterations_dataframe

def call_random_all():
    """
    Calls the random algorithm, taking all parcels
    """
    column_names = ['algorithm_name', 'costs_solution', 'fleet', 'costs_spacecraft', 'packed_mass_vol', 'packed_parcels']
    runs_dataframe = pd.DataFrame()

    max_runs = 10
    # run all parcels random
    best_solution = random_all_parcels()
    count = 0
    dataframe_row = spacefreight.save_run_random(best_solution)
    runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

    while count < max_runs:
        count += 1
        solution = random_all_parcels()

        # save to dataframe
        dataframe_row = spacefreight.save_run_random(solution)
        runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

        # check if costs better
        if solution.costs < best_solution.costs:
            best_solution = solution

    # print("Iterations:", count)
    # spacefreight.printing(best_solution)

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
    iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

    while count < max_iterations:
        count += 1
        solution = pseudo_greedy_random_all()

        # save to dataframe
        dataframe_row = spacefreight.save_iteration(solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

        # check if costs better
        if solution.costs < best_solution.costs:
            best_solution = solution

    print("Iterations:", count)
    spacefreight.printing(best_solution)

    return iterations_dataframe

def call_hill_climber():
    """
    Calls the hill climber algorithm SWAP PARCELS
    """
    column_names_runs = ['algorithm_name', 'iterations', 'start_solution_costs', 'end_solution_costs', 'start_fleet', 'end_fleet', 'start_costs_spacecraft', 'start_packed_mass_vol', 'start_packed_parcels', 'end_costs_spacecraft', 'end_packed_mass_vol', 'end_packed_parcels']
    column_names_iterations = ['algorithm_name', 'iteration', 'costs_solution', 'fleet', 'costs_spacecraft', 'packed_mass_vol', 'packed_parcels']
    iterations_dataframe = pd.DataFrame()
    runs_dataframe = pd.DataFrame()

    max_iterations = 10
    runs = 0
    max_runs = 20

    # set lists for plots
    costs_runs = []
    x = list(range(max_iterations))

    # # HILL CLIMBER 1 keer
    # iterations_dataframe, count, current_solution = hill_climber(iterations_dataframe, max_iterations)
    #
    # print("Iterations:", count)
    # spacefreight.printing(current_solution)

    # HILL CLIMBER max_runs aantal keer en per running max_iterations
    while runs < max_runs:

        iterations_dataframe, start_solution, end_solution, costs_per_run = hill_climber(iterations_dataframe, max_iterations)

        # save run
        dataframe_row = spacefreight.save_run_hill_climber(start_solution, end_solution, max_iterations)
        runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

        # data for plots
        costs_runs.append(costs_per_run)

        runs += 1

    # plot
    for i in list(range(max_runs)):
        plt.plot(x, costs_runs[i])
    plt.xlabel('Iterations')
    plt.ylabel('Costs')
    plt.title('Behaviour of the hillclimber in different runs')
    plt.show()

    # set column names
    runs_dataframe.columns = column_names_runs
    iterations_dataframe.columns = column_names_iterations

    return iterations_dataframe, runs_dataframe

def call_hill_climber_spacecrafts():
    """
    Calls the hill climber algorithm SWAP SPACECRAFTS
    """
    column_names_runs = ['algorithm_name', 'iterations', 'start_solution_costs', 'end_solution_costs', 'start_fleet', 'end_fleet', 'start_costs_spacecraft', 'start_packed_mass_vol', 'start_packed_parcels', 'end_costs_spacecraft', 'end_packed_mass_vol', 'end_packed_parcels']
    column_names_iterations = ['algorithm_name', 'iteration', 'costs_solution', 'fleet', 'costs_spacecraft', 'packed_mass_vol', 'packed_parcels']
    iterations_dataframe = pd.DataFrame()
    runs_dataframe = pd.DataFrame()

    max_iterations = 100
    runs = 0
    max_runs = 10

    # set lists for plots
    costs_runs = []
    x = list(range(max_iterations))


    # HILL CLIMBER max_runs aantal keer en per running max_iterations aantal iteraties
    while runs < max_runs:

        iterations_dataframe, start_solution, end_solution, costs_per_run = hill_climber_spacecrafts(iterations_dataframe, max_iterations)
        # plt.plot(x, solution)
        # plt.xlabel('Iterations')
        # plt.ylabel('Costs')
        # plt.title('Distribution of solutions per run')
        # plt.show()

        # save run
        dataframe_row = spacefreight.save_run_hill_climber(start_solution, end_solution, max_iterations)
        runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

        # data for plots
        costs_runs.append(costs_per_run)

        runs += 1

    # plot
    for i in list(range(max_runs)):
        plt.plot(x, costs_runs[i])
    plt.xlabel('Iterations')
    plt.ylabel('Costs')
    plt.title('Behaviour of the hillclimber in different runs')
    plt.show()

    # set column names
    runs_dataframe.columns = column_names_runs
    iterations_dataframe.columns = column_names_iterations

    return iterations_dataframe, runs_dataframe

def call_hill_climber_combined():
    """
    Calls the hill climber swapping spacecrafts and parcels
    """
    iterations_dataframe = pd.DataFrame()
    max_iterations = 1000

    # HILL CLIMBER max_runs aantal keer en per running max_iterations aantal iteraties
    runs = 0
    max_runs = 20
    solutions_runs = []
    solutions = []
    x = list(range(max_iterations))
    while runs < max_runs:
        iterations_dataframe, count, current_solution, solution = hill_climber_combined(iterations_dataframe, max_iterations)
        plt.plot(x, solution)
        plt.xlabel('Iterations')
        plt.ylabel('Costs')
        plt.title('Distribution of solutions per run')
        plt.show()
        solutions_runs.append(current_solution.costs)
        solutions.append(solution)
        runs += 1

    print("Iterations:", count)
    spacefreight.printing(current_solution)

    plt.plot(list(range(max_runs)), solutions_runs, color='skyblue')
    plt.xlabel('Runs')
    plt.ylabel('Costs')
    plt.title('Distributions of costs over the hill_climbers')
    plt.show()

    for i in list(range(max_runs)):
        plt.plot(x, solutions[i])
    plt.xlabel('Iterations')
    plt.ylabel('Costs (in billion dollars)')
    plt.title('Behaviour of the hillclimber in different solutions')
    plt.show()

    return iterations_dataframe

def call_simulated_annealing():
    """
    Calls the simulated annealing algorithm
    """
    column_names_iterations = ['algorithm_name', 'iteration', 'costs_solution', 'temperature', 'acceptation_chance', 'fleet', 'costs_spacecraft', 'packed_mass_vol', 'packed_parcels']
    iterations_dataframe = pd.DataFrame()
    max_iterations = 100

    # SIMULATED ANNEALING
    iterations_dataframe, count, current_solution = simulated_annealing(iterations_dataframe, max_iterations)
    # temperature = cooling_scheme(count, max_iterations)

    # print("Iterations:", count)
    # spacefreight.printing(current_solution)

    plot_costs(iterations_dataframe)
    plot_cooling(iterations_dataframe)
    plot_acceptatie(iterations_dataframe)

    # set column names
    iterations_dataframe.columns = column_names_iterations

    return iterations_dataframe

def call_simulated_annealing_combined():
    """
    Calls the simulated annealing swapping spacecrafts and parcels
    """
    iterations_dataframe = pd.DataFrame()
    max_iterations = 100

    # SIMULATED ANNEALING
    iterations_dataframe, count, current_solution = simulated_annealing(iterations_dataframe, max_iterations)
    # temperature = cooling_scheme(count, max_iterations)

    print("Iterations:", count)
    spacefreight.printing(current_solution)

    plot_costs(iterations_dataframe)
    plot_cooling(iterations_dataframe)
    plot_acceptatie(iterations_dataframe)

    return iterations_dataframe

def call_political_constraints():

    runs_dataframe = pd.DataFrame()
    max_runs = 1
    count = 0

    while count < max_runs:

        # set up dataframe with all countries and number of spacecrafts used
        data = [['USA', 0], ['Russia', 0], ['Japan', 0], ['China', 0], ['Europe', 0]]
        countries = pd.DataFrame(data, columns = ['country', 'spacecrafts'])

        solution = political_constraints(countries)

        # save run data and put in runs dataframe
        dataframe_row = spacefreight.save_iteration(solution, count)
        runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

        count +=1

    # print minimal costs from dataframe
    print(runs_dataframe.iloc[:, 2].min())

    # plot alle oplossingen samen
    plot_costs(runs_dataframe)
    # # plot voor de vloot
    # runs_high_costs = runs_dataframe[runs_dataframe.iloc[:, 2]>2460000000]
    # plot_costs(runs_high_costs)

    return runs_dataframe
