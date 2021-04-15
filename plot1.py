"""
Created on Fri Feb 14 09:49:16 2020

@author: niloo
This plot, compares the result for different runs
"""
import numpy as np
import matplotlib.pyplot as plt
import variable as var
import matplotlib.pylab as pylab

#plt.close('all')
params = {'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

name = 25
name1 = 26
name2 = 9
name3 = 10


name_s = 'input/N_Atom.txt'
solar = np.loadtxt(name_s,dtype= str)[0:, 5].astype(float)





doc = 'Output/run_sum'+str(name)+'.txt'
doc1 = 'Output/run_sum'+str(name1)+'.txt'
doc2 = 'Output/run_sum'+str(name2)+'.txt'
doc3 = 'Output/run_sum'+str(name3)+'.txt'

dat = np.loadtxt(doc, dtype = str, skiprows = 1)[0:,1:].astype(float)
dat1 = np.loadtxt(doc1, dtype = str, skiprows = 1)[0:,1:].astype(float)
#dat2 = np.loadtxt(doc2, dtype = str, skiprows = 1)[0:,1:].astype(float)
#dat3 = np.loadtxt(doc3, dtype = str, skiprows = 1)[0:,1:].astype(float)

test = np.loadtxt(doc, dtype = str, skiprows = 1)[0:,0]
header = np.loadtxt(doc, dtype = str)[0,1:]
print header
#print dat[:,6]


def scatter(x,y,z,xlabel = '',ylabel='',title = ''):
    plt.figure()
    plt.scatter(x,y,c=z)
    #,norm=matplotlib.colors.LogNorm())
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.colorbar()
    plt.show()

def plot(x,y,xlabel = '',ylabel='',title = ''):
    plt.figure()
    plt.plot(x,y,'.')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

t = np.where((dat[:,21]>=0.1))
dat = dat[t]

#area = dat[:,2]**2*dat[:,5]
#t1 = np.where((dat1[:,1]<=1.1*var.M_f/var.M_earth) & (dat1[:,1]>=0.9*var.M_f/var.M_earth))
#t2= np.where((dat2[:,1]<=1.1*var.M_f/var.M_earth) & (dat2[:,1]>=0.9*var.M_f/var.M_earth))
#t3= np.where((dat3[:,1]<=1.1*var.M_f/var.M_earth) & (dat3[:,1]>=0.9*var.M_f/var.M_earth))
#print t
#dat1 = dat1[t1]
#dat2 = dat2[t2]
#dat3 = dat3[t3]

#m1 = np.where((dat1[:,3]<=1.2) & (dat1[:,3]>=0.8))
#m2 = np.where((dat2[:,3]<=1.2) & (dat2[:,3]>=0.8))
#m3 = np.where((dat3[:,3]<=1.2) & (dat3[:,3]>=0.8))

#datm1 = dat1[m1]
#datm2 = dat2[m2]
#datm3 = dat3[m3]

#plt.figure()

#plt.plot(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),'.')
plt.figure()

plt.plot(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),'.')
plt.plot(dat1[:,7],dat1[:,11]*solar[3]/(dat1[:,13]*solar[5]),'.')
plt.show()
#plt.plot(datm3[:,7],datm3[:,11]*solar[3]/(datm3[:,13]*solar[5]),'.')
#
#plt.xlabel('Metalicity')
#plt.ylabel('C/O')
#plt.title(title)
#plt.show()

con = 2
#plt.figure()
#scatter(dat[:,7],dat[:,11]*solar[3]/(dat[:,13]*solar[5]),(dat[:,con]),'Metalicity','C/O')

#['M_c' 'M_fin' 'a_c' 'a_fin' 'dstg_r' 'pls_r' 'metalicity' 'H' 'He' 'Li'
# 'C' 'N' 'O' 'Na' 'Mg' 'Al' 'Si' 'S' 'K' 'Fe']

#plt.figure()
#plt.plot(dat[:,2],dat[:,7],'.')
#plt.show()
'''  
plt.figure()
bars = ('metal','H', 'He', 'Li', 'C', 'N', 'O', 'Na', 'Mg', 'Al', 'si', 'S', 'K', 'Fe')
y_pos = np.arange(len(bars))
for i in range(2000):
    plt.plot(y_pos,dat[i,6:])
#plt.colorbar()
plt.show()
'''
