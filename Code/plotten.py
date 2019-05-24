# HEURISTIEKEN
# April - Mei 2019
# Space Freight
# Sofie Löhr, Teska Vaessen & Wies de Wit
"""
Script to sort and calculate differences
"""
import pandas as pd
import sys
from plot import *

# import csv data from algorithm
output_location = '/Simulated_Annealing/iterations_SA_CL1_exp_30x2000.csv'
data = pd.read_csv('../Outputs' + output_location, index_col=0)

# data used for plot
used_data = data.loc[data['costs_solution']<1850000000]
# used_data = data.iloc[58000:60000]
print(used_data['costs_solution'])
# plot
# plot_costs(used_data)

plt.plot(list(range(len(used_data['costs_solution']))), \
used_data['costs_solution'])
plt.xlabel('Iterations')
plt.ylabel('Costs')
plt.title('Distribution of the solution')
plt.show()
