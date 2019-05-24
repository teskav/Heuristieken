# Space Freight
## Problem
The case Spacefreight is a constraint optimization problem (COP). The constraints that needs to be met are to ship all parcels from the cargolist(s) and to not exceed the maximum payload mass and the maximum payload volume of the spacecrafts. Each spacecraft has their own specifications. Multiple spacecrafts can be deployed to ship all parcels to the International Space Station (ISS).

The transportation costs need to be minimized, so the parcels from the cargolist(s) need to be distributed optimally to minimize costs.

The costs are divided in two categories, base costs and fuel costs. Every spacecraft has different base costs, the initial costs for the use of the spacecraft. Fuel costs depend on the mass of the spacecraft, the used payload mass and the Fuel-to-Weight ratio (FtW) of the spacecraft.

The mass (in kg) of fuel needed to deploy the spacecraft is calculated as follows:
F = (Mass + Payload-mass) x FtW / (1 - FtW)

The total amount of fuel is purchased per gram and costs $1 per gram, therefore the total costs of deploying the spacecraft are calculated as follows:
Base cost + roundup(F x 1000)

### State Space & Bounds Costs
#### General
For the statespace we looked at the properties of each cargolist and of each spacecraft. We calculated the minimum amount of spacecrafts needed to bring all parcels and the (reasonable) maximum amount of spacecrafts needed. With this information we calculate the lower bound and upper bound of the state space as follows:

+ Lower bound = (Minimum amount of spacecrafts)^(number of parcels in cargolist)
+ Upper bound = (Maximum amount of spacecrafts)^(number of parcels in cargolist)

#### Cargolist 1
So the state space for cargolist 1 is:

+ Lower bound = 4^100 = 1,61 * 10^60
+ Upper bound = 8^100 = 2,04 * 10^90

Using this the lower and upper bound for the costs of cargolist 1 are:

+ Lower bound = $ 0,807 billion
+ Upper bound = $ 3,668 billion

#### Cargolist 2
So the state space for cargolist 2 is:

+ Lower bound = 5^100 = 7,89 * 10^69
+ Upper bound = 8^100 = 2,04 * 10^90

Using this the lower and upper bound for the costs of cargolist 2 are:

+ Lower bound = $ 1,009 billion
+ Upper bound = $ 3,668 billion

##### Cargolist 3
So the state space for cargolist 3 is:

+ Lower bound = 24^1000 = 1,63 * 10^1380
+ Upper bound = 84^1000 = 1,90 * 10^1924

Using this the lower and upper bound for the costs of cargolist 3 are:

+ Lower bound = $ 16,952 billion
+ Upper bound = $ 27,648 billion

## Getting Started
### Prerequisites
This code is written in Python 3. In requirements.txt you will find all the packages you need to run the code successfully. These are easy to install by pip using the following instruction:
```
pip install -r requirements.txt
```

### Structure
All Python scripts are in the folder Code. The Cargolists folder contains all three cargolists with their input values and in the Outputs folder are some of the results that we found.

### Testing
To run the code use the following instruction:
```
python main.py
```
If you want to save your run(s), you have to use an input argument and run the following instruction:
```
python main.py save
```
Then the run(s) (and iterations in case of hill climber or simulated annealing) will be saved in the Outputs file as runs_saved.csv (and iterations_saved.csv).

The rest of the specifications will be set by the following questions:
```
Please give cargolist number:
```
Type 1, 2 or 3 to load the cargolist you want. When you choose cargolist 1 or 2, you will take the 4 spacecrafts. If you choose cargolist 3, you will take the 6 spacecrafts.
```
Please give algorithm:
```
Type here the algorithm you want to run. Options: first fit, random, pseudo greedy random, hill climber, simulated annealing, political constraints. Political constraints is only possible if you chose cargolist 3.

If you choose first fit, you get the following question for the heuristic:
```
Please give heuristic:
```
Type here the heuristic you want to choose. Options: normal, sorted mass, sorted vol.

If you choose hill climber, you get the following question for the heuristic:
```
Please give neighbour solution:
```
Type here the neighbour solution you want to choose. Options: parcels, spacecrafts, combined.

If you choose simulated annealing, you will get the same question about the neighbour solution as with the hill climber. Only spacecrafts is not possible, since for the simulated annealing with spacecrafts it makes no sense to accept an solution with worse costs, since it will never take you to an other optimum. After this you will get the following question for the cooling scheme:
```
Please give cooling scheme:
```
Type here the cooling scheme you want to use. Options: lineair, exponential, sigmoidal.


