# Space Freight
## Problem
The case Spacefreight is a constraint optimization problem (COP). The constraint that needs to be met is to ship all parcels from the cargolist(s). Other constraints are the maximum payload mass and the maximum payload volume of the spacecrafts. Each spacecraft has their own specifications. The maximum payloads of the spacecrafts cant be exceeded while allocating the parcels. Multiple spacecrafts can be deployed to ship all parcels to the International Space Station (ISS).

The transportation costs need to be minimized, so the parcels from the cargolist(s) need to be distributed optimally to minimize costs.

The costs are divided in two categories, base costs and fuel costs. Every spacecraft has different base costs, the initial costs for the use of the spacecraft. Fuel costs depend on the mass of the spacecraft, the used payload mass and the Fuel-to-Weight ratio (FtW) of the spacecraft.

The mass (in kg) of fuel needed to deploy the spacecraft is calculated as follows:
F = (Mass + Payload-mass) x FtW / (1 - FtW)

The total amount of fuel is purchased per gram and costs $1 per gram, therefore the total costs of deploying the spacecraft are calculated as follows:
Base cost + roundup(F x 1000)

### State Space & Bounds Costs
#### General
For the statespace we looked at the properties of each cargolist and of each spacecraft. We calculated the minimum amount of spacecrafts needed to bring all parcels and the (reasonal) maximum amount of spacecrafts needed. With this information we calculate the lower bound and upper bound of the state space as follows:

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
All Python scripts are in the folder Code. The Cargolists folder contains all three cargolists with their input values and in the Outputs folder are all results that are stored by the code.

### Testing
To run the code use the following instruction:
```
python main.py
```
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

This algorithm only has 1 solution. So this is of course not optimal.

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


### Simulated Annealing

## Authors
+ Sofie Löhr, 11038926
+ Teska Vaessen, 11046341
+ Wies de Wit, 10727078

## Ackowledgments
+ StackOverflow
+ Minor Programming at the University of Amsterdam
