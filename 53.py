#Viết chương trình để xóa một phần tử khỏi set

my_set = {'apple', 'banana', 'cherry'}
print("Set ban dau:", my_set)

my_set.remove('banana')
print("Set sau khi xoa 'banana' bang phuong thuc remove():", my_set)

my_set.discard('apple')
print("Set sau khi xoa 'apple' bang phuong thuc discard():", my_set)
