import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import glob, os

rows = 5
cols = 8

files = glob.glob("data.grid/*.jpg")[:rows*cols]
files.sort()

fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(40,20))
#fig.tight_layout()

for i in range(1,rows*cols+1):
    plt.subplot(rows, cols, i)
    img = mpimg.imread(files[i-1])
    plt.axis('off')
    plt.subplots_adjust(left=.01, right=.99, top=.99, bottom=.01, hspace=.01, wspace=.01)
    plt.imshow(img)
fig.savefig('out.png', dpi=100)
