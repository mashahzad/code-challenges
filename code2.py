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

# histogram of Race_I
print("Histogram for Trace - Race_I\n")
plt.title("Histogram for Trace - Race_I")
plt.xlabel("Intervals")
plt.ylabel("Frequency")
plt.hist(master_list, bins=12)
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
print("Histogram for Trace - Race_B\n")
plt.title("Histogram for Trace - Race_B")
plt.xlabel("Intervals")
plt.ylabel("Frequency")
plt.hist(master_list2, bins=15)
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
print("Histogram for Trace - Race_IPB\n")
plt.title("Histogram for Trace - Race_IPB")
plt.xlabel("Intervals")
plt.ylabel("Frequency")
plt.hist(master_list3, bins=10)
plt.show()