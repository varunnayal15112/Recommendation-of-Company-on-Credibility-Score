# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:33:27 2018

@author: vicky
"""

import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
#import pandas.io.data as web
from pandas_datareader import data

style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)
df = data.DataReader("XOM", "yahoo", start, end)
print(df)
print(df.head())

plt.plot(df['High'],'g',linewidth=5)
plt.plot(df['Low'],'r')

plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()