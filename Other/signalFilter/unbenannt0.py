# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:41:39 2019

@author: david
"""

import scipy.io as scio
import numpy as np
import numpy.matlib
from math import pi
from matplotlib import pyplot as plt 

IFreq = 110e6
sampleRate = 1.8e9
sampleCount = 2048
repeatCount = 5000
activeCount=1980

dataFile = 'once_data.mat'
data = scio.loadmat(dataFile)
data0 = data['data0']
data1 = data['data1']
[repeat,Len] = data0.shape
t = [i/sampleRate for i in range(1,activeCount+1)]
Seff0=data0[:,0:activeCount]
Seff1=data1[:,0:activeCount]
S_std=np.exp((0-1j)*2*pi*IFreq*np.array(t))
S_std=np.matlib.repmat(S_std,repeat,1)
S1=S_std*Seff1
S0=S_std*Seff0
I1=np.real(S1).T
Q1=np.imag(S1).T
I0=np.real(S0).T
Q0=np.imag(S0).T
span = 180
slider = 10
seg = int((activeCount-span)/10+1)
I1_tr = np.zeros((seg,5000))
Q1_tr = np.zeros((seg,5000))
I0_tr = np.zeros((seg,5000))
Q0_tr = np.zeros((seg,5000))
for j in range(0, activeCount-span+1, slider):
    I1_tr[int(np.fix((j+10)/10))-1] = np.mean(I1[j:j+span],axis=0)
    Q1_tr[int(np.fix((j+10)/10))-1] = -np.mean(Q1[j:j+span],axis=0)
    I0_tr[int(np.fix((j+10)/10))-1] = np.mean(I0[j:j+span],axis=0)
    Q0_tr[int(np.fix((j+10)/10))-1] = -np.mean(Q0[j:j+span],axis=0)
for i in range(5000):
    I1_tr_tmp = I1_tr[:,2]
    Q1_tr_tmp = Q1_tr[:,2]
    I0_tr_tmp = I0_tr[:,2]
    Q0_tr_tmp = Q0_tr[:,2]
    plt.plot(I0_tr_tmp,Q0_tr_tmp,'b*-',I1_tr_tmp.T,Q1_tr_tmp.T,'r*-')
plt.show()
plt.savefig("1.pdf",format="pdf")
"""
I1_tr_avg = np.mean(I1_tr.T,axis=0)
Q1_tr_avg = -np.mean(Q1_tr.T,axis=0)
I0_tr_avg = np.mean(I0_tr.T,axis=0)
Q0_tr_avg = -np.mean(Q0_tr.T,axis=0)

plt.figure
plt.grid()
plt.plot(I0_tr_avg.T,Q0_tr_avg.T,'r*-',I1_tr_avg.T,Q1_tr_avg.T,'b*-')
plt.plot(I0_tr_avg[0],Q0_tr_avg[0],marker = ".",markersize = 30,color='r')
plt.plot(I1_tr_avg[0],Q1_tr_avg[0],marker = ".",markersize = 30,color='b')
plt.show()
"""