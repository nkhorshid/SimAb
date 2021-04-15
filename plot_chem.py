"""
Created on Fri Feb 14 09:49:16 2020

@author: niloo
This plot, plots thechemistry in gas and solid phase for the given elements
"""
import numpy as np
import matplotlib.pyplot as plt
import variable as var
import matplotlib.pylab as pylab
from chem1 import Chem

#plt.close('all')
params = {'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

pt = np.array([2000,1550,1250,1200,1150,850,650,
               500,499,120,119,47,46,20,19,10])
pd = np.array([0.1, 0.25681085, 0.32614839, 0.34128238, 0.35780877,
               0.50062951, 0.67447689, 0.90275687, 4.40783142,
               12.48935045,32.27286169, 50])

# =============================================================================
# [ 0.25681085  0.32614839  0.34128238  0.35780877 
#   0.50062951  0.67447689  0.90275687  4.40783142 
#   12.48935045 32.27286169]
# [1550         1250        1200        1150
#  850          650         500         120
#  47           20]
# 
# =============================================================================

H  = np.zeros([2,pt.shape[0]])
He = np.zeros([2,pt.shape[0]])
Li = np.zeros([2,pt.shape[0]])
C  = np.zeros([2,pt.shape[0]])
N  = np.zeros([2,pt.shape[0]])
O  = np.zeros([2,pt.shape[0]])
Na = np.zeros([2,pt.shape[0]])
Mg = np.zeros([2,pt.shape[0]])
Al = np.zeros([2,pt.shape[0]])
Si = np.zeros([2,pt.shape[0]])
S  = np.zeros([2,pt.shape[0]])
K  = np.zeros([2,pt.shape[0]])
Fe = np.zeros([2,pt.shape[0]])

ch = Chem()
ch.chem(400)
#print ch.sld[0]

for i in range(pt.shape[0]):
    ch.chem(pt[i])
    H[:,i]  = (ch.gas[0]/1e12,ch.sld[0]/1e12)
    He[:,i] = (ch.gas[1]/1e12,ch.sld[1]/1e12)
    Li[:,i] = (ch.gas[2]/1e12,ch.sld[2]/1e12)
    C[:,i]  = (ch.gas[3]/1e12,ch.sld[3]/1e12)
    N[:,i]  = (ch.gas[4]/1e12,ch.sld[4]/1e12)
    O[:,i]  = (ch.gas[5]/1e12,ch.sld[5]/1e12)
    Na[:,i] = (ch.gas[6]/1e12,ch.sld[6]/1e12)
    Mg[:,i] = (ch.gas[7]/1e12,ch.sld[7]/1e12)
    Al[:,i] = (ch.gas[8]/1e12,ch.sld[8]/1e12)
    Si[:,i] = (ch.gas[9]/1e12,ch.sld[9]/1e12)
    S[:,i]  = (ch.gas[10]/1e12,ch.sld[10]/1e12)
    K[:,i]  = (ch.gas[11]/1e12,ch.sld[11]/1e12)
    Fe[:,i] = (ch.gas[12]/1e12,ch.sld[12]/1e12)

print O[0]*1e4,'\n\n',C[0]*1e4
plt.figure()
plt.gca().invert_xaxis()
plt.plot(pt,C[0]/O[0])
#plt.plot(pt,C[0]*1e4)
plt.xscale('log')
plt.show()
