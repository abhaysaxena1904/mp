"""# creating 3d bar plot using matplotlib
# in python

# to interacte with plot
# %matplotlib widget

# importing required libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# creating random dataset
xs = [2, 3, 4, 5, 1, 6, 2, 1, 7, 2]
ys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
zs = np.zeros(10)
dx = np.ones(10)
dy = np.ones(10)
dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# creating figure
figg = plt.figure()
ax = figg.add_subplot(111, projection='3d')

# creating the plot
plot_geeks = ax.bar3d(xs, ys, zs, dx,
					dy, dz, color='green')

# setting title and labels
ax.set_title("3D bar plot")
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')

# displaying the plot
plt.show()
"""
"""
# Suppress matplotlib user warnings
# Necessary for newer version of matplotlib
import warnings
warnings.filterwarnings("ignore", category = UserWarning, module = "matplotlib")
#
# Display inline matplotlib plots with IPython
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')
"""
%matplotlib.qt

from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d')

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
fig = plt.figure(figsize=(9, 6))
ax = plt.axes(projection='3d')

import numpy as np
np.random.seed(3)
y = np.random.random(100)
x = np.random.random(100)
z = np.random.random(100)
ax.scatter3D(x, y, z, color='red')
ax.set_title("3D scatterplot", pad=25, size=15)
ax.set_xlabel("X") 
ax.set_ylabel("Y") 
ax.set_zlabel("Z")