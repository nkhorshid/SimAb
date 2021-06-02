"""
Created on Fri Feb 14 09:49:16 2020
@author: niloo

This is the main function that runs the whole formation code.
This function sets a random value to the initial conditions and the values for the final mass and position of the plaent.
n: is the run number

"""
import variable as var
from planet import Planet


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
elif plnt.check == 0:
        print ('this run can not be done')   

