'''
Modified: Oct 23rd
@author: N.Khorshid

This module forms the planet and calculates its abundances.
'''
import numpy as np
from SimAb_test import variable as var
from SimAb_test.disk import Disk
from SimAb_test.disk import Star
from SimAb_test.write import Write
#Be carful about this, change it to Chem
from SimAb_test.chem import Chem
import sys

class Planet():
    """
    Planet properties
    """

    ###########################################################################
    def __init__ (self,i):
        #set condition:
        self.con = i
        if self.con == 2:
            #self.C = 1.67785
            self.C_max = var.C_max
            self.C_min = 0.
            self.con1 = 0
            self.ch = Chem()

            #Set environment
            self.star = Star()
            self.disk = Disk()
            self.r_ice = self.disk.r_arr[4:]

        #Set Planet:
        self.M = var.M_c
        self.r = var.r_c

        #Set variables:
        self.d_mig = 0
        self.time = np.zeros([1])
        self.dm_g =np.zeros([0])
        self.dm_d =np.zeros([0])
        self.arr_r=np.zeros([0])
        self.abn = np.zeros([2,13])
        self.abn_t = np.zeros([2,13])

        self.exe([0,0])


    ###########################################################################
    #Running functions
    def evolve(self,d):
        self.time = np.append(self.time,self.time[-1]+d[0])
        self.r = self.r - d[1]
        self.arr_r = np.append(self.arr_r,self.r)
        self.disk.evolve(self.r)

        self.r_hsphere()
        if self.con == 3 or self.con==2:
            self.set_migration()

    def set_migration(self):

        #Method 0
        if self.con == 0:
            if self.con1==2:
                self.con =2
                self.dt = self.C*self.r*self.disk.ang_v/(self.disk.a*self.disk.Cs**2)*self.dr

        if self.con == 2:
            if self.con1==2:
                self.dt = self.C*self.r*self.disk.ang_v/(self.disk.a*self.disk.Cs**2)*self.dr
            else:
                j = 0
                while j<3:
                    self.C = self.C_max
                    a = self.optimize(10)

                    if a== -1:
                        self.C_max = self.C_max * 5.
                    else:
                        j=10
                    self.__init__(0)

                j = 0
                self.C = (self.C_max - self.C_min)/2.

                while j<15:

                    j+=1
                    a = self.optimize(var.n)
                    if a == -1 and j!=15:
                        self.C_min = self.C
                        self.C = (self.C_max - self.C_min)/2. +self.C_min

                    elif a== 0 and j!=15:
                        self.C_max = self.C
                        self.C = (self.C_max - self.C_min)/2.+self.C_min
                    elif a==1:
                        j = 15
                        self.check = 1
                    else:
                        self.check = 0

                    self.__init__(0)






    def optimize(self,n):
        self.r_min = self.r+self.rh
        self.dr = (self.r-var.r_f)/n
        self.dt = self.C*self.r*self.disk.ang_v/(self.disk.a*self.disk.Cs**2)*self.dr

        self.con1 = 2
        self.run_test()

        a=1
        if self.M>(1.001*var.M_f):
            #print ('Mass is big')
            a = 0
        elif self.M<(0.999*var.M_f):
            #print ('Mass is small')
            a =-1
        else:
            #print ('Mass: good enough')
            a = 1
        return a


    def exe(self,d):
        self.evolve(d)
        self.set_migration()


    def run_test(self):

        while (self.r>1.0001*var.r_f):
            self.mas_acc()
            self.evolve([self.dt,self.dr])
        self.mas_acc()

    def run(self):
        self.r_min = self.r+self.rh
        self.w = Write(var.dest,1,self.C)

        self.w.write(0,self.M/var.M_earth,self.r/var.au,self.disk.T,0,0,self.ch.dTg(self.disk.T))
        while (self.r>1.0001*var.r_f):
            self.mas_acc()
            self.w.write(self.dt/var.yr,self.M/var.M_earth,self.arr_r[-1]/var.au,self.disk.T,self.dm_g[-1]*self.dt/var.M_earth,self.dm_d[-1]/var.M_earth,self.dTg)
            self.evolve([self.dt,self.dr])
        self.mas_acc()

        self.ch.metalicity(self.abn_t[0,:], self.abn_t[1,:])
        self.ch.Mmetalicity(self.abn_t[0,:], self.abn_t[1,:])
        self.w.write(self.dt/var.yr,self.M/var.M_earth,self.arr_r[-1]/var.au,self.disk.T,self.dm_g[-1]*self.dt/var.M_earth,self.dm_d[-1]/var.M_earth,self.dTg)

        self.ch.solaricity(self.abn_t[0,:], self.abn_t[1,:])
        self.w.close()

    def mas_acc(self):

        if (abs(self.r - self.r_ice) < self.rh).any():
            ind = np.where(abs(self.r - self.r_ice) < self.rh)[0][0]
            self.disk.evolve(self.r +self.rh)
            T = self.disk.T
            r_min = self.r_ice[ind]
            self.d_mig =(self.r_min**2 - r_min**2) * np.pi
            self.r_min = r_min
            self.dm_d = np.append(self.dm_d,self.solid_acc())
            abn = self.ch.mas_abnd(self.dm_d[-1],T,1)
            self.abn_t += abn

            self.disk.evolve(self.r -self.rh)
            T = self.disk.T+1
            self.migration()
            dm_t = self.solid_acc()
            self.dm_d[-1] += dm_t
            abn = self.ch.mas_abnd(dm_t,T,1)


        else:
            T = self.disk.T
            self.migration()
            self.dm_d = np.append(self.dm_d,self.solid_acc())
            abn = self.ch.mas_abnd(self.dm_d[-1],T,1)

        self.abn_t += abn
        self.dm_g = np.append(self.dm_g,self.gas_acc())
        abn = self.ch.mas_abnd(self.dm_g[-1]*self.dt,self.disk.T,0)
        self.abn_t += abn
        self.M += (self.dm_g[-1]*self.dt+self.dm_d[-1])




    ###########################################################################
    #equation functions:
    def gas_acc(self):
        m1 = 3*np.pi*self.disk.a

        #m2 = (self.rh/(3*self.disk.H))**(3.)
        m2 = (self.rh/self.disk.H)**(9/2.)

        return self.disk.H**2*self.disk.ang_v*self.disk.dns*min(m1,m2)

    def solid_acc(self):
        self.dTg = self.ch.dTg(self.disk.T)


        #set up 4
        dens = self.disk.dns*self.dTg
        sld_acc =dens*self.d_mig*var.pls_r

        return sld_acc




    def r_hsphere(self):
        self.rh = (self.M/(3.*self.star.M))**(1./3.)*(self.r)

    def migration(self):
        if self.dr == 0:
            self.d_mig = 0
            pass
        else:
            r_min = self.r - self.rh

            self.d_mig =(self.r_min**2 - r_min**2) * np.pi
            self.r_min = r_min
