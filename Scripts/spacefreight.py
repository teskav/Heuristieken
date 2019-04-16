#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script sets the spacefreight class
"""
# imports
import pandas as pd
import csv
from parcel import Parcel
from spacecraft import Spacecraft

# Global constants
INPUT = "Scripts/CargoList1.csv"

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
		self.spacecrafts['cygnus'] = Spacecraft(2000, 18.9, 7400, 390, 0.73)
		self.spacecrafts['progress'] = Spacecraft(2400, 7.6, 7020, 175, 0.74)
		self.spacecrafts['kounotori'] = Spacecraft(5200, 14, 10500, 420, 0.71)
		self.spacecrafts['dragon'] = Spacecraft(6000, 10, 12200, 347, 0.72)

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
		spacecraft.packed_parcels.append(parcel.ID)
		spacecraft.packed_mass += parcel.mass
		spacecraft.packed_vol += parcel.volume

		# update unpacked parcels
		self.unpacked_parcels.remove(parcel.ID)

	def printing(self):
		"""
		Prints the results
		"""
		for spacecraft in self.spacecrafts:
			print(spacecraft + ':')
			spacecraft = self.spacecrafts[spacecraft]
			print(spacecraft.packed_parcels)
		print('unpacked:')
		print(self.unpacked_parcels)
		print('number of packed parcels: ', 100-len(self.unpacked_parcels))
		# also print costs for this sollution
