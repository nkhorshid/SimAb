# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Created to try to help Niloo with work

import numpy as np
from subprocess import call

'''
dat = np.loadtxt('testratrancode.inp',skiprows=6)
f = open('lookatmytesttxtfile.txt','w')
f.write(mystr)

for i in dat:
    tempstr = ''
    for j in i:
        tempstr += str(j) + '\t'
    f.write(tempstr + '\n')
    
f.close()
'''


#main function when given a file to read under src_destin/src_name, 
#changes the values of column 4 for all rows except the first, and 

#writes the new file to a certain destination under
#result_destin/result_name. 
def main(src_name,src_destin,result_name,result_destin,change):    
    #The string which is the first 6 rows of your file
    #which you don't want changed
    mystr = 'rmax=2.760e+15\nncell=22\ntcmb=2.728\ncolumns=id,ra,rb,nh,nm,tk,td$
    #loading in the data
    dat = np.loadtxt(src_destin+src_name,skiprows=6)
    #changing the values of the data to be what you want
    #without changing the first row
    dat[1:,4] = change
    #starting to write the new file
    f = open(result_destin+result_name,'w')
    f.write(mystr)
    #writing in each row
    for i in dat:
        tempstring = ''
        for j in i:
            tempstring += str(j)+'\t'
        f.write(tempstring+'\n')
    #closing and you're done!
    f.close()


sd = '/home/khorshid/Downloads/'
sf = 'testratrancode.inp'
rd = '/home/khorshid/Documents/'
rf = 'example.mdl'
c = 75




nb = 'example'
ne = '.mdl'
nd = '/home/khorshid/Documents/'
main(sf,sd,rf,rd,c)
   
   
   
   
#call('amc amc.inp','sky sky.inp')

call('cp '+rd+rf + ' ' + nd+nb+str(c)+ne)
#call('cp '+putwhereamcresultgoeshere + ' ' + nd+nb+str(c)+'result'+ne)



