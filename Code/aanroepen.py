from parcel import Parcel
from spacecraft import Spacecraft
from spacefreight import SpaceFreight
from random_algorithms_new import *
from first_fit_algorithms import *
from iterative_algorithms_new import *
from hill_climber import *
from simulated_annealing import *
from plot import *
import pandas as pd

spacefreight = SpaceFreight()

def aanroepen_random():
    iterations_dataframe = pd.DataFrame()
    max_iterations = 100
    count = 0
    best_solution = random_greedy()
    dataframe_row = spacefreight.save_iteration(best_solution, count)
    iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

    while count < max_iterations:
        count += 1
        solution = random_greedy()

        # save to dataframe
        dataframe_row = spacefreight.save_iteration(solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

        # add number of packed parcels of solution to list to plot
        # plot_parcels.append(len(spacefreight.all_parcels)-solution.not_bring)

        # check if costs better
        if solution.not_bring < best_solution.not_bring:
            best_solution = solution
        elif solution.not_bring == best_solution.not_bring and solution.costs < best_solution.costs:
            best_solution = solution

    print("Iterations:", count)
    spacefreight.printing(best_solution)

    return iterations_dataframe

def aanroepen_constrained():
    iterations_dataframe = pd.DataFrame()
    max_iterations = 100
    count = 0
    best_solution = random_constraints()
    dataframe_row = spacefreight.save_iteration(best_solution, count)
    iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

    while count < max_iterations:
        count += 1
        solution = random_constraints()

        # save to dataframe
        dataframe_row = spacefreight.save_iteration(solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

        # add number of packed parcels of solution to list to plot
        # plot_parcels.append(len(spacefreight.all_parcels)-solution.not_bring)

        # check if costs better
        if solution.not_bring < best_solution.not_bring:
            best_solution = solution
        elif solution.not_bring == best_solution.not_bring and solution.costs < best_solution.costs:
            best_solution = solution

    print("Iterations:", count)
    spacefreight.printing(best_solution)

    return iterations_dataframe

def aanroepen_random_all():
    iterations_dataframe = pd.DataFrame()
    max_iterations = 100
    # run all parcels random
    best_solution = random_all_parcels()
    count = 0
    dataframe_row = spacefreight.save_iteration(best_solution, count)
    iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

    while count < max_iterations:
        count += 1
        solution = random_all_parcels()

        # save to dataframe
        dataframe_row = spacefreight.save_iteration(solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

        # check if costs better
        if solution.costs < best_solution.costs:
            best_solution = solution

    print("Iterations:", count)
    spacefreight.printing(best_solution)

    return iterations_dataframe

def aanroepen_constrained_all():
    iterations_dataframe = pd.DataFrame()
    max_iterations = 100
    # run all parcels constrained
    best_solution = random_constraints_all()
    count = 0
    dataframe_row = spacefreight.save_iteration(best_solution, count)
    iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

    while count < max_iterations:
        count += 1
        solution = random_constraints_all()

        # save to dataframe
        dataframe_row = spacefreight.save_iteration(solution, count)
        iterations_dataframe = iterations_dataframe.append(dataframe_row, ignore_index=True)

        # check if costs better
        if solution.costs < best_solution.costs:
            best_solution = solution

    print("Iterations:", count)
    spacefreight.printing(best_solution)

    return iterations_dataframe

def aanroepen_hill_climber():
    iterations_dataframe = pd.DataFrame()
    max_iterations = 2000

    # # HILL CLIMBER 1 keer
    # iterations_dataframe, count, current_solution = hill_climber(iterations_dataframe, max_iterations)
    #
    # print("Iterations:", count)
    # spacefreight.printing(current_solution)

    # HILL CLIMBER max_runnings aantal keer en per running max_iterations aantal iteraties
    runnings = 0
    max_runnings = 30
    solutions_runnings = []
    solutions = []
    x = list(range(max_iterations))
    while runnings < max_runnings:
        iterations_dataframe, count, current_solution, solution = hill_climber(iterations_dataframe, max_iterations)
        plt.plot(x, solution)
        plt.xlabel('Iterations')
        plt.ylabel('Costs (in billion dollars)')
        plt.title('Distribution of solutions per running')
        plt.show()
        solutions_runnings.append(current_solution.costs)
        solutions.append(solution)
        runnings += 1

    plt.plot(list(range(max_runnings)), solutions_runnings, color='skyblue')
    plt.xlabel('Runnings')
    plt.ylabel('Costs (in billion dollars)')
    plt.title('Distributions of costs over the hill_climbers')
    plt.show()

    for i in list(range(max_runnings)):
        plt.plot(x, solutions[i])
    plt.xlabel('Iterations')
    plt.ylabel('Costs (in billion dollars)')
    plt.title('Behaviour of the hillclimber in different solutions')
    plt.show()




    return iterations_dataframe

def aanroepen_simulated_annealing():
    iterations_dataframe = pd.DataFrame()
    max_iterations = 50

    # SIMULATED ANNEALING
    iterations_dataframe, count, current_solution = simulated_annealing(iterations_dataframe, max_iterations)

    print("Iterations:", count)
    spacefreight.printing(current_solution)

    plot_costs(iterations_dataframe)

    return iterations_dataframe
