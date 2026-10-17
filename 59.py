#Viết chương trình để xóa tất cả các phần tử trong set

set = {1, 2, 3, 4, 5}
print("Set ban dau:", set)

#Cách 1
set.clear()
print("Set sau khi xoa tat ca cac phan tu:", set)

#Cách 2
for item in list(set):
    set.remove(item)
