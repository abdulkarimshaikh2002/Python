# calculating mean
list1 = [22,23,45,66,77,34,23]
mean = sum(list1)/len(list1)
print(mean)

#calculating median
list2 = [22,23,45,66,77,34,23]
list2.sort()
if len(list2) % 2 == 0:
    m1 = list2[len(list2)// 2]
    m2 = list2[len(list2)//2]
    median = (m1 + m2)/2
else:
    median = list1 [len(list2)//2]

print(median)

#calculate mode

list3 = [22,23,45,66,77,34,23]
frequency = {}

for i in list3:
    frequency.setdefault(i,0)
    frequency[i] +=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(mode)