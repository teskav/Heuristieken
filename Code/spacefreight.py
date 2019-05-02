#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script sets the spacefreight class
"""
# imports
import pandas as pd
import csv
import math
from parcel import Parcel
from spacecraft import Spacecraft
from solution import Solution
# Global constants
INPUT = "CargoLists/CargoList1.csv"

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
		self.spacecrafts.append(Spacecraft('cygnus', 2000, 18.9, 7400, 390000000, 0.73))
		self.spacecrafts.append(Spacecraft('progress', 2400, 7.6, 7020, 175000000, 0.74))
		self.spacecrafts.append(Spacecraft('kounotori', 5200, 14, 10500, 420000000, 0.71))
		self.spacecrafts.append(Spacecraft('dragon', 6000, 10, 12200, 347000000, 0.72))

		# self.spacecrafts_names = list(self.spacecrafts.keys())

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

	def calculate_costs_spacecraft(self, spacecraft):
		"""
		This function calculates the costs of a spacecraft.
		"""
		fuel_spacecraft = (spacecraft.mass + spacecraft.packed_mass) * spacecraft.FtW * (1 - spacecraft.FtW)
		costs_spacecraft = spacecraft.base_cost + math.ceil(fuel_spacecraft * 1000)
		# niet deze costs = spacecraft.base_cost + round(fuel * 1000)
		return costs_spacecraft

	def calculate_costs(self):
		"""
		This function calculates the total costs.
		"""
		total_costs = 0
		for spacecraft in self.spacecrafts:
			fuel_spacecraft = (spacecraft.mass + spacecraft.packed_mass) * spacecraft.FtW * (1 - spacecraft.FtW)
			costs_spacecraft = spacecraft.base_cost + math.ceil(fuel_spacecraft * 1000)
			total_costs += costs_spacecraft
		# niet deze costs = spacecraft.base_cost + round(fuel * 1000)
		return total_costs

	def printing(self, solution):
		"""
		Prints the results
		"""
		for spacecraft in self.spacecrafts:
			print(spacecraft.name + ':')
			parcels = []
			for parcel in spacecraft.packed_parcels:
				parcels.append(parcel.ID)
			print(parcels)
			print("Mass:", spacecraft.packed_mass)
			print("Vol:", spacecraft.packed_vol)
#
		print('unpacked:')
		print(self.unpacked_parcels)
		print('number of packed parcels: ', 100-len(self.unpacked_parcels))
		print('Costs:', solution.costs/1000000000, 'billion')


	# def current_solution(spacecrafts):

	def swap_parcel(self, spacecraft1, spacecraft2, parcel1, parcel2):
		"""
		Swaps an item of an spacecraft with an item of another spacecraft if possible.
		"""
		# ik ga er hier weer van uit dat de items objecten zijn

		# Remove item from spacecrafts
		spacecraft1.remove_parcel(parcel1)
		spacecraft2.remove_parcel(parcel2)

		# Swap items if possible (check payload volume and mass)
		if self.check(spacecraft1, parcel2) and self.check(spacecraft2, parcel1):
			spacecraft1.add_parcel(parcel2)
			spacecraft2.add_parcel(parcel1)
		else:
			spacecraft1.add_parcel(parcel1)
			spacecraft2.add_parcel(parcel2)
