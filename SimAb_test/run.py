"""
Created on Fri Feb 14 09:49:16 2020
@author: N.Khorshid

This is the main function that runs the whole formation code.
This function sets a random value to the initial conditions and the values for the final mass and position of the plaent.
n: is the run number

This function runs multiple runs with different initial formation parameters to form a planet of a given mass at a given distance

"""
import random
from SimAb_test import variable as var
from SimAb_test.planet import Planet
from SimAb_test.write import Write
import os
import sys

def single_run(PlanetMass=var.M_f,PlanetDistanse=var.r_f,CoreMass=var.M_c,CoreDistance=var.r_c,DustRatio=var.dstg_r, PlanetesimalRatio=var.pls_r):
    t_dest = 'run_sum.txt'
    w = open(t_dest,'a')

    var.M_f = PlanetMass*var.M_jupiter
    var.M_c = CoreMass*var.M_earth
    var.r_c = CoreDistance*var.au
    var.r_f = PlanetDistanse*var.au


    plnt = Planet(var.con_pl)

    if plnt.check ==1:
        plnt.run()
        T = plnt.disk.calculate_temperature(var.r_c)
        print('result: ',plnt.ch.Mmtl,plnt.ch.mtl,plnt.ch.sol[5]/plnt.ch.sol[3]*0.55)
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

def Multi_run(n=0,PlanetMass=var.M_f,PlanetDistanse=var.r_f, r_max = 250,r_min = 0.02, M_min = 5, M_max = 30,n_run = 2):
    os.mkdir(var.dst+'Run'+str(n))
    t_dest = var.dst + 'run_sum'+str(n)+'.txt'
    w = Write(t_dest,2)

    #Setting the initial values
    var.r_f = PlanetDistanse *var.au
    var.M_f = PlanetMass *var.M_jupiter
    #0.90, 3.63, 14.10 110.11
    r_max = r_max*var.au #Maximum initial orbital distance minus the minimum initial orbital distance in AU
    r_min = r_min*var.au #Minimum initial orbital distance in AU

    print ('This is the folder number ',n)
    i = 0
    while i<n_run:
        #Values
        var.dstg_r = random.uniform(0,1)
        var.pls_r = random.uniform(0,1)

        var.r_c = random.uniform(0.0,1.0)*r_max +r_min

        if var.dstg_r+var.pls_r<=1 and var.r_c != var.r_f:


            var.M_c = (random.uniform(0,1)*M_max+M_min)*var.M_earth
            #var.M_c= 10*var.M_earth
            plnt = Planet(var.con_pl)

            if plnt.check ==1:
                i += 1
                name = 'test'+str(i)
                var.dest = var.dst+'Run'+str(n)+'/'+name+'.txt'
                var.c_dest = var.dst+'Run'+str(n)+'/'+name+'_ch.txt'
                print ('###########Running ',name)


                plnt.run()
                T = plnt.disk.calculate_temperature(var.r_c)
                w.write(name+'\t'+str(var.M_c/var.M_earth)+'\t'+str(plnt.M/var.M_earth)+'\t'+str(var.r_c/var.au)+
                        '\t'+str(plnt.r/var.au)+'\t'+str(var.dstg_r)+'\t'+str(var.pls_r)+'\t'+str(T)+
                        '\t'+str(plnt.ch.Mmtl)+'\t'+str(plnt.ch.mtl)+'\t'+str(plnt.ch.sol[0])+'\t'+str(plnt.ch.sol[1])+'\t'+
                        str(plnt.ch.sol[2])+'\t'+str(plnt.ch.sol[3])+'\t'+str(plnt.ch.sol[4])+'\t'+
                        str(plnt.ch.sol[5])+'\t'+str(plnt.ch.sol[6])+'\t'+str(plnt.ch.sol[7])+'\t'+
                        str(plnt.ch.sol[8])+'\t'+str(plnt.ch.sol[9])+'\t'+str(plnt.ch.sol[10])+'\t'+
                        str(plnt.ch.sol[11])+'\t'+str(plnt.ch.sol[12])+'\t'+str(plnt.C))

                print ('end of ', name)
            elif plnt.check == 0:
                print ('this input did not converge\t',var.M_c/var.M_earth,'\t',var.r_c/var.au,'\t',var.dstg_r,'\t',var.pls_r)
    w.close()
