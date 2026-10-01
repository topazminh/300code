#Viết chương trình để tính tổng các phần tử trong danh sách

import random

my_list = [random.randint(1, 100) for _ in range(10)]
print("Danh sach ban dau:", my_list)

total_sum = sum(my_list)
print("Tong cac phan tu trong danh sach la:", total_sum)
