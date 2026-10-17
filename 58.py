#Viết chương trình để tìm phần bù của hai set

set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'cherry', 'durian'}
print("Set 1:", set1)
print("Set 2:", set2)

#Cách 1
set_difference1 = set1 - set2
print("Phan bu cua hai set cach 1:", set_difference1)

#Cách 2
set_difference2 = set1.difference(set2)
print("Phan bu cua hai set cach 2:", set_difference2)
