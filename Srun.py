"""
Created on Fri Feb 14 09:49:16 2020
@author: niloo

This is the main function that runs the whole formation code.
This function sets a random value to the initial conditions and the values for the final mass and position of the plaent.
n: is the run number

"""
import variable as var
from planet import Planet
from write import Write

t_dest = 'run_sum.txt'
w = open(t_dest,'a')

var.M_f = 1*var.M_jupiter
var.M_c = 10*var.M_earth
var.r_c = 30*var.au 
var.r_f = 0.02*var.au
var.dstg_r = 0.1
var.pls_r = 0.7
    

plnt = Planet(var.con_pl)
        
if plnt.check ==1:
    plnt.run()
    T = plnt.disk.tempr(var.r_c)
    print('result: ',plnt.C,plnt.ch.mtl,plnt.ch.sol[5]/plnt.ch.sol[3]*0.55)
    w.write('\ntest\t'+str(var.M_c/var.M_earth)+'\t'+str(plnt.M/var.M_earth)+'\t'+str(var.r_c/var.au)+
            '\t'+str(plnt.r/var.au)+'\t'+str(var.dstg_r)+'\t'+str(var.pls_r)+'\t'+str(T)+
            '\t'+str(plnt.ch.mtl)+'\t'+str(plnt.ch.sol[0])+'\t'+str(plnt.ch.sol[1])+'\t'+
            str(plnt.ch.sol[2])+'\t'+str(plnt.ch.sol[3])+'\t'+str(plnt.ch.sol[4])+'\t'+
            str(plnt.ch.sol[5])+'\t'+str(plnt.ch.sol[6])+'\t'+str(plnt.ch.sol[7])+'\t'+
            str(plnt.ch.sol[8])+'\t'+str(plnt.ch.sol[9])+'\t'+str(plnt.ch.sol[10])+'\t'+
            str(plnt.ch.sol[11])+'\t'+str(plnt.ch.sol[12])+'\t'+str(plnt.C))
    
elif plnt.check == 0:
        print ('this run can not be done')   

w.close()