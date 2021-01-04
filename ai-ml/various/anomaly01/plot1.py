#!/usr/local/bin/python3

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#df = pd.read_excel('ex8data1.xlsx', sheet_name='X', header=None)
df = pd.read_csv('ex8data1.txt', header=None)
df.head()

plt.figure()
plt.scatter(df[0], df[1])
plt.show()
