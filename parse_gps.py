from __future__ import print_function
import sys
import pandas as pd
import numpy as np
import csv

def process(seq):
    df = pd.read_csv('%s.pos' % seq, comment='%', delim_whitespace=True, header=0)
    dt = pd.to_datetime(df.GPST_time, format='%H:%M:%S.%f')
    delta = dt-dt.shift()
    delta = delta.apply(lambda x: x/np.timedelta64(1, 's'))
    udelta = np.round(np.array(delta)).astype('uint8')
    udelta[0] = 1

    valid = []
    for i in udelta: valid.extend([0]*(i-1)+[1])

    with open('out/%s_valid.csv' % seq,'w+') as fd:
        wr = csv.writer(fd)
        wr.writerow(valid)

    df1 = df.ix[:,[2,3,4]]
    df2 = df.ix[:,[7,8,9,10]]

    values = df1.values - df1.values[0,:]

    df3 = pd.DataFrame(data=values, index=df1.index, columns=df1.columns)
    df4 = pd.concat([df3,df2], axis=1, join_axes=[df3.index])
    
    df4.to_csv('out/%s.csv' % seq, index=False)
    return df4

if __name__ == '__main__':
    for seq in sys.argv[1:]:
        print('processing ', seq)
        process(seq)
