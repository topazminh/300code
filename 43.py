#Viết chương trình để thêm một cặp key-value vào dictionary

my_dict = {
    'name': 'Topaz',
    'age': 25,
    'city': 'Bac Ninh'
}
print("Dictionary ban dau:", my_dict)

new_key = input("Nhap khoa can them: ")
new_value = input("Nhap gia tri can them: ")

my_dict[new_key] = new_value
print("Dictionary sau khi them cap key_value:", my_dict)
