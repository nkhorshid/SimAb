'''
Modified: Oct 23rd
@author: N. Khorshid

This is the disk module.
We use the dust to gas ratio from the chemistry module to calculate the density profile of the disk.
For the temperature, we asume a dust to gas ratio of 0.01.
The temperature is calculated as the maximum value between an irradiation temperature (T_irr) and a viscosity temperature (T_vis)
'''
import variable as var
import numpy as np
from chem import Chem


"""
##########################
Functions and classes
##########################
"""
class Star:
    """
    Star properties
    """
    def __init__ (self):
        self.M = 1.*var.M_sun
        self.L = 1.*var.L_sun
        

"""
===============================================================================
"""   

    
class Disk:
   
    def __init__ (self):
        
        self.ch = Chem()
       
        #Initial values
        self.star = Star()
        self.M = 0.01*self.star.M
        self.R = 20.*var.au #m
        self.et = 0.01 #Gas velocity / Kepplerian velocity
        
        #define parameters
        self.a = 0.1
        self.M_acc = 10**(-7)* var.M_sun/var.yr #kg/sec
        self.mu = 2.5
        self.f_ice = 1
        self.kr =50 #kg,m
        self.dTg_t = 0.01
        #Parameters changing with distance:
        
        self.calc_r()
        #Chemistry
        name_s = 'input/N_Atom.txt'
        self.dat = np.loadtxt(name_s,dtype= str)
        self.solar = self.dat[0:, 5].astype(float)
        self.M_atm = self.dat[0:, 6].astype(float)
        self.chon = self.dat[0:, 4].astype(float)
        self.atm_nm = self.dat[0:,1]
        
        
    ###########################################################################
    def evolve(self, r):
	#Sets the values for the disk at the given orbital distance
        self.set_dtg(r)
        self.T = self.tempr(r)
        self.dens(r)
        
    ###########################################################################
    def set_dtg(self, r):
	#Finds the dust to gas ratio at the given orbital distance
        idx = (np.abs(self.r_arr - r)).argmin()
        if self.r_arr[idx]> r:
            idx = idx -1
        if idx<0:
            idx = 0
        self.dTg = self.dtg[idx]
        
    ###########################################################################
    def tempr(self, r):
       	#Calculates th etemperature at the given orbital distance
        cons = (3*self.mu*var.mp*self.kr*self.dTg_t)/(128*np.pi**2*self.a*var.kb*var.sig)

        T_vis = (cons*self.M_acc**2*(var.G*self.star.M/r**3)**(3./2))**(1./5)
        T_irr = 150*(self.star.L/var.L_sun)**(2./7)*(self.star.M/var.M_sun)**(-1./7)*(r/var.au)**(-3./7)
        #T = (T_vis**4.+T_irr**4.)**(1./4)
        T=max(T_vis,T_irr)
        
        self.Cs = np.sqrt(var.kb*T/(self.mu*var.mp))
        self.ang_v = (var.G*self.star.M/r**3.)**(1/2.)
        self.H = self.Cs/self.ang_v
        
        return T

    ###########################################################################
    def dens(self,r):
	#Calculates the density at the given orbital distance
        cons = self.mu*var.mp/(3*np.pi*self.a*var.kb)
        self.dns = (cons/self.T) * (self.M_acc*(var.G*self.star.M/(r)**3)**(1./2))
        
    def dens_r(self,r):
	#Is used for ploting density profile of the disk
        self.set_dtg(r)
        T= self.tempr(r)
        cons = self.mu*var.mp/(3*np.pi*self.a*var.kb)
        dns = np.zeros(2)
        dns[0] = (cons/T) * (self.M_acc*(var.G*self.star.M/(r)**3)**(1./2))
        dns[1] = dns[0]*self.dTg
        return dns
    ###########################################################################
    def calc_r(self):
	#Calculates the orbital distance at the temperatures the abundances in the disk changes
        self.T_arr = np.array([1600.,1550.,1250.,1200.,1150.,850.,650., 550.,500.,var.T_ice_H2O,var.T_ice_CO2,var.T_ice_CO])
        self.dtg = np.zeros_like(self.T_arr)
        self.r_arr = np.zeros_like(self.T_arr)
 
        const = (3.*self.mu *var.mp*self.kr)/(128.*np.pi**2.*self.a*var.kb*var.sig)
        cons2 = 150*(self.star.L/var.L_sun)**(2./7)*(self.star.M/var.M_sun)**(-1./7)*(1/var.au)**(-3./7)
        for i in range(len(self.T_arr)):
            self.dtg[i] = self.ch.dTg(self.T_arr[i]) 
            cons1 = const *self.dTg_t
            r1 = ((cons1*self.M_acc**2/self.T_arr[i]**5)**(2./3)*var.G*self.star.M)**(1./3)
            r2 = (cons2/self.T_arr[i])**(7/3)

            self.r_arr[i] = max(r1,r2)

    
    def convert_T(self,T):
	#Calculates the orbital distance given the temperature
         const = (3.*self.mu *var.mp*self.kr)/(128.*np.pi**2.*self.a*var.kb*var.sig)
         cons2 = 150*(self.star.L/var.L_sun)**(2./7)*(self.star.M/var.M_sun)**(-1./7)*(1/var.au)**(-3./7)
         dtg = self.dTg_t
         cons1 = const *dtg
         r1 = ((cons1*self.M_acc**2/T**5)**(2./3)*var.G*self.star.M)**(1./3)
         r2 = (cons2/T)**(7/3)
         r = max(r1,r2)
         return r
