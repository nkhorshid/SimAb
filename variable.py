'''
Modified: Oct 23rd
@author: N.Khorshid

This is the variable module.
This module sets the default values.
'''

"""
################################
#Constant values and units:
################################
"""
#Constant values:
#Global constant values
mp = 1.67 *10**(-27) # kg
G = 6.67 * 10**(-11) # m3*kg-1*s-2
sig = 5.67 *10**(-8) # W*m-2*K-4
kb = 1.38*10**(-23) #m2*kg*s-2*K-1


#unit converts and some constants
M_sun = 1.99e30 #kg
M_earth = 5.97e24 #kg
M_jupiter = 317.8*M_earth #kg
yr = 3.15e7 #sec
au = 1.5e11 #m
L_sun = 3.28e26 #w
#! Change rho_p to rho_solid
rho_p = 5000. #kg/m3
rho_ice = 2000. #kg/m3

#Disk that are assumed:
#! change to d2g or dust2gas
dTg = 0.01 #dust to gas

T_ice_H2O = 143.
T_ice_NH3 = 68.
T_ice_CO2 = 47.
T_ice_CH4 = 30.
T_ice_CO = 20.
T_ice_N2 = 18.

"""
##########################
Initial inputs:
##########################
"""
#! change dst to maindir
dst = 'Output/'
#!change dest to mainfile
dest ='output.txt'

#Planet:
#!change M_c and r_c to M_i and r_i
M_f = 1 #Mass of the initial core in Jupiter mass
M_c = 10 #Planet final mass in M_earth
r_c = 20.23 #distance of the core to the star AU
r_f = 0.02 #Planet final distance in AU


#Values
#Change dstg_r to dustgrain_ratio
dstg_r = 0.5
#change pls_r to planetesimal_ratio
pls_r = 0.5
#I do not even know what this is!
plsTg = 10

#Parameter
#Check to see if this C_max is needed and what it is
C_max = 2

#conditions:
#Chck to see of there are multiple conditions or not
con_pl = 2
con_chem = 1

#Step numbers:
n=100
