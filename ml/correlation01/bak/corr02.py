#!/usr/bin/env python3

#https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/

import pandas as pd
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
from scipy.stats import pearsonr

#read text file into pandas DataFrame
#df = pd.read_csv("data.txt", sep=" ", header=None)

dfcsr = pd.read_csv("datacsr3.txt", sep=" ", header=None)
dfdbrt = pd.read_csv("datadbrt3.txt", sep=" ", header=None)

#display DataFrame
print("DF-CSR")
print(dfcsr)

print
print("DF-DBRT")
print(dfdbrt)
print
print

# ANALYZE

# summarize
print('dfcsr: mean=%.3f stdv=%.3f' % (mean(dfcsr), std(dfcsr)))
print('dfdbrt: mean=%.3f stdv=%.3f' % (mean(dfdbrt), std(dfdbrt)))

# plot
#pyplot.scatter(x, y)
#pyplot.scatter(dfdbrt, dfcsr)
pyplot.scatter(dfcsr, dfdbrt)
pyplot.show()

# Pearsons correlation
#corr, _ = pearsonr(data1, data2)
corr, _ = pearsonr(dfcsr, dfdbrt)
print('Pearsons correlation: %.3f' % corr)
