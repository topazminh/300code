#Viết chương trình để xóa một cặp key-value khỏi dictionary

my_dict = {
    'name': 'Beo',
    'age': 15,
    'city': 'Ha Noi'
}
print("Dictionary ban dau:", my_dict)

key_to_delete = input("Nhap khoa con xoa: ")

if key_to_delete in my_dict:
    my_dict.pop(key_to_delete)
    print(f"Da xoa cap key-value co khoa '{key_to_delete}'.")
else:
    print(f"Khoa '{key_to_delete}' khong ton tai trong dictionary.")

print("Dictionary sau khi xoa cap key-value:", my_dict)