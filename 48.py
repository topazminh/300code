#Viết chương trình để lấy tất cả các cặp key-value trong dictionary

my_dict = {
    'name': 'Linh',
    'age': 7,
    'city': 'Bac Kinh'
}
print("Dictionary ban dau:", my_dict)

items = my_dict.items()
items_list = list(items)
print("Danh sach cac cap key-value trong dictionary:", items_list)
