# Space Freight
<!-- ## zorg dat iemand die het niet kent alles weet
documentatie heel belangrijk -->

## Belangrijkst:
Met de hill climber parcel switch zijn we er achter gekomen dat het wisselen van parcels weinig verschil maakt en de start vloot eigenlijk alles bepalend is. (resultaten verbeteren maximaal met 13000 tov miljarden)

Wanneer je spacecrafts wisselt verbeteren de resultaten wel met honderden miljoenen door de grote verschillen in initiele kosten van de spacecrafts.

Zelfde bij simulated annealing gevonden (parcel switch)

Geprobeerd dit te kwantificeren: random gesorteerd op goedkoopste kosten en onderzocht of dit idd vaak dezelfde vloot heeft

Daarnaast ook de hele case afgerond.

## VERSCHILLENDE ALGORITMES
* first fit
+ volgorde van cargolist en spacecraft
+ parcels gesorteerd op massa
+ parcels gesorteerd op volume
* random
* pseudo greedy random
* hill climber
+ swap parcels
+ swap spacecrafts
* simulated annealing
+ parcels
* political constraints (opdracht e)

## Problem
The case Spacefreight is a constraint optimization problem (COP). The constraint that needs to be met is to ship all parcels from the cargolist(s). Other constraints are the maximum payload mass and the maximum payload volume of the spacecrafts. Each spacecraft has their own specifications. The maximum payloads of the spacecrafts cant be exceeded while allocating the parcels. Multiple spacecrafts can be deployed to ship all parcels to the International Space Station (ISS).

The transportation costs need to be minimized, so the parcels from the cargolist(s) need to be distributed optimally to minimize costs.

The costs are divided in two categories, base costs and fuel costs. Every spacecraft has different base costs, the initial costs for the use of the spacecraft. Fuel costs depend on the mass of the spacecraft, the used payload mass and the Fuel-to-Weight ratio (FtW) of the spacecraft.

The mass (in kg) of fuel needed to deploy the spacecraft is calculated as follows:
F = (Mass + Payload-mass) x FtW / (1 - FtW)

The total amount of fuel is purchased per gram and costs $1 per gram, therefore the total costs of deploying the spacecraft are calculated as follows:
Base cost + roundup(F x 1000)

### State Space
#### General
For the statespace we looked at the properties of each cargolist and of each spacecraft. We calculated the minimum amount of spacecrafts needed to bring all parcels and the (reasonal) maximum amount of spacecrafts needed. With this information we calculate the lower bound and upper bound of the state space as follows:

+ Lower bound = (Minimum amount of spacecrafts)^(number of parcels in cargolist)
+ Upper bound = (Maximum amount of spacecrafts)^(number of parcels in cargolist)

#### Cargolist 1
So the state space for cargolist 1 is:

+ Lower bound = 4^100 = 1,61 * 10^60
+ Upper bound = 8^100 = 2,04 * 10^90

#### Cargolist 2
So the state space for cargolist 2 is:

+ Lower bound = 5^100 = 7,89 * 10^69
+ Upper bound = 8^100 = 2,04 * 10^90

##### Cargolist 3
So the state space for cargolist 3 is:

+ Lower bound = 46^1000 = 1,89 * 10^166
+ Upper bound = 84^1000 = 2,68 * 10^192

VRAAG: HEBBEN WE HIER REKENING GEHOUDEN MET DE 6 SPACECRAFTS BIJ LIJST 3 WANT MOETEN WE EIGENLIJK WEL DOEN

### Upper & lower bound costs
When deploying all four spacecrafts once, we get the following upper- and lowerbound for the costs.

Lower bound = 1.339430662 mld. dollar
Upper bound = 1.342566901 mld. dollar

The lower bound is calculated by using a payload mass of 0 kg, which comes down to deploying the spacecraft without any payload.

The upper bound is calculated by using the maximum payloas mass of the spacecraft, which comes down to deploying the spacecraft with full capacity.

When deploying all six spacecrafts once, we get the following upper- and lowerbound for the costs calculated similarly.

Lower bound = 2.838094712 mld. dollar
Upper bound = 2.843961701 mld. dollar

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
Type here the algorithm you want to run. Options: random, pseudo greedy random, random all, pseudo greedy random all, hill climber, hill climber spacecrafts, hill climber combined, simulated annealing, simulated annealing combined, political constraints.

### Data
Structure:
+ Parcels
+ Spacecrafts
+ Spacefreight

## Algorithms
iets dat state space kleiner maakt

### First fit
The first fit algorithm is a greedy algorithm. With this algorithm we loop over the spacecrafts in the order they are loaded and then loop over the parcels in the order they are loaded. So we take the first spacecraft and place the first parcel in this spacecrafts. Then for every parcel we check if it still fits in the first spacecraft and if it fits, it goes in the first spacecraft. Then if we checked every parcel, we do the same for the second spacecraft. Here we also check if the parcel is still unpacked. Then we do this for the third spacecraft and so on.

This algorithm only has 1 solution. So this is of course not optimal.

### Random
Our random algorithm is not greedy. This algorithm basically does the same as our first fit algorithm, though the random algorithm does everything in random order. So it first picks a random spacecraft, then the cargolist will be in a random order and it fills the spacecrafts. Then it picks another random spacecraft (which can be the same as the first one) and fills this one. This goes on untill all parcels are packed.

With this algorithm you can make every solution in the state space. Which is not optimal, since it will take forever to find the most optimal solution.

### Pseudo greedy and random
This algorithm first uses a pseudo greedy heuristic (multiple constraints) to fill the first 4 spacecrafts. After that it uses a random algorithm to allocate the rest of the parcels.

#### Pseudo greedy
For this part we looked at the properties of the spacecrafts. We saw for example that the Cygnus spacecraft can bring relatively few mass, but relatively a lot of volume. So we made a constraint that the big, light-weight parcels will be allocated in a Cygnus spacecraft. We did this for every spacecraft and came up with the following constraints:
```
if parcel mass < mean mass / 2 and parcel volume > mean volume * 2:
    parcel in Cygnus

if parcel mass < mean mass and parcel volume < mean volume / 2:
    parcel in Progress

if parcel mass > mean mass and parcel volume > mean volume:
    parcel in Kounotori

if parcel mass > mean mass and parcel volume < mean volume:
    parcel in Dragon

if parcel mass > mean mass * 2 and parcel volume > mean volume:
    parcel in TianZhou

if parcel mass > mean_mass * 2 and parcel volume > mean volume * 2:
    parcel in Verne ATV
```
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

<!-- Met iterative random is het gelukt om 96 parcels mee te nemen. -->

<!-- ## Exercises
Hoeft niet
### a

It is impossible to bring more than 97 parcels in the 4 spacecrafts since the total mass and volume of the parcels exceeds the sum of the payload mass and payload volume of the spacecrafts. Not bringing 2 of the heaviest parcels makes it theorethical possible to bring 97 parcels.

#### Mass & volume of all the parcels Cargolist1
mass = 15.927,9 kg
volume = 53,474 m3

#### Sum of payload mass & volume of spacecrafts
mass = 15.600 kg
volume = 50,5 m3

With the algorithms we made (greedy/random/first fit) we managed to bring 96 parcels in a reasonable runningtime.

### b

As told in exercise a you can't bring more than 97 parcels. We managed to bring 96.




constructief vs iteratief

2 verschillende algoritmes wat we hebben, tes vragen
+ first fit
+ die met de constraints -->
