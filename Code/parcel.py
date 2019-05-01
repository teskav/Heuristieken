#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script sets the class Parcel
"""

class Parcel(object):
    """
    Representation of a parcel in spacefreight
    """
    def __init__ (self, ID, mass, volume):
    	self.ID = ID
    	self.mass = mass
    	self.volume = volume