### Data
Structure:
+ Parcels
+ Spacecrafts
+ Spacefreight

## Algorithms
### First fit
The first fit algorithm is a greedy algorithm. With this algorithm we loop over the spacecrafts in the order they are loaded and then loop over the parcels in the order they are loaded. So we take the first spacecraft and place the first parcel in this spacecrafts. Then for every parcel we check if it still fits in the first spacecraft and if it fits, it goes in the first spacecraft. Then if we checked every parcel, we do the same for the second spacecraft. Here we also check if the parcel is still unpacked. Then we do this for the third spacecraft and so on.

This algorithm only has 1 solution and this solution is for our case not optimal.

#### Sorted
There are two additional options (besides the 'normal') for the first fit algorithm. For these options, sorted mass and sorted volume, we first sort the cargolists by mass (descending) or volume (ascending) and loop over the cargolists in this order.

### Random
Our random algorithm is not greedy. This algorithm basically does the same as our first fit algorithm, though the random algorithm does everything in random order. So it first picks a random spacecraft, then the cargolist will be in a random order and it fills the spacecrafts. Then it picks another random spacecraft (which can be the same as the first one) and fills this one. This goes on untill all parcels are packed.

With this algorithm you can make every solution in the state space. Which is not optimal, since it will take forever to find the most optimal solution.

### Pseudo greedy and random
This algorithm first uses a pseudo greedy heuristic (multiple constraints) to fill the first 4 spacecrafts. After that it uses a random algorithm to allocate the rest of the parcels.

#### Pseudo greedy
For this part we looked at the properties of the spacecrafts. We saw for example that the Cygnus spacecraft can bring relatively few mass, but relatively a lot of volume. So we made a constraint that the big, light-weight parcels will be allocated in a Cygnus spacecraft. We did this for every spacecraft and added the constraints to the algorithm.

#### Random
After filling the first 4 or 6 spacecrafts with these constraints, the unpacked parcels will be random allocated in random spacecrafts (just as in the random algorithm).

With this algorithm you use every spacecraft at least once.

### Hill Climber
For our hill climber algorithm we use the random algorithm to generate a random start solution. After that we generate a neighbour solution. We have three different versions, depending on this neighbour solution. After generating the neighbour solution, the costs of this neighbour solution will be compared to the costs of the current solution. If the costs of the neighbour solution are lower, this neighbour solution will be set as the current solution. This will continue untill the maximum number iterations is reached.

#### Parcel switch
The neighbour solution is generated by picking a random parcel from a random spacecraft and switching this parcel with another random parcel from another random spacecraft. Then we check if the payload constraints still hold. If the constraints do not hold, we stop this iteration and go on to the next iteration. This means that also invalid switches count as an iteration.

#### Spacecraft switch
The neighbour solution is generated by picking a random spacecraft and putting the payload of this spacecraft in another random empty spacecraft. Then we check if the payload constraints still hold. If the constraints do not hold, we stop this iteration and go on to the next iteration. This means that also invalid switches count as an iteration.

#### Combined
The last heuristic choses random which of the abovementioned mutations will be used to generate the neighbour solution.

### Simulated Annealing
The simulated annealing algorithm also uses the random algorithm to generate a start solution. For the neighbour solution we only use the parcel and the combined option (see hill climber). We don't use the spacecraft option, since this will never give a better end solution. We still use the spacecraft option in the combined option, since the cooling scheme will never accept such an increase of costs.

The simulated annealing and the hill climber algorithm both accept neighbour solutions with a decrease of costs at any time. The difference between simulated annealing and hill climber is that the simulated annealing algorithm also sometimes accepts a neighbour solution with an increase of costs with a certain acceptance probabilty. The acceptance propability is calculated with the following formula:
```
acceptance = e^(change costs / temperature)
```
To determine the temperature, we use a cooling scheme. We have three options for the cooling scheme, however we noticed that the exponential cooling scheme worked best for our problem. Still you can choose between lineair, exponential or sigmoidal. For the cooling schemes we use the following the begin temperature (T_0) and end temperature (T_N):
+ T_0 =
+ T_N = 1
This is based on the average improvement of a hill climber run.

## Authors
+ Sofie Löhr, 11038926
+ Teska Vaessen, 11046341
+ Wies de Wit, 10727078

## Findings
If you are interested in our findings, please take a look at our presentation in the following link.

## Ackowledgments
+ StackOverflow
+ Minor Programming at the University of Amsterdam
