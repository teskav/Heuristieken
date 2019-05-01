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

# Global constants
INPUT = "CargoLists/CargoList1.csv"

class SpaceFreight():
	def __init__ (self):

		# load the list with all parcel objects
		self.all_parcels = self.load_parcels(INPUT)

		# make list with all unpacked parcels (only ID)
		self.unpacked_parcels = []
		for p in self.all_parcels:
			self.unpacked_parcels.append(p.ID)

		# load spacecraft objects
		self.spacecrafts = {}
		self.spacecrafts['cygnus'] = Spacecraft('cygnus', 2000, 18.9, 7400, 390000000, 0.73)
		self.spacecrafts['progress'] = Spacecraft('progress', 2400, 7.6, 7020, 175000000, 0.74)
		self.spacecrafts['kounotori'] = Spacecraft('kounotori', 5200, 14, 10500, 420000000, 0.71)
		self.spacecrafts['dragon'] = Spacecraft('dragon', 6000, 10, 12200, 347000000, 0.72)

		self.spacecrafts_names = list(self.spacecrafts.keys())

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

	def check_mass(self, spacecraft, parcel):
		"""
		Check if the payload mass does not get exceeded
		Boolean
		"""
		if (spacecraft.packed_mass + parcel.mass) < spacecraft.payload_mass:
			return True
		else:
			return False

	def check_vol(self, spacecraft, parcel):
		"""
		Check if the payload volume does not get exceeded
		Boolean
		"""
		if (spacecraft.packed_vol + parcel.volume) < spacecraft.payload_vol:
			return True
		else:
			return False

	def update(self, spacecraft, parcel):
		"""
		Update spacecraft packed parcels, mass, volume
		Update list of unpacked parcels
		"""
		# update spacecraft specifications
		self.spacecrafts[spacecraft.name]
		self.spacecrafts[spacecraft.name].packed_parcels.append(parcel.ID)
		self.spacecrafts[spacecraft.name].packed_mass += parcel.mass
		self.spacecrafts[spacecraft.name].packed_vol += parcel.volume

		# update unpacked parcels
		self.unpacked_parcels.remove(parcel.ID)

	def calculate_costs(self, spacecraft):
		"""
		This function calculates the costs of a spacecraft.
		"""
		fuel = (spacecraft.mass + spacecraft.packed_mass) * spacecraft.FtW * (1 - spacecraft.FtW)
		costs = spacecraft.base_cost + math.ceil(fuel * 1000)
		# niet deze costs = spacecraft.base_cost + round(fuel * 1000)
		return costs

	def printing(self):
		"""
		Prints the results
		"""
		total_costs = 0
		for spacecraft in self.spacecrafts:
			print(spacecraft + ':')
			spacecraft = self.spacecrafts[spacecraft]
			print(spacecraft.packed_parcels)
			cost_spacecraft = self.calculate_costs(spacecraft)
			print("Mass:", spacecraft.packed_mass)
			print("Vol:", spacecraft.packed_vol)
			total_costs += cost_spacecraft

		print('unpacked:')
		print(self.unpacked_parcels)
		print('number of packed parcels: ', 100-len(self.unpacked_parcels))
		print('Costs:', total_costs/1000000000, 'billion')
