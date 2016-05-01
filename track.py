import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mpl.rcParams['legend.fontsize'] = 10

df = pd.read_csv('data/tr1_data.csv')
data = df.values

n = 10
# error bars
fig1 = plt.figure()
ax = fig1.gca()
ax.grid(True)
plt.title('Y,Z path projections for first 10 measurements w/ errors')
plt.errorbar(data[:n,1], data[:n,2], xerr=data[:n,4], yerr=data[:n,5], fmt='--o')

fig2, axes = plt.subplots(nrows=1, ncols=2)

axes[0].grid(True)
axes[0].set_xlabel('Y')
axes[0].set_ylabel('Z')
axes[0].set_title('Y,Z projection')
axes[0].plot(data[:,1], data[:,2])

axes[1].grid(True)
axes[1].set_xlabel('X')
axes[1].set_ylabel('Z')
axes[1].set_title('X,Z projection')
axes[1].plot(data[:,0], data[:,2])

fig3 = plt.figure()
ax = fig3.gca(projection='3d')
ax.grid(True)
plt.title('3D path plot')
plt.plot(data[:,0], data[:,1], data[:,2])

fig1.savefig('fig1.png', dpi=100)
fig2.savefig('fig2.png', dpi=100)
fig3.savefig('fig3.png', dpi=100)
