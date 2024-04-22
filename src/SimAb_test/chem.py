'''
Modified: Oct 23rd
@author: N. Khorshid

This is the chemistry module.
This module calculates the dust to gas ratio, and the abundances of different elements at a given temperature.
'''
import variable as var
import numpy as np


class Chem ():
    def __init__(self):
        name_s = 'input/N_Atom.txt'
        self.dat = np.loadtxt(name_s,dtype= str)
        self.solar = self.dat[0:, 5].astype(float)
        self.M_atm = self.dat[0:, 6].astype(float)
        self.chon = self.dat[0:, 4].astype(float)
        self.atm_nm = self.dat[0:,1]
        self.M_s_ARCiS = np.sum(self.solar[2:])/np.sum(self.solar[:2])
        self.MM_s = np.sum(self.solar[2:]*self.M_atm[2:])/np.sum(self.solar[:]*self.M_atm[:])
        #self.T_change= np.array([1600.,1300.,900.,700., 500.,120.,47.,20.])
        
    
    ###########################################################################    
    def mas_abnd(self,mas,T,con):
	#Calculates the abundases of the elements for the given mass, at the given position, for the given type of material
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
    
    ###########################################################################    
    def dTg(self,T):
	#Calculates the dust to gas ratio
        self.chem(T)
        return np.sum(self.sld*self.M_atm)/np.sum(self.gas*self.M_atm)
        
    ###########################################################################    
    def metalicity(self,ab_g,ab_s):
	#Calculates the metalicity of gas and dust together
        ab_tot = np.add(ab_s , ab_g)
        ab_tot = ab_tot/ab_tot[0]*1e12
        M = np.sum(ab_tot[2:])/np.sum(ab_tot[:2])
        self.mtl = np.log10(M/self.M_s_ARCiS)
    
    ###########################################################################    
    def metalicity_d(self,ab):
	#Calculates the metalicity of the given abundance
        ab_tot = ab/ab[0]*1e12
        M = np.sum(ab_tot[2:])/np.sum(ab_tot[:2])
        mtl = np.log10(M/self.M_s_ARCiS)
        return mtl
    ###########################################################################    
    def Mmetalicity(self,ab_g,ab_s):
	#Calculates the metalicity of gas and dust together
        ab_tot = np.add(ab_s , ab_g)
        ab_tot = ab_tot/ab_tot[0]*1e12
        M = np.sum(ab_tot[2:]*self.M_atm[2:])/np.sum(ab_tot[:]*self.M_atm[:])
        self.Mmtl = np.log10(M/self.MM_s)
    
    ###########################################################################    
    def Mmetalicity_d(self,ab):
	#Calculates the metalicity of the given abundance
        ab_tot = ab/ab[0]*1e12
        M = np.sum(ab_tot[2:]*self.M_atm[2:])/np.sum(ab_tot[:]*self.M_atm[:])
        mtl = np.log10(M/self.MM_s)
        return mtl
    ###########################################################################        
    def solaricity(self,ab_g,ab_s):
	#Converts the abundances to solar units
        self.sol = np.add(ab_g,ab_s)
        
        self.sol = self.sol/self.sol[0]*1e12
        self.sol = self.sol/self.solar
        
        
    ###########################################################################    
    def chem(self,T):
        #Sets the abundances based on the temperature
        if T<= 500:
            self.chem_LT(T)
        elif T>500:
            self.chem_HT(T)
        
    
    ###########################################################################
    def chem_LT (self,T):
        #Sets the abundances for themperatures less than 500K        
            
        self.sld = np.copy(self.chon)
        self.gas = self.solar - self.sld
        
	#Including CO ice:
        CO = np.zeros(2)
        CO[0] = np.copy(self.gas[3])*0.85
        CO[1] = CO[0]

        #Including CO2 ice: Add 0.4 to CO if not including CH4
        CO2 = np.zeros(2) 
        CO2[0] = np.copy(self.gas[3])*0.15
        CO2[1] = 2*CO2[0]
	
	# =============================================================================
	##Including CH4 ice: Add 0.08 to CO if not including CH4
        #CH4 = np.zeros(2) 
        #CH4[0] = np.copy(self.gas[3])*0.08 
        #CH4[1] = 4*CH4[0]
        # =============================================================================
	
	# =============================================================================
	##Including N2 ice: 
        #N2 = np.copy(self.gas[4])*0.93
	# =============================================================================

	# =============================================================================           
	##Including NH3 ice: Add 0.07 to N2 if not including NH3
        #NH3 = np.zeros(2) 
        #NH3[0] = np.copy(self.gas[4])*0.07
        #NH3[1] = 3*NH3[0]
	# =============================================================================        

	#Includinf H2O ice:
        H2O = np.zeros([2])
        H2O[1] = self.gas[5] - (CO[1]+CO2[1])
        H2O[0] = np.copy(H2O[0])*2
     
        if T<=var.T_ice_H2O:
            
            self.gas[0] -= H2O[0]
            self.gas[5] -= H2O[1]
            self.sld[0] += H2O[0]
            self.sld[5] += H2O[1]
            pass
        
        if T<=var.T_ice_CO2:
            
            self.gas[3] -= CO2[0]
            self.gas[5] -= CO2[1]
            self.sld[3] += CO2[0]
            self.sld[5] += CO2[1]
            pass
        
        if T<=var.T_ice_CO:
            
            self.gas[3] -= CO[0]
            self.gas[5] -= CO[1]
            self.sld[3] += CO[0]
            self.sld[5] += CO[1]
            pass
        
        if T<=var.T_ice_CH4:
            #self.gas[5] -= CH4[0]
            #self.gas[0] -= CH4[1]
            #self.sld[5] += CH4[0]
            #self.sld[0] += CH4[1]
            pass
        
        if T<=var.T_ice_N2:
            #self.gas[4] -= N2
            #self.sld[4] += N2
            pass
        
        if T<=var.T_ice_NH3:
            #self.gas[4] -= NH3[0]
            #self.gas[0] -= NH3[1]
            #self.sld[4] += NH3[0]
            #self.sld[0] += NH3[1]
            pass
    
    ###########################################################################    
    def chem_HT(self,T):
	#Sets the abundances for temperatures higher than 500K
        name= 'input/molec_ab.txt'
        dat = np.loadtxt(name,dtype= str)
              
        atm_T = dat[1:,0].astype(float)
        ind = [(atm_T<T) & (atm_T>(T-50)) | (atm_T == T)]
        if T>1550:
            ind[0][22] = True
        n = np.where(ind[0] == True)
        self.gas = dat[n[0][0]+1,1:].astype(float)
        
        self.sld = self.solar - self.gas
       
  
