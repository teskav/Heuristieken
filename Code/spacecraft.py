# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script sets the class Parcel
"""

class Spacecraft(object):
    """
    Representation of a spacecraft in SpaceFreight
    """
    def __init__ (self, name, payload_mass, payload_vol, mass, base_cost, FtW, \
                    country):
        self.name = name
        self.payload_mass = payload_mass
        self.payload_vol = payload_vol
        self.mass = mass
        self.base_cost = base_cost
        self.FtW = FtW
        self.country = country
        self.packed_parcels = []
        self.packed_mass = 0
        self.packed_vol = 0
        self.costs = 0

    def remove_parcel(self, parcel):
        """
		Removes an item from the packed parcel list of an spacecraft
		"""
        # Remove item from the list
        self.packed_parcels.remove(parcel)

        # Update mass and volume of spacecraft
        self.packed_mass -= parcel.mass
        self.packed_vol -= parcel.volume

    def add_parcel(self, parcel):
        """
		Adds an item from the packed parcel list of an spacecraft
		"""
        # Add item to the list
        self.packed_parcels.append(parcel)

        # Update mass and volume of spacecraft
        self.packed_mass += parcel.mass
        self.packed_vol += parcel.volume
