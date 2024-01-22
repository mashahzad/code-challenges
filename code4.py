# code 
import scipy.stats as stats 
import matplotlib.pyplot as plt 
import statsmodels.api as sm 

#Trace_I
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
master_list.sort()

print("\n---Trace_I-----\n")

#q-q plot
stats.probplot(master_list, dist="norm", plot=plt) 
plt.title("Normal Q-Q plot") 
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show() 

#Trace_B
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
master_list2.append(61832)   
master_list2.remove([])
master_list2.sort()

print("\n---Trace_B-----\n")

#q-q plot
stats.probplot(master_list2, dist="norm", plot=plt) 
plt.title("Normal Q-Q plot") 
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show() 

#Trace_IPB
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
master_list3.append(61832)   
master_list3.remove([])
master_list3.sort()

print("\n---Trace_IPB-----\n")

#q-q plot
stats.probplot(master_list3, dist="norm", plot=plt) 
plt.title("Normal Q-Q plot") 
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show() 