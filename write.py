"""
Created on Fri Feb 14 09:49:16 2020

@author: niloo

This module does all the writing that is needed during the run
mod = 1 is used to write all the information of each step for a single simulation
mod = 2 is used to write the important information about the final stage of the simulations
"""
import variable as var

class Write():
    def __init__(self,direct,mod,C=0):
        if mod ==1:
            header_i = 'M_c\ta_c\tM_fin\ta_fin\tdstg_r\tpls_r\tC\n'
            header = 'time\tM\tr\tT\tdm_g\tdm_pls\tdTg\n'
            self.f = open(direct,'w')
            self.f.write(header_i)
            self.f.write(str(var.M_c/var.M_earth)+'\t'+str(var.r_c/var.au)+'\t'+
                         str(var.M_f/var.M_earth)+'\t'+str(var.r_f/var.au)+'\t'+
                         str(var.dstg_r)+'\t'+str(var.pls_r)+'\t'+str(C)+'\n')
            self.f.write(header)
        elif mod ==2:
            header = 'Test\tM_c\tM_fin\ta_c\ta_fin\tdstg_r\tpls_r\ttemperature\tmetalicity\tH\tHe\tLi\tC\tN\tO\tNa\tMg\tAl\tSi\tS\tK\tFe\talpha_inverse\n'
            self.f = open(direct,'w')
            self.f.write(header)
            
    
    def write(self,*argv):
        for arg in argv:
            self.f.write(str(arg)+'\t')
            
        self.f.write('\n')
      
    def close(self):
        self.f.close()
