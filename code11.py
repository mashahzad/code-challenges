import statistics
import statsmodels

# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(110)
# generate some integers
for _ in range(1000):
 value = randint(0, 1000)
 print(value)

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
print("Trace - Race_I\n")

#Mean
average = statistics.mean(master_list)
print("Mean is",int(average))

#Variance
variancee = statistics.variance(master_list)
print("variance is",int(variancee))

#autocorrelation
#generate delayed by time 1
master_list_lagby1 = []
for i in range(0,len(master_list)):
    master_list_lagby1.append(int(master_list[i])+1)

autocorr = statistics.correlation(master_list,master_list_lagby1)
# correlation(x, y, /, *, method='linear')
print("Autocorrelation is", autocorr)

#mode
modee = statistics.mode(master_list)
print("Mode is",int(modee))

#median
mediann = statistics.median(master_list)
print("median is",int(mediann))

#Max
maxx = max(master_list)
print("The maximum value is",maxx)

print("\n----\n")
