#Viết chương trình để lấy tất cả các giá trị trong dictionary

my_dict = {
    'name': 'Nguyet',
    'age': 3,
    'city': 'TP HCM'
}
print("Dictionary ban dau:", my_dict)

values = my_dict.values()
values_array = list(values)
print("Array cac gia tri trong dictionary:", values_array)
