##!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
This script sets the class solution
"""

class Solution(object):
    """
    Representation of the current solution
    """
    def __init__ (self, name, not_bring, unpacked_parcels, costs, used_spacecrafts):

        # algorithm name
        self.name = name
        # number of unpacked parcels
        self.not_bring = not_bring
        # list of unpacked_parcels
        self.unpacked_parcels = unpacked_parcels
        # costs
        self.costs = costs
        # list of used spacecrafts objects
        self.used_spacecrafts = used_spacecrafts

    #
    # def __getitem__(self, key):
    # # loop over spacecrafts tot je de goeie vindt die key is
    # # dan deze list returnen
    #
    #     return self.Solution[key]
