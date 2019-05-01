#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script sets the class solution
"""
from spacefreight import SpaceFreight

spacefreight = SpaceFreight()

class Solution(object):
    """
    Representation of the current solution
    """
    def __init__ (self, not_bring, unpacked_parcels, costs, cygnus, progress, kounotori, dragon):

        # number of unpacked parcels
        self.not_bring = not_bring
        # list of unpacked_parcels
        self.unpacked_parcels = unpacked_parcels
        # costs
        self.costs = costs
        # list of parcels in every spacecraft
        self.cygnus = cygnus
        self.progress = progress
        self.kounotori = kounotori
        self.dragon = dragon

    #
    # def __getitem__(self, key):
    # # loop over spacecrafts tot je de goeie vindt die key is
    # # dan deze list returnen
    #
    #     return self.Solution[key]
