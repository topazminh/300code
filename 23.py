#Viết chương trình để thêm một phần tử vào đầu danh sách

my_list = [1, 2, 3, 4, 5]

new_element = input("Nhap phan tu muon them vao dau danh sach: ")

my_list.insert(0, new_element)

print("Danh sach sau khi them phan tu:", my_list)
