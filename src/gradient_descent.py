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
y = np.power(x, 2)
dy = np.diff(y)

plt.figure()
plt.subplot(211)
plt.plot(x, y)
plt.title('Cost/loss function')
plt.subplot(212)
plt.plot(x[0:len(dy)], dy)  
plt.title('Derivative of cost/loss wrt x')
plt.show()

n_iterations = 50000
precision = 1E-4

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
iter_index = 0
previous_cost = 0.0
deltas = []
while True:
    iter_index += 1
    if (iter_index > n_iterations):
        print('n_iterations: ' + str(n_iterations) + ' reached. Stop')
        break

    x_star = x_star - learning_rate*dy[x_star]
    cost = y[x_star]

    delta = np.abs(cost - previous_cost)
    deltas.append(delta)
    if delta < precision:
        print('precision: ' + str(precision) + ' reached. Stop')
        break
    
    if iter_index % 100 == 0:
        print('iter_index: ' + str(iter_index) + ', delta: ' + str(delta))
            
    #ax.plot(x[x_star], y[x_star], 'ro', alpha = (iter_index + 1)/n_iterations)
    ax.plot(x[x_star], y[x_star], 'ro', alpha = (iter_index + 1)/n_iterations, color = scalar_map.to_rgba(iter_index))
    
#color = scalar_map.to_rgba(iter_index)
plt.show()

print(x_star, x[x_star])

plt.figure()
plt.plot(deltas)
plt.title('Delta vs iteration no.')
plt.show()  

print('2 parameters cost/loss function')
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
fig = plt.figure(figsize=(10, 6))
ax = fig.gca(projection='3d')
x, y = np.mgrid[-1:1:0.02, -1:1:0.02]
X, Y, Z = x, y, np.sin(omega*x)*np.exp(-x)*np.cos(omega*y)*np.exp(-y)
ax.plot_surface(X, Y, Z, rstride=2, cstride=2, alpha=0.75, cmap='jet', shade=False)
ax.set_xlabel('Some Parameter 1')
ax.set_ylabel('Some Parameter 2')
ax.set_zlabel('2 parameters cost/loss function')
plt.show()