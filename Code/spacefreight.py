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

INPUT = "CargoLists/CargoList1.csv"

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
		self.spacecrafts.append(Spacecraft('Cygnus', 2000, 18.9, 7400, 390000000, 0.73))
		self.spacecrafts.append(Spacecraft('Progress', 2400, 7.6, 7020, 175000000, 0.74))
		self.spacecrafts.append(Spacecraft('Kounotori', 5200, 14, 10500, 420000000, 0.71))
		self.spacecrafts.append(Spacecraft('Dragon', 6000, 10, 12200, 347000000, 0.72))
		# self.spacecrafts.append(Spacecraft('TianZhou', 6500, 15, 13500, 412000000, 0.75))
		# self.spacecrafts.append(Spacecraft('Verne ATV', 7500, 48, 20500, 1080000000, 0.72))

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
		if (spacecraft.packed_mass + parcel.mass) < spacecraft.payload_mass and (spacecraft.packed_vol + parcel.volume) < spacecraft.payload_vol:
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
		fuel_spacecraft = (spacecraft.mass + spacecraft.packed_mass) * spacecraft.FtW * (1 - spacecraft.FtW)
		costs_spacecraft = spacecraft.base_cost + math.ceil(fuel_spacecraft * 1000)
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
		volume, the unpacked parcels, number of packed parcels and the total costs.
		"""
		for spacecraft in solution.used_spacecrafts:
			print(spacecraft.name + ':')
			parcels = []
			for parcel in spacecraft.packed_parcels:
			    parcels.append(parcel.ID)
			print(parcels)
			print("Mass:", "{0:.3f}".format(spacecraft.packed_mass))
			print("Vol:", "{0:.3f}".format(spacecraft.packed_vol))

		print('unpacked:')
		print(solution.unpacked_parcels)
		print('number of packed parcels: ', len(self.all_parcels) - solution.not_bring)
		print('Costs:', solution.costs/billion, 'billion')

	def swap_parcel(self, spacecraft_1, spacecraft_2, parcel_1, parcel_2):
		"""
		Swaps an item of an spacecraft with an item of another spacecraft, if possible.
		"""
		# Remove item from spacecrafts
		spacecraft_1.remove_parcel(parcel_1)
		spacecraft_2.remove_parcel(parcel_2)

		# Swap items if possible (check payload volume and mass)
		if self.check(spacecraft_1, parcel_2) and self.check(spacecraft_2, parcel_1):
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
		column_names = ['algorithm_name', 'iteration', 'costs_solution', 'number_unpacked_parcels', 'unpacked_parcels']
		# columns = ['algorithm_name', 'iteration', 'costs_solution', 'number_unpacked_parcels', 'unpacked_parcels']
		data = [solution.name, count, solution.costs, solution.not_bring, solution.unpacked_parcels]
		# append to dataframe
		for spacecraft in solution.used_spacecrafts:
			# append data
			data.append(spacecraft.name)
			data.append(len(spacecraft.packed_parcels))
			parcels = []
			for parcel in spacecraft.packed_parcels:
				parcels.append(parcel.ID)
			data.append(parcels)
			data.append(spacecraft.costs)
			data.append("{0:.3f}".format(spacecraft.packed_mass))
			data.append("{0:.3f}".format(spacecraft.packed_vol))
			# append column names
			column_names.extend(['name', 'number_packed_parcels', 'packed_parcels', 'spacecraft_costs', 'spacecraft_packed_mass', 'spacecraft_packed_vol'])

		row = pd.DataFrame([data])

		return row

	def save_iteration_SA(self, solution, count, temperature, acceptatiekans):
		"""
		Save the solution from an iteration in a dataframe
		"""
		column_names = ['algorithm_name', 'iteration', 'costs_solution', 'number_unpacked_parcels', 'unpacked_parcels', 'temperature', 'acceptatiekans']
		data = [solution.name, count, solution.costs, solution.not_bring, solution.unpacked_parcels, temperature, acceptatiekans]
		# append to dataframe
		for spacecraft in solution.used_spacecrafts:
			# append data
			data.append(spacecraft.name)
			data.append(len(spacecraft.packed_parcels))
			parcels = []
			for parcel in spacecraft.packed_parcels:
				parcels.append(parcel.ID)
			data.append(parcels)
			data.append(spacecraft.costs)
			data.append("{0:.3f}".format(spacecraft.packed_mass))
			# print("{0:.3f}".format(spacecraft.packed_mass))
			data.append("{0:.3f}".format(spacecraft.packed_vol))
			# append column names
			column_names.extend(['name', 'number_packed_parcels', 'packed_parcels', 'spacecraft_costs', 'spacecraft_packed_mass', 'spacecraft_packed_vol'])

		row = pd.DataFrame([data])

		return row

	def max_costs(self):
		"""
		This function calculates the maximal costs.
		"""
		costs_max = 0
		for spacecraft in self.spacecrafts:
			fuel_spacecraft = (spacecraft.mass + spacecraft.payload_mass) * spacecraft.FtW * (1 - spacecraft.FtW)
			costs_spacecraft = spacecraft.base_cost + math.ceil(fuel_spacecraft * 1000)
			costs_max += costs_spacecraft
		return costs_max

	def min_costs(self):
		"""
		This function calculates the minimal costs.
		"""
		costs_min = 0
		for spacecraft in self.spacecrafts:
			fuel_spacecraft = (spacecraft.mass + 0) * spacecraft.FtW * (1 - spacecraft.FtW)
			costs_spacecraft = spacecraft.base_cost + math.ceil(fuel_spacecraft * 1000)
			costs_min += costs_spacecraft
		return costs_min
