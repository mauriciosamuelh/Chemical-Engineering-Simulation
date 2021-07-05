# Isotermic PFR Reactor with axial dispersion in transient regime

A tubular non-ideal isotermic tubular reactor, occuring que first order tranformation A -> B

## Variables


![title](img/PFR.png)

## Model
The transient axial dispersion model, is given by:

<img src="/eq_1.png" height="20" />

Where: ![title](img/eq_2.png)

## Simulation parameters
| Symbol | Definition                                | Value | Unit    |
|--------|-------------------------------------------|-------|---------|
| CA0    | Initial concentration of A in one segment | 1.00  | mol.m-3 |
| D      | Axial effective difusity                  | 1.00  | m2.h-1  |
| k      | Reaction rate                             | 0.03  | h-1     |
| L      | Reactor length                            | 10.00 | m       |
| N      | Segment quantity                          | 5.00  | -       |
| ts     | Simulation duration                       | 50.00 | h       |
| u      | Flow speed                                | 1.00  | m.h-1   |

## Initial conditions
![title](img/initial condition.png)