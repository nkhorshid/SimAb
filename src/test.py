"""
Created on Fri Feb 14 09:49:16 2020
@author: N.Khorshid

This is the main function that runs the whole formation code.
This function sets a random value to the initial conditions and the values for the final mass and position of the plaent.
n: is the run number

This function runs multiple runs with different initial formation parameters to form a planet of a given mass at a given distance

"""
import run

run.single_run(PlanetMass=3,PlanetDistanse=0.2,CoreMass=15,CoreDistance=100,DustRatio=0.0, PlanetesimalRatio=0.1)
run.Multi_run(n=1,PlanetMass=3,PlanetDistanse=0.2,n_run = 2)
