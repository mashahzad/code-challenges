import statistics
import statsmodels

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
print("Trace - Race_B\n")

#Mean
average = statistics.mean(master_list2)
print("Mean is",int(average))

#Variance
variancee = statistics.variance(master_list2)
print("variance is",int(variancee))

#autocorrelation
#generate delayed by time 1
master_list_lagby1 = []
for i in range(0,len(master_list2)):
    master_list_lagby1.append(int(master_list2[i])+1)

autocorr = statistics.correlation(master_list2,master_list_lagby1)
# correlation(x, y, /, *, method='linear')
print("Autocorrelation is", autocorr)

#mode
modee = statistics.mode(master_list2)
print("Mode is",int(modee))

#median
mediann = statistics.median(master_list2)
print("median is",int(mediann))

#Max
maxx = max(master_list2)
print("The maximum value is",maxx)

print("\n----\n")

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
print("Trace - Race_IPB\n")

#Mean
average = statistics.mean(master_list3)
print("Mean is",int(average))

#Variance
variancee = statistics.variance(master_list3)
print("variance is",int(variancee))

#autocorrelation
#generate delayed by time 1
master_list_lagby1 = []
for i in range(0,len(master_list3)):
    master_list_lagby1.append(int(master_list3[i])+1)

autocorr = statistics.correlation(master_list3,master_list_lagby1)
# correlation(x, y, /, *, method='linear')
print("Autocorrelation is", autocorr)

#mode
modee = statistics.mode(master_list3)
print("Mode is",int(modee))

#median
mediann = statistics.median(master_list3)
print("median is",int(mediann))

#Max
maxx = max(master_list3)
print("The maximum value is",maxx)

print("\n----\n")

