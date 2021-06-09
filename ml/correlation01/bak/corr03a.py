#!/usr/bin/env python3

#https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/

import sys, getopt

import pandas as pd
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
from scipy.stats import pearsonr


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
   print("X file is ", xfile)
   print("Y file is ", yfile)

   #read text file into pandas DataFrame
   #df = pd.read_csv("data.txt", sep=" ", header=None)
   
   xdata = pd.read_csv(xfile, sep=" ", header=None)
   ydata = pd.read_csv(yfile, sep=" ", header=None)
   
   #display DataFrame
   print
   print
   print("X DATA")
   print(xdata)

   print
   print
   print("Y DATA")
   print(ydata)
   print
   print
   
   # ANALYZE
   
   # summarize
   print('xdata: mean=%.3f stdv=%.3f' % (mean(xdata), std(xdata)))
   print('ydata: mean=%.3f stdv=%.3f' % (mean(ydata), std(ydata)))
   
   # plot
   #pyplot.scatter(x, y)
   #pyplot.scatter(ydata, xdata)
   pyplot.scatter(xdata, ydata)
   pyplot.show()
   
   # Pearsons correlation
   #corr, _ = pearsonr(data1, data2)
   #corr, _ = pearsonr(xdata, ydata)
   #print('Pearsons correlation: %.3f' % corr)

if __name__ == "__main__":
   main(sys.argv[1:])
