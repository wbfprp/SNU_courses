
import matplotlib.pyplot as plt
import numpy as np
import math

f = open("data.txt", 'r')
dlist = []
timese = []
listline = []

while(True):
    line = f.readline()
    if (line == ""):
        break    
    timese.append(line.split()[0])
    dlist.append(line.split()[1])
f.close()
n = len(timese)
timese = [float (i)/1000 for i in timese]
dlist = [float (i) for i in dlist]
dt = (timese[n-1]-timese[0])/n
fs = 1/dt
te = n*dt

#plt.figure(num=1,dpi=1000,facecolor='white')
#plt.plot(timese,dlist,'r')
#plt.xlim(timese[0], timese[len(timese)-1])
#plt.xlabel('time($sec$)')
#plt.ylabel('Acc(g)')
#plt.savefig("./test_figure1.png",dpi=3000)
#timese.pop(0)
#dlist.pop(0)
#timese.pop(0)
#dlist.pop(0)
NFFT = n
k = np.arange(NFFT)
T = n/fs
freq = k/T
freq = freq[range(int(n/2))]

Y = np.fft.fft(dlist)/n
Y = Y[range(int(n/2))]

fig, ax = plt.subplots(2, 1)
ax[0].plot(timese, dlist)
ax[0].set_xlabel('Time($sec$)')
ax[0].set_ylabel('Acc(g)')
ax[0].grid(True)
#ax[1].plot(freq, abs(Y))
#ax[1].plot(freq, abs(Y), color='c', linestyle = 'solid') 

f = open("config.txt",'r')
while(True):
    line=f.readline()
    if (line == ""):
        break  
    listline.append(line)
xstart=(float)(listline[0].split()[2])
xend=(float)(listline[0].split()[4])
ystart=(float)(listline[1].split()[2])
yend=(float)(listline[1].split()[4])

ax[1].set_xlim([xstart,xend])
ax[1].set_ylim([ystart,yend])
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('AMP')
ax[1].vlines(freq, [0], abs(Y), colors='b')
ax[1].grid(True)
plt.savefig("data.png",dpi=300)
plt.show()

