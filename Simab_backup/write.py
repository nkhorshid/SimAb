"""
Created on Fri Feb 14 09:49:16 2020

@author: niloo

This module does all the writing that is needed during the run
"""
import numpy as np
import variable as var

header1 = 'M_c\ta_c\tM_fin\ta_fin\tdstg_r\tpls_r\n'
header2 = 'time\tM\tr\tT\tdm_g\tdm_pls\n'
header3 = 'Test\tM_ctM_tot\ta_c\ta_fin\tdstg_r\tpls_r'


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
            header = 'Test\tM_c\tM_fin\ta_c\ta_fin\tdstg_r\tpls_r\ttemperature\tmetalicity\tH\tHe\t\tLi\tC\tN\tO\tNa\tMg\tAl\tSi\tS\tK\tFe\tC\n'
            self.f = open(direct,'w')
            self.f.write(header)
        elif mod ==3:
            header1 = 'T\tH(g)\tHe(g)\tLi(g)\tC(g)\tN(g)\tO(g)\tNa(g)\tMg(g)\tAl(g)\tSi(g)\tS(g)\tK(g)\tFe(g)\t'
            header2 = 'H(s)\tHe(s)\tLi(s)\tC(s)\tN(s)\tO(s)\tNa(s)\tMg(s)\tAl(s)\tSi(s)\tS(s)\tK(s)\tFe(s)\tmetalicity\n'
            self.f = open(direct,'w')
            self.f.write(header1)
            self.f.write(header2)
            
            
    
    def write(self,*argv):
        for arg in argv:
            self.f.write(str(arg)+'\t')
            
        self.f.write('\n')
      
    def close(self):
        self.f.close()
