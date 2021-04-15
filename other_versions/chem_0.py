'''
Modified: Oct 23rd

This is the chemistry module
This verson has CO2 ice line
'''
import variable as var
import numpy as np
from write import Write


class Chem ():
    def __init__(self):
        name_s = 'input/N_Atom.txt'
        self.dat = np.loadtxt(name_s,dtype= str)
        self.solar = self.dat[0:, 5].astype(float)
        self.M_atm = self.dat[0:, 6].astype(float)
        self.chon = self.dat[0:, 4].astype(float)
        self.atm_nm = self.dat[0:,1]
        self.M_s = np.sum(self.solar[2:])/np.sum(self.solar[:])
        self.T_change= np.array([1600.,1300.,900.,700., 500.,120.,47.,20.])
        
    
        
    def mas_abnd(self,mas,T,con):
        
        self.chem(T)
        if con == 0 :
            #The mass is in gass:
            dTg= np.sum(self.sld*self.M_atm)/np.sum(self.gas*self.M_atm)           
            M_sld = mas*dTg *var.dstg_r
            M_gas = mas
            #*(1-dTg) *var.dstg_r 
            
            ab_mas_g = self.gas*self.M_atm
            ab_mas_g_t = np.sum(ab_mas_g)
            ab_g =M_gas *ab_mas_g/ab_mas_g_t/self.M_atm
            
            
        if con == 1:
            #The mass is all in solid
            M_sld = mas
            ab_g = np.zeros_like(self.gas)
            
        
        ab_mas_s = self.sld*self.M_atm
        ab_mas_s_t = np.sum(ab_mas_s)
        if ab_mas_s_t == 0:
            ab_mas_s_t = 1
        
        ab_d =M_sld *ab_mas_s/ab_mas_s_t/self.M_atm
            
        return (ab_g, ab_d)   
    
    
    def dTg(self,T):
        self.chem(T)
        return np.sum(self.sld*self.M_atm)/np.sum(self.gas*self.M_atm)
        
    
    def metalicity(self,ab_g,ab_s):
        ab_tot = np.add(ab_s , ab_g)
        ab_tot = ab_tot/ab_tot[0]*1e12
        M = np.sum(ab_tot[2:])/np.sum(ab_tot[:])
        self.mtl = np.log(M/self.M_s)
        
    def solaricity(self,ab_g,ab_s):
        self.sol = np.add(ab_g,ab_s)
        
        self.sol = self.sol/self.sol[0]*1e12
        self.sol = self.sol/self.solar
        
        
        #print 'compared tp solar',self.sol
        
    
    def chem(self,T):
        
        if T< 500:
            self.chem_LT(T)
        elif T>=500:
            self.chem_HT(T)
        
    
    
    
    
    
    #Functioning:
    def chem_LT (self,T):
                
            
        self.sld = np.copy(self.chon)
        self.gas = self.solar - self.sld
        
        CO = np.zeros(2)
        CO[0] = np.copy(self.gas[3])*0.8
        CO[1] = CO[0]
        
        CO2 = np.zeros(2)
        CO2[0] = np.copy(self.gas[3])*0.2
        CO2[1] = 2*CO2[0]
        
        H2O = np.zeros([2])
        H2O[1] = self.gas[5] - (CO[1]+CO2[1])
        H2O[0] = np.copy(H2O[0])*2
        
        T_ice_CO = 20
        T_ice_H2O = 120
        T_ice_CO2 = 47
        # =============================================================================
        #         print 'C in total:\t',self.gas[3],'\n C in CO:\t',CO[0],'\nC in CO2:\t',CO2[0]
        #         print 'remaining:\t', self.gas[3]-CO[0]-CO2[0]
        # =============================================================================
        if T<T_ice_H2O:
            
            self.gas[0] -= H2O[0]
            self.gas[5] -= H2O[1]
            self.sld[0] += H2O[0]
            self.sld[5] += H2O[1]
            pass
        
        if T<T_ice_CO2:
            
            self.gas[3] -= CO2[0]
            self.gas[5] -= CO2[1]
            self.sld[3] += CO2[0]
            self.sld[5] += CO2[1]
            pass
        
        if T<T_ice_CO:
            
            self.gas[3] -= CO[0]
            self.gas[5] -= CO[1]
            self.sld[3] += CO[0]
            self.sld[5] += CO[1]
            pass
    
    
    def chem_HT(self,T):
        name= 'input/molec_ab.txt'
        dat = np.loadtxt(name,dtype= str)
              
        atm_T = dat[1:,0].astype(float)
        ind = [(atm_T<T) & (atm_T>(T-50)) | (atm_T == T)]
        if T>1550:
            ind[0][22] = True
        n = np.where(ind[0] == True)
        self.gas = dat[n[0][0]+1,1:].astype(float)
        
        self.sld = self.solar - self.gas
       
  