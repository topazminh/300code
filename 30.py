#Viết chương trình để đếm số lần xuất hiện của một phần tử trong danh sách

my_list = [1, 3, 7, 8, 7, 5, 6, 7, 2, 7, 10]
print("Danh sách ban đầu:", my_list)

element_to_count = input("Nhập phần tử muốn đếm số lần xuất hiện: ")

try:
    element_to_count = int(element_to_count)
except ValueError:
    try:
        element_to_count = float(element_to_count)
    except ValueError:
        pass

count = my_list.count(element_to_count)
print(f"Phần tử {element_to_count} xuất hiện {count} lần trong danh sách.")