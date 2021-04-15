import numpy as np
import matplotlib.pyplot as plt
import variable as var
from disk import Disk
from chem import Chem
import matplotlib.pylab as pylab
import matplotlib.axes as ax


from scipy.stats import spearmanr
dsk = Disk()
chm = Chem()
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

pylab.rc('font', **font)
###################################################
###################################################
'''Input folder'''
name = 225

###################################################
name_s = 'input/N_Atom.txt'
solar = np.loadtxt(name_s,dtype= str)[0:, 5].astype(float)

doc = 'Output/run_sum'+str(name)+'.txt'
dat = np.loadtxt(doc, dtype = str, skiprows = 1)[0:,1:].astype(float)

#Plot the data:
plt.figure()
plt.plot(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),'.')
plt.xlabel('Metalicity')
plt.ylabel('C/O')
plt.show()

bins = np.arange(1,100,1)
z = np.zeros([np.shape(bins)[0]-1,3])
for i in range(np.shape(bins)[0]-90):
    g0 = np.where((dat[:,2]<=bins[i+1])&(dat[:,2]>bins[i]))
    data = np.copy(dat[g0])
    x=data[:,7]
    y=data[:,12]*solar[4]/(data[:,13]*solar[5])

    z[i] = np.polyfit(x, y, 3)
    #x0 = np.sort(x)
    #plt.figure()
    #z0 = np.polyval(z,x0)
    #plt.scatter(x,y,color='blue',alpha=0.5)
    #plt.plot(x0,z0,color='black')
    #plt.show()
    #input("continue?")


