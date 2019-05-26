# Heuristieken
# April - May 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script gives us outputs for our presentation
"""

import pandas as pd
from spacecraft import Spacecraft
from solution import Solution
from helpers import *
from plot import *
import math
INPUT = "CargoLists/CargoList1.csv"

data = pd.read_csv('../Outputs/Random/random_CL1_100000.csv', index_col=0)

optimal_fleet = data[data['costs_solution'] < 1600000000]

spacecrafts_list = []
spacecrafts_list.append(Spacecraft('Progress', 2400, 7.6, 7020, \
                            175000000, 0.74, 'Russia'))
spacecrafts_list.append(Spacecraft('Progress', 2400, 7.6, 7020, \
                            175000000, 0.74, 'Russia'))
spacecrafts_list.append(Spacecraft('Progress', 2400, 7.6, 7020, \
                            175000000, 0.74, 'Russia'))
spacecrafts_list.append(Spacecraft('Progress', 2400, 7.6, 7020, \
                            175000000, 0.74, 'Russia'))
spacecrafts_list.append(Spacecraft('Progress', 2400, 7.6, 7020, \
                            175000000, 0.74, 'Russia'))
spacecrafts_list.append(Spacecraft('Progress', 2400, 7.6, 7020, \
                            175000000, 0.74, 'Russia'))
spacecrafts_list.append(Spacecraft('Dragon', 6000, 10, 12200, \
                            347000000, 0.72, 'USA'))

parcel_list = load_parcels(INPUT)
print(parcel_list)

max_runs = 1
# run all parcels random
best_solution = random_algorithm()
count = 0
dataframe_row = save_run_random(best_solution)
runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

while count < (max_runs - 1):
    solution = random_algorithm()

    # save to dataframe
    dataframe_row = save_run_random(solution)
    runs_dataframe = runs_dataframe.append(dataframe_row, ignore_index=True)

    # check if costs better
    if solution.costs < best_solution.costs:
        best_solution = solution

    count += 1

# print the best solution in terminal
printing(best_solution)

# set column names
runs_dataframe.columns = column_names

# plot if more than 1 run
if max_runs > 1:
    plot_costs(runs_dataframe)

print(runs_dataframe)


def random_algorithm():
    """
    Random allocate the parcels in spacecrafts
    """
    # set starting settings random
    parcel_randoms = random.sample(range(100, 100))
    spacecraft_randoms = random.sample(7,7)
    used_spacecrafts = []
    total_costs = 0
    # every single run of the function sets unpacked_parcels at starting point
	unpacked = []
  	for p in parcel_list:
  		unpacked.append(p.ID)


    while len(unpacked) > 0:
        for spacecraft_number in spacecraft_randoms:
	        spacecraft = spacecrafts_list[spacecraft_number]

	        # set variables at 0
	        empty_single_spacecraft(spacecraft)

	        for parcel_number in parcel_randoms:
	            parcel = parcel_list[parcel_number]
	            if (check(spacecraft, parcel) and
	                    parcel.ID in unpacked):
	                spacecraft = update(spacecraft, parcel)

	        #calculate costs spacecraft
	        spacecraft.costs = calculate_costs_spacecraft(spacecraft)
	        total_costs += spacecraft.costs

        # add spacecraft to used_spacecrafts
        used_spacecrafts.append(spacecraft)

    # save solution
    current_solution = Solution('random all', total_costs, used_spacecrafts)

    return current_solution


def load_parcels(file):
    """
    Load parcels from csv file.
    Returns a list with Parcel objects.
    """
    with open(INPUT) as in_file:
        data_frame = csv.reader(in_file, delimiter = ',')
        next(data_frame)
        parcels = []
        for parcel in data_frame:
            name = parcel[0]
            parcel = Parcel(parcel[0], float(parcel[1]), float(parcel[2]))
            parcels.append(parcel)

    return parcels

def check(self, spacecraft, parcel):
        """
        Checks if payload mass and volume of spacecraft doesn't get exceeded.
        Boolean.
        """
        if ((spacecraft.packed_mass+parcel.mass) < spacecraft.payload_mass and
                (spacecraft.packed_vol+parcel.volume) < spacecraft.payload_vol):
            return True
        else:
            return False

def update(self, spacecraft, parcel):
    """
    Updates spacecraft's packed parcels, mass, volume.
    Updates list of unpacked parcels. Returns the spacecraft.
    """
    # update spacecraft specifications
    spacecraft.packed_parcels.append(parcel)
    spacecraft.packed_mass += parcel.mass
    spacecraft.packed_vol += parcel.volume

    # update unpacked parcels
    self.unpacked_parcels.remove(parcel.ID)

    return spacecraft
 
def calculate_costs_spacecraft(self, spacecraft):
    """
    This function calculates and returns the costs of a spacecraft.
    """
    fuel_spacecraft = (spacecraft.mass + spacecraft.packed_mass) * \
        spacecraft.FtW / (1 - spacecraft.FtW)
    costs_spacecraft = spacecraft.base_cost + \
        math.ceil(fuel_spacecraft * 1000)

    return costs_spacecraft

def calculate_costs(self, solution):
    """
    This function calculates and returns the total costs.
    """
    total_costs = 0
    for spacecraft in solution.used_spacecrafts:
        spacecraft_costs = calculate_costs_spacecraft(spacecraft)
        total_costs += spacecraft_costs

    return total_costs

def printing(self, solution):
    """
    This functions prints the spacecrafts, packed parcels, packed mass and
    volume and total costs of a solution.
    """
    print(Fore.YELLOW + "Best solution of the runs:" + Style.RESET_ALL)
    print("=====================================")
    print(Back.GREEN + 'Total costs: $', solution.costs/billion, 'billion' + \
          Style.RESET_ALL)
    print("=====================================")
    print(Back.CYAN + "Fleet and payloads:" + Style.RESET_ALL)
    print("=====================================")
    for spacecraft in solution.used_spacecrafts:
        print('\n' + Fore.CYAN + spacecraft.name + ':' + Style.RESET_ALL)
        parcels = []
        for parcel in spacecraft.packed_parcels:
            parcels.append(parcel.ID)
        print(tabulate([["{0:.3f}".format(spacecraft.packed_mass), "{0:.3f}".format(spacecraft.packed_vol)]], headers=['Payload mass', 'Payload volume'], tablefmt='orgtbl'))
        print('Packed parcels:')
        count = 0
        for number in range(math.ceil(len(parcels)/4)):
            print(parcels[count:count+4])
            count += 4
        print("-------------------------------------")

def save_run_random(self, solution):
    """
    Saves and returns the solution from a run in a dataframe.
    """

    data = [solution.name, solution.costs]
    fleet = []
    costs_spacecraft = []
    packed_mass_vol = []
    packed_parcels = []

    # make lists
    for spacecraft in solution.used_spacecrafts:
        fleet.append(spacecraft.name)
        costs_spacecraft.append(spacecraft.costs)
        packed_mass_vol.append([spacecraft.packed_mass, \
                                spacecraft.packed_vol])

        parcels = []
        for parcel in spacecraft.packed_parcels:
            parcels.append(parcel.ID)

        packed_parcels.append(parcels)

    data.append(fleet)
    data.append(costs_spacecraft)
    data.append(packed_mass_vol)
    data.append(packed_parcels)

    row = pd.DataFrame([data])

    return row
