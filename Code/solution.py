# HEURISTIEKEN
# April - May 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script sets the class solution
"""

class Solution(object):
    """
    Representation of the current solution
    """
    def __init__ (self, name, costs, used_spacecrafts):

        # algorithm name
        self.name = name
        # costs
        self.costs = costs
        # list of used spacecrafts objects
        self.used_spacecrafts = used_spacecrafts
