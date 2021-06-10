#!/usr/bin/env python3

#https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/

import sys, getopt

import pandas as pd
import numpy as np
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import kendalltau


def main(argv):
   xfile = ''
   yfile = ''
   try:
      opts, args = getopt.getopt(argv,"hx:y:",["xfile=","yfile="])
   except getopt.GetoptError:
      print(argv[0], "-x <xfile> -y <yfile>")
      #print(argv[0])
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print(argv[0], "-x <xfile> -y <yfile>")
         sys.exit()
      elif opt in ("-x", "--xfile"):
         xfile = arg
      elif opt in ("-y", "--yfile"):
         yfile = arg

   print("")
   print("========================")
   print("X file is ", xfile)
   print("Y file is ", yfile)

   #read text file into pandas DataFrame
   #df = pd.read_csv("data.txt", sep=" ", header=None)
   
   xdata = pd.read_csv(xfile, sep=" ", header=None)
   ydata = pd.read_csv(yfile, sep=" ", header=None)

   #print (type(xdata))
   #print (type(ydata))
   #print (xdata)

   # https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-a-list/
   xdatalist = xdata[0].tolist()
   ydatalist = ydata[0].tolist()
   #print (xdatalist)
   #print (ydatalist)

   # ANALYZE
   
   # summarize
   print('xdata: mean=%.3f stdv=%.3f' % (mean(xdata), std(xdata)))
   print('ydata: mean=%.3f stdv=%.3f' % (mean(ydata), std(ydata)))
   
   # plot
   #pyplot.scatter(x, y)
   #pyplot.scatter(xdata, ydata)
   #pyplot.show()
   
   # Pearsons correlation
   # Correlation: https://www.geeksforgeeks.org/exploring-correlation-in-python/
   # Correlation: https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/
   #corr, _ = pearsonr(data1, data2)
   corr, _ = pearsonr(xdatalist, ydatalist)
   print('Pearsons correlation: %.6f' % corr)

   # Spearman correlation
   # https://machinelearningmastery.com/how-to-calculate-nonparametric-rank-correlation-in-python/
   # corr, p = spearmanr(data1, data2)
   corr, p = spearmanr(xdatalist, ydatalist)
   print('Spearman correlation: %.6f' % corr)

   # Kendall correlation
   # https://machinelearningmastery.com/how-to-calculate-nonparametric-rank-correlation-in-python/
   # corr, p = kendalltau(data1, data2)
   corr, p = kendalltau(xdatalist, ydatalist)
   print('Kendall correlation: %.6f' % corr)

   # Covariance
   # https://www.geeksforgeeks.org/python-pandas-series-cov-to-find-covariance/
   xseries = pd.Series(xdatalist)
   yseries = pd.Series(ydatalist)
   covar = xseries.cov(yseries)
   print('Covariance: %6f' % covar)

if __name__ == "__main__":
   main(sys.argv[1:])
