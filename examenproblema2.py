import numpy as np
import matplotlib.pyplot as plt 

def y(x):
    return 2.5*np.sin(2*np.pi*x)+2015

x = np.arange(0.0, 5.0, 0.1)

plt.plot(x, y(x), 'r--')
plt.savefig('funciontrigonometrica.png')
plt.show()
