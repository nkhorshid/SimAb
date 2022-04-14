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
rho_p = 5000. #kg/m3
rho_ice = 2000. #kg/m3

#Disk that are assumed:
dTg = 0.01

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
dst = 'Output/'
dest ='output.txt'

#Planet:
M_c = 20.*M_earth #Mass of the initial core in earth mass
r_c = 30.*au #distance of the core to the star AU
M_f = 318.*M_earth #Planet final mass inM_earth
r_f = 0.02*au #Planet final distance in AU


#Values 
dstg_r = 0.5
pls_r = 0.2
plsTg = 10
#Parameter
C_max = 2
#conditions:
con_pl = 2
con_chem = 1

#Step numbers:
n=100
