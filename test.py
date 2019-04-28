import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,10,1)
y=np.arange(0,10,1)

X,Y=np.meshgrid(x,y)
#plt.plot(X,Y,'b')
plt.plot(Y,X,'b.')
plt.show()
