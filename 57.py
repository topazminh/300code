#Viết chương trình để tìm giao của hai set

set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'cherry', 'durian'}
print("Set 1:", set1)
print("Set 2:", set2)

#Cách 1
set_intersection1 = set1 & set2
print("Giao cua hai set cach 1:", set_intersection1)

#Cách 2
set_intersection2 = set1.intersection(set2)
print("Giao cua hai set cach 2:", set_intersection2)
