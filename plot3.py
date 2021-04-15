"""
Created on Fri Feb 14 09:49:16 2020

@author: niloo

This plot, plots the results for the given run
"""

import numpy as np
import matplotlib.pyplot as plt
import variable as var
import matplotlib.pylab as pylab
import matplotlib

#plt.close('all')
params = {'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)
font = {'family' : 'normal',
        'size'   : 18}
#'weight' : 'bold',
matplotlib.rc('font', **font)

name = 26


name_s = 'input/N_Atom.txt'
solar = np.loadtxt(name_s,dtype= str)[0:, 5].astype(float)





doc = 'Output/run_sum'+str(name)+'.txt'

dat = np.loadtxt(doc, dtype = str, skiprows = 1)[0:,1:].astype(float)

test = np.loadtxt(doc, dtype = str, skiprows = 1)[0:,0]
header = np.loadtxt(doc, dtype = str)[0,1:]
print header


def scatter(x,y,z,xlabel = '',ylabel='',clabel = '',title = ''):
    plt.figure()
    plt.scatter(x,y,c=z)
    #,norm=matplotlib.colors.LogNorm())
    plt.xlabel(xlabel, fontsize = 22,fontweight = 'bold')
    plt.ylabel(ylabel, fontsize = 22,fontweight = 'bold')
    plt.title(title)
    plt.colorbar(label = clabel)
    #plt.show()

def plot(x,y,xlabel = '',ylabel='',title = ''):
    plt.figure()
    plt.plot(x,y,'.')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()




#['M_c' 'M_fin' 'a_c' 'a_fin' 'dstg_r' 'pls_r' 'temperature' 'metalicity' 'H' 'He' 'Li'
# 'C' 'N' 'O' 'Na' 'Mg' 'Al' 'Si' 'S' 'K' 'Fe' 'alpha']

#the icelines for alpha = 0.257 are at 3.52 and 25.77
#the icelines for alpha = 0.1 are at 4.4 and 32.27
#[ 0.25681085  0.32614839  0.34128238  0.35780877  0.50062951  0.67447689
# 0.90275687  4.40783142 12.48935045 32.27286169]

i = 2
c1 = np.array([0.81,4.4,10,12,20,25,32.27,35,40])
c2 = np.array([0.1,0.5,1,2,5,10,20,50,100])
c = np.copy(c1)
m0 =np.where((dat[:,i]<=c[0]))
m1 =np.where((dat[:,i]<=c[1])&(dat[:,i]>c[0]))
m2 =np.where((dat[:,i]<=c[2])&(dat[:,i]>c[1]))
m3 =np.where((dat[:,i]<=c[3])&(dat[:,i]>c[2]))
m4 =np.where((dat[:,i]<=c[4])&(dat[:,i]>c[3]))
m5 =np.where((dat[:,i]<=c[5])&(dat[:,i]>c[4]))
m6 =np.where((dat[:,i]<=c[6])&(dat[:,i]>c[5]))
m7 =np.where((dat[:,i]<=c[7])&(dat[:,i]>c[6]))
m8 =np.where((dat[:,i]<=c[8])&(dat[:,i]>c[7]))
m9 =np.where((dat[:,i]>c[8]))

dat0 = np.copy(dat[m0])
dat1 = np.copy(dat[m1])
dat2 = np.copy(dat[m2])
dat3 = np.copy(dat[m3])
dat4 = np.copy(dat[m4])
dat5 = np.copy(dat[m5])
dat6 = np.copy(dat[m6])
dat7 = np.copy(dat[m7])
dat8 = np.copy(dat[m8])
dat9 = np.copy(dat[m9])

co = 6
co2= 3  
g0 =np.where((dat[:,i]<=c1[0]))
g1 =np.where((dat[:,i]<=c1[1])&(dat[:,i]>c1[0]))
g2 =np.where((dat[:,i]<=c1[co2])&(dat[:,i]>c1[1]))
g3 =np.where((dat[:,i]<=c1[co])&(dat[:,i]>c1[co2]))
g4 =np.where((dat[:,i]>c[co]))

datg0 = np.copy(dat[g0])
datg1 = np.copy(dat[g1])
datg2 = np.copy(dat[g2])
datg3 = np.copy(dat[g3])
datg4 = np.copy(dat[g4])

con = 2
clabel = 'Initial orbital distance'
#fname = 'all_r.png'
data = dat
#C: data[:,11]*solar[3]
#S: data[:,18]*solar[10]
scatter(data[:,7],data[:,11]*solar[3]/(data[:,13]*solar[5]),data[:,2],'Metalicity','C/O',clabel)
plt.axhline(y=0.55,color='black')
plt.axvline(x=0.0,color='black')
#scatter(data[:,7],data[:,18]*solar[10]/(data[:,13]*solar[5]),data[:,2],'Metalicity','C/O',clabel)
#scatter(data[:,7],data[:,18]*solar[10]/(data[:,13]*solar[5]),data[:,4],'Metalicity','C/O',clabel)
#scatter(data[:,7],data[:,18]*solar[10]/(data[:,13]*solar[5]),data[:,5],'Metalicity','C/O',clabel)
#plt.savefig(fname,dpi = 1000)
# =============================================================================
# scatter(datg1[:,7],datg1[:,11]*solar[3]/(datg1[:,13]*solar[5]),datg1[:,con],'Metalicity','C/O')
# scatter(datg2[:,7],datg2[:,11]*solar[3]/(datg2[:,13]*solar[5]),datg2[:,con],'Metalicity','C/O')
# scatter(datg3[:,7],datg3[:,11]*solar[3]/(datg3[:,13]*solar[5]),datg3[:,con],'Metalicity','C/O')
# 
# =============================================================================
#plt.show()

#Plot alpha for each region
# =============================================================================
# a0 = (1/(datg0[:,21]*3*0.1**(1.1)))**(1/2.1)*0.1
# a1 = (1/(datg1[:,21]*3*0.1**(1.1)))**(1/2.1)*0.1
# a2 = (1/(datg2[:,21]*3*0.1**(1.1)))**(1/2.1)*0.1
# plt.figure()
# plt.plot(a0,'.')
# 
# plt.figure()
# plt.plot(a1,'.')
# 
# plt.figure()
# plt.plot(a2,'.')
# plt.show()
# =============================================================================

#Plot regions:

plt.figure()
plt.plot(dat[:,13],dat[:,11],'.')
x = np.linspace(*plt.xlim())
plt.plot(x, x)
plt.xlabel('Oxygen to solar', fontsize = 22,fontweight = 'bold')
plt.ylabel('Carbon to solar', fontsize = 22,fontweight = 'bold')
plt.yscale('log')
plt.xscale('log')
plt.axhline(y=1,color='black')
plt.axvline(x=1, color = 'black')
# =============================================================================
# plt.plot(datg4[:,7],datg4[:,11]*solar[3]/((datg4[:,13])*solar[5]),'g.',alpha = 0.75,label = 'Region 4')
# plt.plot(datg3[:,7],datg3[:,11]*solar[3]/((datg3[:,13])*solar[5]),'b.',alpha = 0.75,label = 'Region 3')
# plt.plot(datg2[:,7],datg2[:,11]*solar[3]/((datg2[:,13])*solar[5]),'r.',alpha = 0.75, label ='Region 2')
# plt.plot(datg1[:,7],datg1[:,11]*solar[3]/((datg1[:,13])*solar[5]),'k.', label = 'Region 1')
# plt.plot(datg0[:,7],datg0[:,11]*solar[3]/((datg0[:,13])*solar[5]),'.', color = 'cyan', label = 'Region 0')
# 
# plt.legend()
# plt.xlabel('Metalicity', fontsize = 22,fontweight = 'bold')
# plt.ylabel('C/O', fontsize = 22,fontweight = 'bold')
# =============================================================================
#plt.title(title)
plt.show()


#plot
# =============================================================================
# plt.figure()
# plt.plot(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),'.')
# plt.plot(dat0[:,7],dat0[:,11]*solar[3]/(dat0[:,13]*solar[5]),'.')
# 
# plt.show()
# plt.figure()
# plt.plot(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),'.')
# 
# plt.plot(dat1[:,7],dat1[:,11]*solar[3]/(dat1[:,13]*solar[5]),'.')
# 
# plt.show()
# plt.figure()
# plt.plot(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),'.')
# 
# plt.plot(dat2[:,7],dat2[:,11]*solar[3]/(dat2[:,13]*solar[5]),'.')
# 
# plt.show()
# plt.figure()
# plt.plot(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),'.')
# 
# plt.plot(dat3[:,7],dat3[:,11]*solar[3]/(dat3[:,13]*solar[5]),'.')
# 
# plt.show()
# plt.figure()
# plt.plot(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),'.')
# 
# plt.plot(dat4[:,7],dat4[:,11]*solar[3]/(dat4[:,13]*solar[5]),'.')
# 
# plt.show()
# plt.figure()
# plt.plot(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),'.')
# 
# plt.plot(dat5[:,7],dat5[:,11]*solar[3]/(dat5[:,13]*solar[5]),'.')
# 
# plt.show()
# plt.figure()
# plt.plot(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),'.')
# 
# plt.plot(dat6[:,7],dat6[:,11]*solar[3]/(dat6[:,13]*solar[5]),'.')
# 
# plt.show()
# plt.figure()
# plt.plot(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),'.')
# 
# plt.plot(dat7[:,7],dat7[:,11]*solar[3]/(dat7[:,13]*solar[5]),'.')
# 
# plt.show()
# plt.figure()
# plt.plot(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),'.')
# 
# plt.plot(dat8[:,7],dat8[:,11]*solar[3]/(dat8[:,13]*solar[5]),'.')
# 
# plt.show()
# plt.figure()
# plt.plot(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),'.')
# 
# plt.plot(dat9[:,7],dat9[:,11]*solar[3]/(dat9[:,13]*solar[5]),'.')
# plt.show()
# =============================================================================

#plt.xlabel('Metalicity')
#plt.ylabel('C/O')
#plt.title(title)
#plt.show()
