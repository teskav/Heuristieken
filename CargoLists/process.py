#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script sets the spacefreight class
"""

# Global constants
INPUT = "CargoList1.csv"

class SpaceFreight():
	def __init__ (self):
		# load the parcels
		self.all_parcels = self.load_parcels(INPUT)

		self.unpacked_parcels = []
		for p in self.all_parcels:
			self.unpacked_parcels.append(p.ID)

		# load spacecraft objects
		self.spacecrafts = {}
		self.spacecrafts['cygnus'] = Spacecraft(2000, 18.9, 7400, 390, 0.73)
		self.spacecrafts['progress'] = Spacecraft(2400, 7.6, 7020, 175, 0.74)
		self.spacecrafts['kounotori'] = Spacecraft(5200, 14, 10500, 420, 0.71)
		self.spacecrafts['dragon'] = Spacecraft(6000, 10, 12200, 347, 0.72)


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


<<<<<<< HEAD
	def allocate_pseudo_random(self):
		"""
		Random allocate the parcels in spacecrafts
		"""

		# list with random numbers, order in which the parcels are being added
		my_randoms = random.sample(range(1, 101), 100)
		self.unpacked_parcels = list(self.all_parcels.keys())

		for spacecraft in random_spacecrafts:
			spacecraft = self.spacecrafts[spacecraft]
			# set variables at 0
			spacecraft.packed_parcels = []
			spacecraft.packed_mass = 0
			spacecraft.packed_vol = 0
			for item in my_randoms:
				parcel_code = 'CL1#' + str(item)
				parcel = self.all_parcels[parcel_code]
				if self.check_mass(spacecraft, parcel) and self.check_vol(spacecraft, parcel) and parcel.ID in self.unpacked_parcels:
					self.update(spacecraft, parcel)
			print(spacecraft.packed_parcels)
		print('unpacked:')
		print(self.unpacked_parcels)
		# print(len(self.unpacked_parcels))
		return len(self.unpacked_parcels)

=======
>>>>>>> cf8c375e917972508798e870dc90c51f313198a5
	def allocate_random(self):
		"""
		Random allocate the parcels in spacecrafts
		"""

		# list with random numbers, order in which the parcels are being added
		my_randoms = random.sample(range(1, 101), 100)
		self.unpacked_parcels = list(self.all_parcels.keys())

<<<<<<< HEAD
		random_spacecrafts = random.sample(range(1,5), 4)

		for spacecraft in random_spacecrafts:
			spacecraft = self.spacecrafts[spacecraft]
			# set variables at 0
=======
		for spacecraft in self.spacecrafts:
			# print(spacecraft)
			spacecraft = self.spacecrafts[spacecraft]
>>>>>>> cf8c375e917972508798e870dc90c51f313198a5
			spacecraft.packed_parcels = []
			spacecraft.packed_mass = 0
			spacecraft.packed_vol = 0
			for item in my_randoms:
				parcel_code = 'CL1#' + str(item)
				parcel = self.all_parcels[parcel_code]
				if self.check_mass(spacecraft, parcel) and self.check_vol(spacecraft, parcel) and parcel.ID in self.unpacked_parcels:
					self.update(spacecraft, parcel)
<<<<<<< HEAD
			print(spacecraft.packed_parcels)
		print('unpacked:')
		print(self.unpacked_parcels)
=======
		# 	print(spacecraft.packed_parcels)
		# print('unpacked:')
>>>>>>> cf8c375e917972508798e870dc90c51f313198a5
		# print(len(self.unpacked_parcels))
		return len(self.unpacked_parcels)

	def first_fit(self):
		"""
		Allocate the parcels in spacecrafts
		"""
		for spacecraft in self.spacecrafts:
			spacecraft = self.spacecrafts[spacecraft]
			for parcel in self.all_parcels:
				parcel = self.all_parcels[parcel]
				if self.check_mass(spacecraft, parcel) and self.check_vol(spacecraft, parcel) and parcel.ID in self.unpacked_parcels:
					self.update(spacecraft, parcel)
		# 	print(spacecraft.packed_parcels)
		# print(self.unpacked_parcels)

	def check_mass(self, spacecraft, parcel):
		"""
		Check if the payload mass does not get exceeded
		Boolean
		"""
		# fuel = (spacecraft.mass + spacecraft.packed_mass + parcel.mass) * spacecraft.FtW / (1 - spacecraft.FtW)
		# mass = fuel + spacecraft.packed_mass + parcel.mass
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
<<<<<<< HEAD
		self.unpacked_parcels.remove(parcel.ID)
=======
		# print(self.unpacked_parcels)
		self.unpacked_parcels.remove(parcel.ID)
		# print(self.unpacked_parcels)

class Parcel(object):
    def __init__ (self, ID, mass, volume):
    	self.ID = ID
    	self.mass = mass
    	self.volume = volume

class Spacecraft(object):
    def __init__ (self, payload_mass, payload_vol, mass, base_cost, FtW):
    	self.payload_mass = payload_mass
    	self.payload_vol = payload_vol
    	self.mass = mass
    	self.base_cost = base_cost
    	self.FtW = FtW
    	self.packed_parcels = []
    	self.packed_mass = 0
    	self.packed_vol = 0


if __name__ == "__main__":
	spacefreight = SpaceFreight()
	# number_unpacked_parcels = spacefreight.allocate()
	number_unpacked_parcels = spacefreight.allocate_random()

	count = 0

	# while loop weghalen als je normale first fit runt
	while number_unpacked_parcels > 12:
		number_unpacked_parcels = spacefreight.allocate_random()
		count += 1

	print('Number of iterations:', count)
	print('Number of unpacked parcels:', len(spacefreight.unpacked_parcels))
	print(spacefreight.unpacked_parcels)
	for spacecraft in spacefreight.spacecrafts:
		print(spacecraft)
		spacecraft = spacefreight.spacecrafts[spacecraft]
		print('Current mass load:', spacecraft.packed_mass)
		print('Current volume load:', spacecraft.packed_vol)
		# print(spacecraft.mass)
		print(spacecraft.packed_parcels)

	# spacefreight.sort(spacefreight.all_parcels)
>>>>>>> cf8c375e917972508798e870dc90c51f313198a5
