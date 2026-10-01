#Viết chương trình để sắp xếp danh sách theo thứ tự giảm dần

import random

my_list = [1, 3, 46, 26, 13, 20, 77]
print("Danh sach ban dau:",my_list)

random.shuffle(my_list)
print("Danh sach sau khi sao tron:", my_list)

my_list.sort(reverse=True)
print("Danh sach sau khi sap xep giam dan:", my_list)
