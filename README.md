# Space Freight
Teska Vaessen, 
Wies de Wit,
Sofie Löhr, 11038926


## Installation

## Usage

## Problem
Spacefreight is a constraint optimization problem (COP) 

#### Upper & lower bound costs
Lowerbound = 1,339 mld. dollar
Upperbound = 1,343 mld. dollar

#### State Space

#### Data structure
+ Parcels
+ Spacecrafts
+ Spacefreight

### Algorithms

Met iterative random is het gelukt om 96 parcels mee te nemen. 62 pakketjes gaan altijd mee met het sorted deel, de overige 34 zijn random en varieren dus per run.


## Exercises
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



