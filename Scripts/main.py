#!/usr/bin/env python
# Name: Sofie, Teska Wies
"""
Main script
"""
from parcel import Parcel
from spacecraft import Spacecraft
from spacefreight import SpaceFreight

spacefreight = SpaceFreight()
number_unpacked_parcels = spacefreight.allocate_pseudo_random()
count = 0

while number_unpacked_parcels > 20:
	number_unpacked_parcels = spacefreight.allocate_random()
	count += 1

print(count)

# spacefreight.sort(spacefreight.all_parcels)
