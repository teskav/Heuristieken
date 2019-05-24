# HEURISTIEKEN
# April - May 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script sets the class Parcel.
"""

class Parcel(object):
    """
    Representation of a parcel in spacefreight.
    """
    def __init__ (self, ID, mass, volume):
        self.ID = ID
        self.mass = mass
        self.volume = volume
