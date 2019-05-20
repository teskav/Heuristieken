# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script sets the spacefreight class
"""

# imports
import pandas as pd
import csv
import math
import matplotlib.pyplot as plt
import copy
from parcel import Parcel
from spacecraft import Spacecraft
from solution import Solution

INPUT_1 = "CargoLists/CargoList1.csv"
INPUT_2 = "CargoLists/CargoList2.csv"
INPUT_3 = "CargoLists/CargoList3.csv"

print("Cargolist options: \n 1 2 3 \n")
list = input("Please give cargolist number: ")

if list == '1':
    INPUT = INPUT_1

if list == '2':
    INPUT = INPUT_2

if list == '3':
    INPUT = INPUT_3

billion = 1000000000

class SpaceFreight():
	def __init__ (self):

		global current_solution

		# load the list with all parcel objects
		self.all_parcels = self.load_parcels(INPUT)

		# make list with all unpacked parcels (only ID)
		self.unpacked_parcels = []
		for p in self.all_parcels:
			self.unpacked_parcels.append(p.ID)

		# load spacecraft objects
		self.spacecrafts = []
		self.spacecrafts.append(Spacecraft('Cygnus', 2000, 18.9, 7400, \
                                390000000, 0.73, 'USA'))
		self.spacecrafts.append(Spacecraft('Progress', 2400, 7.6, 7020, \
                                175000000, 0.74, 'Russia'))
		self.spacecrafts.append(Spacecraft('Kounotori', 5200, 14, 10500, \
                                420000000, 0.71, 'Japan'))
		self.spacecrafts.append(Spacecraft('Dragon', 6000, 10, 12200, \
                                347000000, 0.72, 'USA'))

		if INPUT == INPUT_3:
			self.spacecrafts.append(Spacecraft('TianZhou', 6500, 15, 13500, \
                                    412000000, 0.75, 'China'))
			self.spacecrafts.append(Spacecraft('Verne ATV', 7500, 48, 20500, \
                                    1080000000, 0.72, 'Europe'))

	def load_parcels(self, file):
		"""
		Load parcels from csv file.
		Returns dictionary of 'name': Parcel objects.
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
		Check if the payload mass and volume does not get exceeded
		Boolean
		"""
		if ((spacecraft.packed_mass+parcel.mass) < spacecraft.payload_mass and
                (spacecraft.packed_vol+parcel.volume) < spacecraft.payload_vol):
			return True
		else:
			return False

	def update(self, spacecraft, parcel):
		"""
		Update spacecraft packed parcels, mass, volume
		Update list of unpacked parcels
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
		This function calculates the costs of a spacecraft.
		"""
		fuel_spacecraft = (spacecraft.mass + spacecraft.packed_mass) * \
            spacecraft.FtW * (1 - spacecraft.FtW)
		costs_spacecraft = spacecraft.base_cost + \
            math.ceil(fuel_spacecraft * 1000)
		# niet deze costs = spacecraft.base_cost + round(fuel * 1000)
		return costs_spacecraft

	def calculate_costs(self, solution):
		"""
		This function calculates the total costs.
		"""
		total_costs = 0
		for spacecraft in solution.used_spacecrafts:
			spacecraft_costs = self.calculate_costs_spacecraft(spacecraft)
			total_costs += spacecraft_costs
		# niet deze costs = spacecraft.base_cost + round(fuel * 1000)
		return total_costs

	def printing(self, solution):
		"""
		This functions prints the spacecrafts, packed parcels, packed mass and
		volume, unpacked parcels, number of packed parcels and total costs.
		"""
		for spacecraft in solution.used_spacecrafts:
			print(spacecraft.name + ':')
			parcels = []
			for parcel in spacecraft.packed_parcels:
			    parcels.append(parcel.ID)
			print(parcels)
			print("Mass:", "{0:.3f}".format(spacecraft.packed_mass))
			print("Vol:", "{0:.3f}".format(spacecraft.packed_vol))

		print('Unpacked:')
		print(solution.unpacked_parcels)
		print('Number of packed parcels: ', len(self.all_parcels) - \
                solution.not_bring)
		print('Costs:', solution.costs/billion, 'billion')

	def swap_parcel(self, spacecraft_1, spacecraft_2, parcel_1, parcel_2):
		"""
		Swaps an item of an spacecraft with an item of another spacecraft,
        if possible.
		"""
		# Remove item from spacecrafts
		spacecraft_1.remove_parcel(parcel_1)
		spacecraft_2.remove_parcel(parcel_2)

		# Swap items if possible (check payload volume and mass)
		if (self.check(spacecraft_1, parcel_2) and
                self.check(spacecraft_2, parcel_1)):
			spacecraft_1.add_parcel(parcel_2)
			spacecraft_2.add_parcel(parcel_1)
			return True
		else:
			spacecraft_1.add_parcel(parcel_1)
			spacecraft_2.add_parcel(parcel_2)
			return False

	def swap_spacecraft(self, spacecraft_1, spacecraft_2):
		"""
		Swaps the whole payload of one spacecraft to another spacecraft
		"""
		spacecraft_2.packed_mass = copy.copy(spacecraft_1.packed_mass)
		spacecraft_2.packed_vol = copy.copy(spacecraft_1.packed_vol)
		spacecraft_2.packed_parcels = copy.copy(spacecraft_1.packed_parcels)
		spacecraft_2.costs = self.calculate_costs_spacecraft(spacecraft_2)

		return spacecraft_2

	def save_iteration(self, solution, count):
		"""
		Save the solution from an iteration in a dataframe
		"""
		data = [solution.name, count, solution.costs]
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

	def save_iteration_SA(self, solution, count, temperature, acceptatiekans):
		"""
		Save the solution from an iteration in a dataframe
		"""
		data=[solution.name, count, solution.costs, temperature, acceptatiekans]

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

	def save_run_random(self, solution):
		"""
		Save the solution from a run in a dataframe
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

	def save_run_hill_climber(self, start_solution, end_solution, max_iterations):
		"""
		Save the solution from a run in a dataframe
		"""
		data = [start_solution.name, max_iterations, start_solution.costs, \
                end_solution.costs]
		start_fleet = []
		start_costs_spacecraft = []
		start_packed_mass_vol = []
		start_packed_parcels = []
		end_fleet = []
		end_costs_spacecraft = []
		end_packed_mass_vol = []
		end_packed_parcels = []

		# make lists start solution
		for spacecraft in start_solution.used_spacecrafts:
			start_fleet.append(spacecraft.name)
			start_costs_spacecraft.append(spacecraft.costs)
			start_packed_mass_vol.append([spacecraft.packed_mass, \
                                        spacecraft.packed_vol])

			parcels = []
			for parcel in spacecraft.packed_parcels:
				parcels.append(parcel.ID)

			start_packed_parcels.append(parcels)

		data.append(start_fleet)
		data.append(start_costs_spacecraft)
		data.append(start_packed_mass_vol)
		data.append(start_packed_parcels)

		# make lists end solution
		for spacecraft in end_solution.used_spacecrafts:
			end_fleet.append(spacecraft.name)
			end_costs_spacecraft.append(spacecraft.costs)
			end_packed_mass_vol.append([spacecraft.packed_mass, \
                                        spacecraft.packed_vol])

			parcels = []
			for parcel in spacecraft.packed_parcels:
				parcels.append(parcel.ID)

			end_packed_parcels.append(parcels)

		data.append(end_fleet)
		data.append(end_costs_spacecraft)
		data.append(end_packed_mass_vol)
		data.append(end_packed_parcels)

		row = pd.DataFrame([data])

		return row

	def max_costs(self):
		"""
		This function calculates the maximal costs.
		"""
		costs_max = 0
		for spacecraft in self.spacecrafts:
			fuel_spacecraft = (spacecraft.mass + spacecraft.payload_mass) * \
                spacecraft.FtW * (1 - spacecraft.FtW)
			costs_spacecraft = spacecraft.base_cost + \
                math.ceil(fuel_spacecraft * 1000)
			costs_max += costs_spacecraft
		return costs_max

	def min_costs(self):
		"""
		This function calculates the minimal costs.
		"""
		costs_min = 0
		for spacecraft in self.spacecrafts:
			fuel_spacecraft = (spacecraft.mass + 0) * \
                spacecraft.FtW * (1 - spacecraft.FtW)
			costs_spacecraft = spacecraft.base_cost + \
                math.ceil(fuel_spacecraft * 1000)
			costs_min += costs_spacecraft
		return costs_min
