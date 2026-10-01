#Viết chương trình để đếm số lần xuất hiện của một phần tử trong tuple

my_tuple = (1, 2, 3, 1, 1, 7, 9, 0, 1, 4)
print("Tuple da tao:", my_tuple)
element = input("Nhap phan tu can dem so lan xuat hien: ")

try:
    element = int(element)
except ValueError:
    try:
        element = float(element)
    except ValueError:
        pass

count = my_tuple.count(element)
print(f"Phan tu {element} xuat hien {count} lan trong tuple.")
