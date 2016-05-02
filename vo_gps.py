import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mpl.rcParams['legend.fontsize'] = 10

df_vo = pd.read_csv('data/vo_data.csv')
df_gt = pd.read_csv('data/gt_data.csv')

data_vo = df_vo.values
data_gt = df_gt.values

fig = plt.figure()
ax = fig.gca()
ax.grid(True)
ax.set_xlabel('Y m')
ax.set_ylabel('Z m')
ax.set_title('Y,Z projection')
plt.plot(data_vo[:,1], data_vo[:,2], label='VO')
plt.plot(data_gt[:,1], data_gt[:,2], label='GT')
plt.legend()
fig.savefig('fig4.png', dpi=100)

dt = data_vo-data_gt
dists = np.linalg.norm(data_gt, axis=1)
norms = np.linalg.norm(dt, axis=1)

fig2 = plt.figure()
ax = fig2.gca()
ax.grid(True)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Error % of travelled distance')
ax.set_title('VO Error')

plt.plot(range(dt.shape[0]), norms/dists)

fig2.savefig('fig6.png', dpi=100)

