if self.r_min>self.r_ice and (self.r - self.rh)<self.r_ice:
            self.dm_g = np.append(self.dm_g,self.gas_acc())
            
            
            if self.dr == 0:
                self.d_mig = 0
                pass
            else:
                r_min = self.r_ice
            
                self.d_mig =(self.r_min**2 - r_min**2) * np.pi
                self.r_min = r_min
                
            self.dm_d = np.append(self.dm_d,self.solid_acc())
            
            $abn1 = self.ch.mas_abnd([self.dm_g[-1]*self.dt,self.dm_d[-1]],self.disk.T)
            
            self.migration()
            self.disk.evolve(self.r_min)
            dm_t = self.solid_acc()
            self.dm_d[-1] += dm_t
            $abn2 = self.ch.mas_abnd([0,dm_t],self.disk.T)
            self.abn = np.add(abn1,abn2)
            	
        
        else:
            self.migration()
            self.dm_g = np.append(self.dm_g,self.gas_acc())
            self.dm_d = np.append(self.dm_d,self.solid_acc())
            $self.abn = self.ch.mas_abnd([self.dm_g[-1]*self.dt,self.dm_d[-1]],self.disk.T)
	    
        self.abn_t += self.abn
        self.M += (self.dm_g[-1]*self.dt+self.dm_d[-1])
