#Viết chương trình để truy cập giá trị của một key trong dictionary

my_dict = {
    'name': 'Minh',
    'age': 20,
    'city': 'Ha Noi'
}
print("Dictionnary da tao:", my_dict)

key = input("Nhap khoa can truy cap: ")

if key in my_dict:
    value = my_dict[key]
    print(f"Gia tri cua khoa '{key}' la: {value}")
else:
    print(f"Khoa '{key}' khong ton tai trong dictionary.")
    