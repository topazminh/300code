#Viết chương trình để kiểm tra một phần tử có tồn tại trong set khong

my_set = {'apple', 'banana', 'cherry'}
print("Set ban dau:", my_set)

element = 'banana'
if element in my_set:
    print(f"Phan tu '{element}' ton tai trong set.")
else:
    print(f"Phan tu '{element}' khong ton tai trong set.")

