# Heuristieken
# April - May 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
This script gives us outputs for our presentation
"""

import pandas as pd


data = pd.read_csv('../Outputs/Random/random_CL1_100000.csv', index_col=0)

optimal_fleet = data[data['costs_solution'] < 1600000000]

for row in optimal_fleet:
    
