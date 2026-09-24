#Viết chương trình để xóa một phần tử khỏi danh sách

my_list = [1, 2, 3, 4, 5]
element_to_remove = input("Nhap phan tu muon xoa khoi danh sach: ")

try:
    element_to_remove = int(element_to_remove)
except ValueError:
    try:
        element_to_remove = float(element_to_remove)
    except ValueError:
        pass

if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print("Danh sach sau khi xoa phan tu:", my_list)
else:
    print("Phan tu khong ton tai trong danh sach.")

    