"""
Created on Fri Feb 14 09:49:16 2020

@author: niloo
This plot, plots the result for a given test from aa given run
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as pylab

plt.close('all')
params = {'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

n = 90934
t = 185165
'''
plt.figure()
for i in range(1,2000):
    doc= 'Output/Run5/test'+str(i)+'.txt'
    data = np.loadtxt(doc, dtype = str, skiprows = 3).astype(float)
    plt.plot(data[:,4][1:]/data[:,5][1:])
plt.show()
    
    
'''
n = 90934
t = 185165
doc = 'Output/Run5/test'+str(t)+'.txt'
doc1 = 'Output/Run6/test'+str(n)+'.txt'

data = np.loadtxt(doc1, dtype = str, skiprows = 3).astype(float)
heda = np.loadtxt(doc1, dtype = str)[0:3]
dat = np.loadtxt(doc, dtype = str, skiprows = 3).astype(float)
hed = np.loadtxt(doc, dtype = str)[0:3]

plt.figure()
#plt.plot(data[:,4][1:],'.')
plt.plot(data[:,5][1:])
plt.yscale('log')
plt.show()

#plt.figure()
#plt.plot(dat[:,4][1:])
#plt.plot(dat[:,5][1:])
#plt.yscale('log')
#plt.show()

#plt.figure()
#plt.plot(dat[:,2][1:])
#plt.plot(data[:,2][1:])
#plt.plot(dat[:,5][1:]*100)
#plt.show()

'''
name = 5
name1 = 4

doc = 'Output/run_sum'+str(name)+'.txt'
doc1 = 'Output/run_sum'+str(name1)+'.txt'
dat = np.loadtxt(doc, dtype = str, skiprows = 1)[0:,1:].astype(float)
data = np.loadtxt(doc1, dtype = str, skiprows = 1)[0:,1:].astype(float)
test = np.loadtxt(doc, dtype = str, skiprows = 1)[0:,0]
header = np.loadtxt(doc, dtype = str)[0,1:]
print header




t1 = np.where((dat[:,3]<=1.2) & (dat[:,3]>=0.8) & (dat[:,2]<=4))

#['M_c' 'M_fin' 'a_c' 'a_fin' 'dstg_r' 'pls_r' 'temperature' 'metalicity'
# 'H' 'He' 'Li' 'C' 'N' 'O' 'Na' 'Mg' 'Al' 'Si' 'S' 'K' 'Fe']
#t3 = np.where((dat123[:,4]>+0.2)&(dat123[:,4]<0.3)&(dat123[:,5]>=0.4));t3
#t2 = np.where((dat12[:,0]<6)&(dat12[:,0]>=5));t2
#t1 = np.where((dat1[:,3]<=1)&(dat1[:,3]>=0.8))
#t = np.where((dat[:,1] ==318)&(dat1[:,3]<=1)&(dat1[:,3]>=0.8)&(dat12[:,0]<6)&(dat12[:,0]>=5)&(dat123[:,4]>+0.2)&(dat123[:,4]<0.3)&(dat123[:,5]>=0.4))

'''























'''
# Fixing random state for reproducibility
np.random.seed(19680801)


N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
area = np.pi * (10 * np.random.rand(N))**2  # 0 to 10 point radii
c = np.sqrt(area)
print area
r = np.sqrt(x * x + y * y)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)
plt.colorbar()
# Show the boundary between the regions:
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))

plt.show()
'''