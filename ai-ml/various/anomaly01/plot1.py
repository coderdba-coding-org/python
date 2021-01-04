#!/usr/local/bin/python3

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#==============
# FUNCTIONS
#==============
def probability(df):
    s = np.sum(df, axis=0)
    m = len(df)
    mu = s/m
    vr = np.sum((df - mu)**2, axis=0)
    variance = vr/m
    var_dia = np.diag(variance)
    k = len(mu)
    X = df - mu
    p = 1/((2*np.pi)**(k/2)*(np.linalg.det(var_dia)**0.5))* np.exp(-0.5* np.sum(X @ np.linalg.pinv(var_dia) * X,axis=1))
    return p

# Function to calculate the true positives, false positives, and false negatives:
def tpfpfn(ep, p):
    tp, fp, fn = 0, 0, 0
    for i in range(len(y)):
        if p[i] <= ep and y[i][0] == 1:
            tp += 1
        elif p[i] <= ep and y[i][0] == 0:
            fp += 1
        elif p[i] > ep and y[i][0] == 1:
            fn += 1
    return tp, fp, fn

# Define a function to calculate the ‘f1’ score 
def f1(ep, p):
    tp, fp, fn = tpfpfn(ep, p)
    prec = tp/(tp + fp)
    rec = tp/(tp + fn)
    f1 = 2*prec*rec/(prec + rec)
    return f1

#==============
# MAIN
#==============
#df = pd.read_excel('ex8data1.xlsx', sheet_name='X', header=None)
df = pd.read_csv('ex8data1.txt', header=None)
df.head()

plt.figure()
plt.scatter(df[0], df[1])
#plt.show()

# Check how many training examples are in this dataset:
m = len(df)
print("Sample size:")
print(m)
print()

# Calculate the mean for each feature. Here we have only two features: 0 and 1.
s = np.sum(df, axis=0)
print("Total of each column:")
print(s)
print()

#Mean of column values
mu = s/m
mu

print("Mean of each column:")
print(mu)
print()

#Variance of column values
vr = np.sum((df - mu)**2, axis=0)
variance = vr/m

print("Variance of each column:")
print(variance)
print()

#Now make it diagonal shaped
var_dia = np.diag(variance)
print("Diagonalized variance of each column:")
print(var_dia)
print()

#Calculate the probability:
k = len(mu)
X = df - mu
p = 1/((2*np.pi)**(k/2)*(np.linalg.det(var_dia)**0.5))* np.exp(-0.5* np.sum(X @ np.linalg.pinv(var_dia) * X,axis=1))

print("Probablity of each column:")
print(p)
print()

#Now import the cross-validation data and the labels:
#cvx = pd.read_excel('ex8data1.xlsx', sheet_name='Xval', header=None)
cvx = pd.read_csv('ex8xval.txt', header=None)
cvx.head()

#Here are the labels:
cvy = pd.read_csv('ex8labels.txt', header=None)
cvy.head()

# Now call the probability function we defined before to find the probability for our cross-validation data ‘cvx’:
p1 = probability(cvx)

p1.describe()
print("Probablity of cross validation data:")
print(p1)
print(p1.describe())
print()

# convert ‘cvy’ to a NumPy array just because I like working with arrays
y = np.array(cvy)
print("cvy as numpy array")
print(y)
print()

# Make a list of the probabilities that are lower than or equal to the mean probability
eps = [i for i in p1 if i <= p1.mean()]

print("Probabilities that are lower than or equal to the mean probability")
print(len(eps))

# calculate the f1 score for all the epsilon or the range of probability
f = []
for i in eps:
    f.append(f1(i, p1))

print("The f1 score for all the epsilon or the range of probability")
print("f")
