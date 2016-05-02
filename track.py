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
axes[0].set_xlabel('Y [m]')
axes[0].set_ylabel('Z [m]')
axes[0].set_title('Y,Z projection')
axes[0].plot(data[:,1], data[:,2])

axes[1].grid(True)
axes[1].set_xlabel('X [m]')
axes[1].set_ylabel('Z [m]')
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

df_dt = df - df.shift()
data_dt = df_dt.values[1:,0:3]
norms = np.linalg.norm(data_dt, axis=1)

fig3, axes = plt.subplots(nrows=2, ncols=1)

axes[0].grid(True)
axes[0].set_xlabel('Time [s]')
axes[0].set_ylabel('Distance [m/s]')
axes[0].set_title('Distance per step')
axes[0].plot(range(len(norms)), norms)

axes[1].grid(True)
axes[1].set_xlabel('Time [s]')
axes[1].set_ylabel('Distance [m]')
axes[1].set_title('Cumulative distance')
axes[1].plot(range(len(norms)), np.cumsum(norms))

fig3.savefig('fig5.png', dpi=100)

print('track length:', np.sum(norms))
print('average speed:', np.sum(norms)/len(df))
