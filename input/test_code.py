#def chm_HT():
mname = 'input/Molec.atm'
dat = np.loadtxt(mname,dtype= str)
ab = dat[11,1:-1].astype(float)
ab_cp = np.copy (ab)
dat_cp = np.copy(dat)
dat_T = dat[1:-1,-1].astype(float)
ab_t = np.zeros_like(dat_T)
print ab_cp
set1 = np.array([8,3,5,7,9,6,1,2])
#set1 = np.array([8,3])
r = np.array([1.,1.,0.5,0.5,0.17,1,0.83,1.,1.,1.])
for i in set1:
    print i, '\t','The molecule is:', dat[0,i] 
    
    atm_info = dat_cp[1:-1,i].astype(float)
    j = np.nonzero(atm_info)[0]


    N_list = np.zeros_like(dat_cp[j[0]+1,1:-1].astype(float))
    M_r = np.zeros_like(j)
    count = 0
    for j1 in j:
        M_r[count] = dat_cp[j1+1,i].astype(float)
        N_list = N_list +dat_cp[j1+1,1:-1].astype(float)*r[j1]
        count += 1
    ab_r = ab_cp[i-1]*N_list/N_list[i-1]
    #print 'This is ab_r', ab_r
    dat_cp_tmp = np.copy(dat_cp)
    dat_cp_tmp[j+1,1:] = 0
    ab_cp_tmp = (ab_cp - ab_r)
    
    ab_t[j] = ab_cp[i-1]*r[j]/M_r
    
    
    tst = dat_cp_tmp[1:-1,1:-1]
    chk = np.sum(dat_cp_tmp[1:-1,1:-1].astype(float),axis = 0)
    k = np.where(chk == 0)[0]

    if chk[k].any() != ab_cp_tmp[k].any():
        print 'False'
        #, ab_cp_tmp[k]

    ab_cp = np.copy(ab_cp_tmp)
    dat_cp = np.copy(dat_cp_tmp)
    print ab_cp
    
print 'THis is molecule abundance:\n', ab_t,'\n'
dat1 = dat[1:-1,1:].astype(float)
dt_tst = np.copy(dat1)
for i in range(10):
    dat1[i,:-1]= dat1[i,:-1]*ab_t[i]
print dat1    













##//////////////////////////////////////////////////////////
### Other part
##/////////////////////////////////////////////////////////


#def chm_HT():
mname = 'input/Molec.atm'
dat = np.loadtxt(mname,dtype= str)
ab = dat[11,1:-1].astype(float)
ab_cp = np.copy (ab)
dat_cp = np.copy(dat)
dat_T = dat[1:-1,-1].astype(float)
ab_t = np.zeros_like(dat_T)
print ab_cp
set1 = np.array([8,3,5,7,9,6,1,2])
#set1 = np.array([8,3])
r = np.array([1.,1.,0.5,0.5,0.25,1,0.75,1.,1.,1.])
for i in set1:
    print i, '\t','The molecule is:', dat[0,i] 
    
    atm_info = dat_cp[1:-1,i].astype(float)
    j = np.nonzero(atm_info)[0]


    N_list = np.zeros_like(dat_cp[j[0]+1,1:-1].astype(float))
    M_r = np.zeros_like(j)
    count = 0
    for j1 in j:
        M_r[count] = dat_cp[j1+1,i].astype(float)
        N_list = N_list +dat_cp[j1+1,1:-1].astype(float)*r[j1]
        count += 1
    ab_r = ab_cp[i-1]*N_list/N_list[i-1]
    #print 'This is ab_r', ab_r
    dat_cp_tmp = np.copy(dat_cp)
    dat_cp_tmp[j+1,1:] = 0
    ab_cp_tmp = (ab_cp - ab_r)
    
    ab_t[j] = ab_cp[i-1]*r[j]/M_r
    
    
    tst = dat_cp_tmp[1:-1,1:-1]
    chk = np.sum(dat_cp_tmp[1:-1,1:-1].astype(float),axis = 0)
    k = np.where(chk == 0)[0]

    if chk[k].any() != ab_cp_tmp[k].any():
        print 'False'
        #, ab_cp_tmp[k]

    ab_cp = np.copy(ab_cp_tmp)
    dat_cp = np.copy(dat_cp_tmp)
    #print ab_cp
    
print 'THis is molecule abundance:\n', ab_t,'\n'
dat1 = dat[1:-1,1:].astype(float)
dt_tst = np.copy(dat1)
for i in range(10):
    dat1[i,:-1]= dat1[i,:-1]*ab_t[i]
print dat1 






 

##////////////////////////////////////////////////
##Molec.atm
##///////////////////////////////////////////////

Condensates	C	O	Na	Mg	Al	Si	S	K	Fe	T_s
[CO		1	1	0	0	0	0	0	0	0	2000]

[H2O		0	1	0	0	0	0	0	0	0	2000]

[Al2O3 		0	3	0	0	2	0	0	0	0	1550]

[MgAl2O4	0	4	0	1	2	0	0	0	0	1250]

[Mg2SiO4	0	4	0	2	0	1	0	0	0	1200]

[Fe		0	0	0	0	0	0	0	0	1	1200]

[MgSiO3		0	3	0	1	0	1	0	0	0	1150]

[KALSi3O8	0	8	0	0	1	3	0	1	0	850]

[NaAlSi3O8	0	8	1	0	1	3	0	0	0	850]

[FeS		0	0	0	0	0	0	1	0	1	650]

[abundance 	7.19e6	1.57e7	5.7e4	1.03e6	8.27e4	1e6	4.38e5	3.65e3	8.7e5	0]


# Atom name	abundace(CI)	Abundance(Solar)	Mass (AMU)
01	H	5.13e6 (8.22)	2.93e10	(12)		1.0079
02	He	0.601  (1.29)	2.47e9	(10.93)		4.0026
03	Li	55.6   (1.05)	55.6	(3.26)		6.941
06	C	7.60e5 (8.43)	7.19e6	(7.39)		12.0107
07	N	5.53e4 (7.83)	2.12e6	(6.26)		14.0067
08	O	7.63e6 (8.43)	1.57e7	(8.40)		15.9994
11	Na	5.7e4  (6.24)	5.77e4	(6.27)		22.9897
12	Mg	1.03e6 (7.60)	1.03e6	(7.53)		24.305
13	Al	8.27e4 (6.45)	8.46e4	(6.43)		26.9815
14	Si	1e6    (7.51)	1e6     (7.51)		28.0855
16	S	4.38e5 (7.12)	4.38e5	(7.15)		32.065
19	K	3.65e3 (5.03)	3.76e3	(5.08)		39.0983
26	Fe	8.7e5  (7.50)	8.7e5	(7.45)		55.845
