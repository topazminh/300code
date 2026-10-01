#Viết chương trình để tìm phần tử nhỏ nhất trong tuple

my_tuple = (3, 6, 9, 1, 7, 5, 4)

min_element = my_tuple[0]

for element in my_tuple:
    if element < min_element:
        min_element = element

print("Phan tu nho nhat trong tuple la:", min_element)