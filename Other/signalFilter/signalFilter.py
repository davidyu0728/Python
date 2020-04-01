#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 0021 14:54
# @Author  : Muzi Shen
# @File    : signalFilter.py
from math import pi

import numpy as np
import numpy.matlib
import scipy.io as sio
import matplotlib.pyplot as plt
from scipy import signal

IFreq = 110e6
sampleRate = 1.8e9
sampleCount = 2048
repeatCount = 5000
activeCount = 1980
dataFile = 'once_data.mat'

data = sio.loadmat(dataFile)
data0 = data['data0']
data1 = data['data1']
[repeat, Len] = data0.shape
t = [i / sampleRate for i in range(1, activeCount + 1)]
Seff0 = data0[:, 0:activeCount]
Seff1 = data1[:, 0:activeCount]
S_std = np.exp((0 - 1j) * 2 * pi * IFreq * np.array(t))
S_std = np.matlib.repmat(S_std, repeat, 1)
S1 = S_std * Seff1
S0 = S_std * Seff0
I1 = np.real(S1).T
Q1 = np.imag(S1).T
I0 = np.real(S0).T
Q0 = np.imag(S0).T
p = I1[:,1]
plt.plot(p)
plt.show()
"""
for i in range(5000):
    I1_tr_tmp = I1[:, 1]
    Q1_tr_tmp = Q1[:, 1]
    I0_tr_tmp = I0[:, 1]
    Q0_tr_tmp = Q0[:, 1]
    fig1 = plt.figure('fig1')
    # plt.plot(I0_tr_tmp, Q0_tr_tmp)
    # print(I1_tr_tmp.shape)
# fig1.show()
# 滤波
# X = np.column_stack((I1,Q1))
b, a = signal.butter(5, 0.2, 'lowpass')
dataI = np.log(np.abs(signal.hilbert(I1)))
dataQ = np.log(np.abs(signal.hilbert(Q1)))
filtedDataI = signal.filtfilt(b, a, dataI)
filtedDataQ = signal.filtfilt(b, a, dataQ)
print(filtedDataI.shape)
for i in range(5000):
     I1_tr_tmp = filtedDataI[:,1]
     Q1_tr_tmp = filtedDataI[:,1]
     # I0_tr_tmp = filtedDataI[:,1]
     # Q0_tr_tmp = filtedDataI[:,1]
     fig1 = plt.figure('fig1')
     plt.plot(Q1_tr_tmp)

fig1.show()
"""