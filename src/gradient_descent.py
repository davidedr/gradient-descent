'''
Created on 07 set 2017

@author: davide
'''

'''
    An example implementation of GD 
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

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

n_iterations = 500

cmap = plt.get_cmap('coolwarm')
cmap_norm = colors.Normalize(vmin = 0, vmax = n_iterations)
scalar_map = cmx.ScalarMappable(norm = cmap_norm, cmap = cmap)

learning_rate = 1.0

fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)

x_0 = 120
x_0 = np.random.randint(len(x)*0.2, len(x)*0.8)
x_star = x_0 # Optimal value of parameter
for iter_index in range(n_iterations):
    x_star = x_star - learning_rate*dy[x_star]
    ax.plot(x[x_star], y[x_star], 'ro', alpha = (iter_index + 1)/n_iterations, color=scalar_map.to_rgba(iter_index))
color = scalar_map.to_rgba(iter_index)
plt.show()

print(x_star, x[x_star])  
