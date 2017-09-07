'''
Created on 07 set 2017

@author: davide
'''

'''
    An example implementation of GD 
'''
import numpy as np
import matplotlib.pyplot as plt

omega = 10 # rad/s
x = np.linspace(-1, 1, 200)
y = np.sin(omega*x)*np.exp(-x)
dy = np.diff(y)

plt.figure()
plt.subplot(211)
plt.plot(x, y)
plt.title('Cost/loss function')
plt.subplot(212)
plt.plot(x[0:len(dy)], dy)
plt.title('Derivative of cost/loss wrt x')
plt.show()
