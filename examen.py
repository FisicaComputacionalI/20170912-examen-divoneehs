import numpy as np
import matplotlib.pyplot as plt
def y(x):
	return (x) + 1997
x= np.arange(0.0,20.0,1.0)
plt.plot(x, y(x),'*g')
plt.title("Diana Ivonee Huitzil Sosa")
plt.xlabel("Edad")
plt.ylabel("Anio")
plt.savefig('edadIvonee.png')
plt.show ()
