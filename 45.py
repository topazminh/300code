#Viết chương trình để kiểm tra một key có tồn tại trong dictionary khong

my_dict = {
    'name': 'Hung',
    'age': '10',
    'city': 'Bac Ninh'
}
print("Dictionary ban dau:", my_dict)

key_to_check = input("Nhap khoa can kiem tra: ")

if key_to_check in my_dict:
    print(f"Khoa '{key_to_check}' ton tai trong dictionary.")
else:
    print(f"Khoa '{key_to_check}' khong ton tai trong dictionary.")

