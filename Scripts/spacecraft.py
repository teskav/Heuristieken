#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script sets the class Parcel
"""

class Spacecraft(object):
    """
    Representation of a spacecraft in SpaceFreight
    """
    def __init__ (self, payload_mass, payload_vol, mass, base_cost, FtW):
    	self.payload_mass = payload_mass
    	self.payload_vol = payload_vol
    	self.mass = mass
    	self.base_cost = base_cost
    	self.FtW = FtW
    	self.packed_parcels = []
    	self.packed_mass = 0
    	self.packed_vol = 0
