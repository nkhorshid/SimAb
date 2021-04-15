'''
Modified: Oct 23rd

This is the disk module
This version uses the dTg from chemistry module
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
   
    ###########################################################################
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
        #self.dTg = 0.01
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
        self.set_dtg(r)
        self.T = self.tempr(r)
        self.dens(r)
        
    ###########################################################################
    def set_dtg(self, r):
        idx = (np.abs(self.r_arr - r)).argmin()
        if self.r_arr[idx]> r:
            idx = idx -1
        self.dTg = self.dtg[idx]
        
    ###########################################################################
    def tempr(self, r):
        self.set_dtg(r)
        cons = (3*self.mu*var.mp*self.kr*self.dTg)/(128*np.pi**2*self.a*var.kb*var.sig)

        T = (cons*self.M_acc**2*(var.G*self.star.M/r**3)**(3./2))**(1./5)
        self.Cs = np.sqrt(var.kb*T/(self.mu*var.mp))
        self.ang_v = (var.G*self.star.M/r**3.)**(1/2.)
        self.H = self.Cs/self.ang_v
        
        return T

    ###########################################################################
    def dens(self,r):
        cons = self.mu*var.mp/(3*np.pi*self.a*var.kb)
        self.dns = (cons/self.T) * (self.M_acc*(var.G*self.star.M/(r)**3)**(1./2))
        
    def dens_r(self,r):
        T= self.tempr(r)
        cons = self.mu*var.mp/(3*np.pi*self.a*var.kb)
        dns = np.zeros(2)
        dns[0] = (cons/T) * (self.M_acc*(var.G*self.star.M/(r)**3)**(1./2))
        dns[1] = dns[0]*self.dTg
        return dns
    ###########################################################################
    def calc_r(self):
        #This function calculates the R where the jump in the chemistry happens
        #I first check with just CO ice line, then check with the other ones and
        #see if that is important or not.
        # reurns a list of distances
        #print ('the function is done')

        self.T_arr = np.array([1600.,1300.,900.,700., 500.,var.T_ice_H2O,var.T_ice_CO2,var.T_ice_CO])
        self.dtg = np.zeros_like(self.T_arr)
        self.r_arr = np.zeros_like(self.T_arr)
 
        const = (3.*self.mu *var.mp*self.kr)/(128.*np.pi**2.*self.a*var.kb*var.sig)
        
        for i in range(len(self.T_arr)):
            self.dtg[i] = self.ch.dTg(self.T_arr[i]) 
            #self.dtg[i] = 0.01
            cons = const *self.dtg[i]
            self.r_arr[i] = ((cons*self.M_acc**2/self.T_arr[i]**5)**(2./3)*var.G*self.star.M)**(1./3)
        self.dtg[0] = self.dtg[1]
    
    def convert_T(self,T):
         const = (3.*self.mu *var.mp*self.kr)/(128.*np.pi**2.*self.a*var.kb*var.sig)
         dtg = self.ch.dTg(T)
         #dtg = self.dTg
         cons = const *dtg
         r = ((cons*self.M_acc**2/T**5)**(2./3)*var.G*self.star.M)**(1./3)
         return r