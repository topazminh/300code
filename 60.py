#Viết chương trình để chuyển đổi một danh sách thành set

list1 = [1, 2, 3, 4, 5]
print("Danh sach ban dau:", list1)

#Cách 1
set1 = set(list1)
print("Set sau khi chuyen doi tu danh sach:", set)

#Cách 2
set1 = set()
for item in list1:
    set1.add(item)
