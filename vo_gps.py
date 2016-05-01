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
ax.set_xlabel('Y')
ax.set_ylabel('Z')
ax.set_title('Y,Z projection')
plt.plot(data_vo[:,1], data_vo[:,2], label='VO')
plt.plot(data_gt[:,1], data_gt[:,2], label='GT')
plt.legend()
fig.savefig('fig4.png', dpi=100)
