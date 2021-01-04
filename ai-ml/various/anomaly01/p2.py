#!/usr/local/bin/python3

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#==============
# MAIN
#==============
#df = pd.read_excel('ex8data1.xlsx', sheet_name='X', header=None)
df = pd.read_csv('ex8dataLabeled.txt', header=None)
df.head()

# This does not work
#plt.figure()
#plt.scatter(df[0], df[1], label=df[2])
#plt.show()

data = pd.DataFrame({"X Value": df[0], "Y Value": df[1], "Category": df[2]})
print(data)

groups = data.groupby("Category")
for name, group in groups:
    plt.plot(group["X Value"], group["Y Value"], marker="o", linestyle="", label=name)

plt.legend()
plt.show()
