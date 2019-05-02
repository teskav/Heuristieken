#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script sets the class Parcel
"""

class Spacecraft(object):
    """
    Representation of a spacecraft in SpaceFreight
    """
    def __init__ (self, name, payload_mass, payload_vol, mass, base_cost, FtW):
        self.name = name
        self.payload_mass = payload_mass
        self.payload_vol = payload_vol
        self.mass = mass
        self.base_cost = base_cost
        self.FtW = FtW
        self.packed_parcels = []
        self.packed_mass = 0
        self.packed_vol = 0
        self.costs = 0

    def remove_parcel(self, parcel):
        """
		Removes an item from the packed parcel list of an spacecraft
		"""
        # volgens mij hoeven we dus hier niet een spacecraft als input te doen,
        # omdat dit in de spacecraft class is en dan moet je in de andere class
        # (waar de swap komt) gewoon doen: spacecraftobject.remove_item(item)

        # ik ga er nu even van uit dat item een object is, maar moeten even
        # kijken hoe we dat gaan doen als dat niet lukt

        # we moeten denk ik wel al de massa en volume aanpassen in de remove en
        # add, want dan kan je in de swap checken of er uberhaupt geswapt kan worden

        # Remove item from the list
        self.packed_parcels.remove(parcel)

        # Update mass and volume of spacecraft
        self.packed_mass -= parcel.mass
        self.packed_vol -= parcel.volume

    def add_parcel(self, spacecraft, parcel):
        """
		Adds an item from the packed parcel list of an spacecraft
		"""
        # Add item to the list
        self.packed_parcels.add(parcel)

        # Update mass and volume of spacecraft
        self.packed_mass += parcel.mass
        self.packed_vol += parcel.volume
