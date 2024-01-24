import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import numpy as np
import matplotlib.pyplot as plt

# race_I
with open('race_I.txt', 'r') as f:
    data = f.readlines()
    master_list = []
    lst = []
    for i in data:
        if '\n' in i:
            master_list.append(lst)
            lst = int(i)
        else:
            lst.append(i.replace('\n', ''))
master_list.append(61832)   
master_list.remove([])
print("\nThe autocorrelation function for the given trace - Trace I\n")     
master_list = np.array(master_list)
plt.figure(figsize=(10,5))
plt.plot(master_list)
plot_acf(master_list,lags = 90)
plt.show()

#   race_B
with open('race_B.txt', 'r') as f:
    data = f.readlines()
    master_list2 = []
    lst = []
    for i in data:
        if '\n' in i:
            master_list2.append(lst)
            lst = int(i)
        else:
            lst.append(i.replace('\n', ''))
master_list2.append(13144)   
master_list2.remove([])
print("\nThe autocorrelation function for the given trace - Trace B\n")
master_list2 = np.array(master_list2)
plt.figure(figsize=(10,5))
plt.plot(master_list2)
plot_acf(master_list2,lags = 90)
plt.show()         

#   race_IPB
with open('race_IPB.txt', 'r') as f:
    data = f.readlines()
    master_list3 = []
    lst = []
    for i in data:
        if '\n' in i:
            master_list3.append(lst)
            lst = int(i)
        else:
            lst.append(i.replace('\n', ''))
master_list3.append(13144)   
master_list3.remove([])
print("\nThe autocorrelation function for the given trace - Trace IPB\n")
master_list3 = np.array(master_list3)
plt.figure(figsize=(10,5))
plt.plot(master_list3)
plot_acf(master_list3,lags = 90)
plt.show()         