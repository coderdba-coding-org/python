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

   #print (type(xdata))
   #print (type(ydata))
   #print (xdata)

   # https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-a-list/
   xdata = xdata[0].tolist()
   ydata = ydata[0].tolist()

   # ANALYZE
   
   # summarize
   print('xdata: mean=%.3f stdv=%.3f' % (mean(xdata), std(xdata)))
   print('ydata: mean=%.3f stdv=%.3f' % (mean(ydata), std(ydata)))
   
   # plot
   #pyplot.scatter(x, y)
   pyplot.scatter(xdata, ydata)
   pyplot.show()
   
   # Pearsons correlation
   #corr, _ = pearsonr(data1, data2)
   corr, _ = pearsonr(xdata, ydata)
   print('Pearsons correlation: %.3f' % corr)

if __name__ == "__main__":
   main(sys.argv[1:])
