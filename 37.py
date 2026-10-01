#Viết chương trình để kiểm tra một phần tử có tồn tại trong tuple khong

my_tuple = (5, 10, 15, 20, 25)
print("Tuple da tao:", my_tuple)
element = input("Nhap phan tu can kiem tra: ")

try:
    element = int(element)
except ValueError:
    try:
        element = float(element)
    except ValueError:
        pass

if element in my_tuple:
    print(f"Phan tu {element} ton tai trong tuple.")
else:
    print(f"Phan tu {element} khong ton tai trong tuple.")