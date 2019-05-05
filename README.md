# Space Freight
Teska Vaessen,
Wies de Wit, 10727078
Sofie Löhr, 11038926

## zorg dat iemand die het niet kent alles weet
documentatie heel belangrijk

## Usage

## Problem
The case Spacefreight is a constraint optimization problem (COP). The constraint that needs to be met is to ship all parcels from the cargolist(s). Multiple spacecrafts can be deployed to ship all parcels to the International Space Station (ISS).
The transportation costs need to be minimized, so the parcels from the cargolist(s) need to be distributed optimally to minimize costs.

The costs are divided in two categories, base costs and fuel costs. Every spacecraft has different base costs, the initial costs for the use of the spacecraft. Fuel costs depend on the mass of the spacecraft, the used payload mass and the Fuel-to-Weight ratio (FtW) of the spacecraft.

The mass (in kg) of fuel needed to deploy the spacecraft is calculated as follows:
F = (Mass + Payload-mass) x FtW / (1 - FtW)

The total amount of fuel is purchased per gram and costs $1 per gram, therefore the total costs of deploying the spacecraft are calculated as follows:
Base cost + roundup(F x 1000)

#### Upper & lower bound costs
When deploying all four spacecrafts once, we get the following upper- and lowerbound for the costs.

Lowerbound = 1.339430662 mld. dollar
Upperbound = 1.342566901 mld. dollar

The lowerbound is calculated by using a payload mass of 0 kg, which comes down to deploying the spacecraft without any payload.

The upperbound is calculated by using the maximum payloas mass of the spacecraft, which comes down to deploying the spacecraft with full capacity.

When deploying all six spacecrafts once, we get the following upper- and lowerbound for the costs calculated similarly.

Lowerbound = 2.838094712 mld. dollar
Upperbound = 2.843961701 mld. dollar

#### State Space
##### 100 parcels in 4 spacecrafts
5^100


#### Data
Structure:
+ Parcels
+ Spacecrafts
+ Spacefreight

mean parcel mass = 159.27899999999997 kg
mean parcel volume = 0.53474 m3

# Algorithms
iets dat state space kleiner maakt

#### iterative random
niet goede naam, bedenken wat een goede naam is goede stap richting waarom is deze beter

#### hill climber

#### greedy


Met iterative random is het gelukt om 96 parcels mee te nemen.

## Exercises
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
+ die met de constraints
