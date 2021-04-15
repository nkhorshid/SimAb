"""
Created on Fri Feb 14 09:49:16 2020

@author: niloo

This version of Run is compatible with the version of chemistry and planet
that first writes info about the formed planet in test#.txt and then read form it

"""
import random
import variable as var
from planet import Planet
from write import Write
import sys
import numpy as np



n = sys.argv[1]
op = np.array([0.03,0.2,1,5,15,35])

var.r_c = op[int(n)]* var.au

t_dest = var.dst + 'run_sum'+str(n)+'.txt'
w = Write(t_dest,2)
var.r_f = 0.02*var.au
r_max = 100*var.au
r_min = 0.02*var.au
var.con_pl = 2
var.con_chem = 1


print 'This is the folder number ',n,'\n This is the dust grain ratio value', var.dstg_r
i = 0
while i<1000:
    #Values 
    #var.dstg_r = random.uniform(0,1)
    #var.pls_r = random.uniform(0,1)
    #var.r_c = random.uniform(0.0,1.0)*r_max +r_min
    
    if var.dstg_r+var.pls_r<=1 and var.r_c != var.r_f:
        
        
        var.M_c = (random.uniform(0,1)*30+5)*var.M_earth
        #print '******************values',var.M_c/var.M_earth,'\t',var.r_c/var.au,'\t',var.pls_r ,'\t',var.dstg_r
        plnt = Planet(var.con_pl)
        
        if plnt.check ==1:
            i += 1
            name = 'test'+str(i)
            var.dest = var.dst+'Run'+str(n)+'/'+name+'.txt'
            var.c_dest = var.dst+'Run'+str(n)+'/'+name+'_ch.txt'
            print '###########Running ',name
            
        
            plnt.run()
            T = plnt.disk.tempr(var.r_c)
            w.write(name+'\t'+str(var.M_c/var.M_earth)+'\t'+str(plnt.M/var.M_earth)+'\t'+str(var.r_c/var.au)+
                    '\t'+str(plnt.r/var.au)+'\t'+str(var.dstg_r)+'\t'+str(var.pls_r)+'\t'+str(T)+
                    '\t'+str(plnt.ch.mtl)+'\t'+str(plnt.ch.sol[0])+'\t'+str(plnt.ch.sol[1])+'\t'+
                    str(plnt.ch.sol[2])+'\t'+str(plnt.ch.sol[3])+'\t'+str(plnt.ch.sol[4])+'\t'+
                    str(plnt.ch.sol[5])+'\t'+str(plnt.ch.sol[6])+'\t'+str(plnt.ch.sol[7])+'\t'+
                    str(plnt.ch.sol[8])+'\t'+str(plnt.ch.sol[9])+'\t'+str(plnt.ch.sol[10])+'\t'+
                    str(plnt.ch.sol[11])+'\t'+str(plnt.ch.sol[12])+'\t'+str(plnt.C))
            
            print 'end of ', name
        elif plnt.check == 0:
            print 'this run can not be done\t',var.M_c/var.M_earth,'\t',var.r_c/var.au,'\t',var.dstg_r,'\t',var.pls_r     
          
w.close()
