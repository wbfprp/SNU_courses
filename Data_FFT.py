
import matplotlib.pyplot as plt
import numpy as np
import math
from readcfg import Configuration as Cfg
from readdata import Data

cfg = Cfg()
data = Data()
data._readdata()
cfg._readcfg()

freq = []
rms = 0.0
sqsum = 0.0
n = data.n
dt = (data.time[n-1]-data.time[0])/n
fs = 1/dt
te = n*dt
k = np.arange(n)
T = n/fs
freq = k/T
Y = np.fft.fft(data.dlist)/n
ESD = []
ESD = Y * Y

freq = freq[range(int(n/2))]
Y = Y[range(int(n/2))]
ESD = ESD[range(1,int(n/2))]
np.insert(ESD,0,0)
fig, ax = plt.subplots(2,1)
#Export Summary
for i in range(0, len(data.dlist)):
    sqsum = sqsum +pow((data.dlist[i] - 1),2)
rms = pow(sqsum,0.5)
f = open("summary.csv", 'w')
f.write('rms value,\t')
f.write(str(rms) + '\n')
f.write('Maximum Acc(g),\t')
f.write(str(max(data.dlist)) + '\n')
f.write('ESD max,\t')
f.write(str(max(ESD)) + '\n')
f.write('ESD_max freq,\t')
f.write(str(freq[np.where(ESD == max(ESD))[0]])+'\n')
f.close()
#Draw Acc Plots
ax[0].plot(data.time, data.dlist)
ax[0].set_xlabel('Time($sec$)')
ax[0].set_ylabel('Acc(g)')
ax[0].grid(True)
#Draw FFT 

for i in range(0,int(len(cfg.listline)/4)):
    ax[1].set_xlim([cfg.xstart[i],cfg.xend[i]])
    ax[1].set_ylim([cfg.ystart[i],cfg.yend[i]])
    ax[1].set_xlabel('Freq (Hz)')
    ax[1].set_ylabel('ESD (g^2/Hz)')
    ax[1].vlines(freq, [0], abs(Y), colors='b')
    ax[1].grid(True)    
    plt.savefig("Acc_FFT_data" + str(i) + ".png", dpi=300)
    ax[1].cla()
#Draw ESD Plots
for i in range(int(len(cfg.listline)/4),int(len(cfg.listline)/2)):
    ax[1].set_xlim([cfg.xstart[i],cfg.xend[i]])
    ax[1].set_ylim([cfg.ystart[i],cfg.yend[i]])
    ax[1].set_xlabel('Freq (Hz)')
    ax[1].set_ylabel('ESD g^2')    
    ax[1].vlines(freq, [0], abs(ESD), colors='b')
    ax[1].grid(True)    
    plt.savefig("ESD_data" + str(i) + ".png", dpi=300)
    ax[1].cla()
