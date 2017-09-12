import numpy as np
import matplotlib.pyplot as plt 

def y(x):
    return (x)+1997

def g(t):
    return 2.5*np.sin(2*np.pi*t)+2015

x = np.arange(0.0,20.0,1.0)
t= np.arange(0.0,5.0,0.1)

plt.figure(1)
plt.subplot(211)
plt.plot(x, y(x), '--',t, g(t), '*r')


def f(m):
    return np.cos(2*np.pi*m)
m = np.arange(0.0, 5.0, 0.02)


plt.plot(m, f(m), 'k')
plt.subplot(212)
plt.plot(m, np.cos(2*np.pi*m), 'r--')
plt.savefig('problema3.png')
plt.show()
