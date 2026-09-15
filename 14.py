#Viết hàm để tìm số lớn nhất trong một danh sách 

def find_max(numbers):
    if not numbers:
        return "Danh sach rong, khong co so lon nhat."
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

try:
    input_numbers = input("Nhap cac so, cach nhau boi dau cach: ")
    numbers = [float(num) for num in input_numbers.split()]

    if not numbers:
        print("Danh sach rong, khong co so lon nhat.")
    else:
        max_number = find_max(numbers)
        print(f"So lon nhat trong danh sach la: {max_number}")
except ValueError:
    print("Vui long nhap cac so hop le.")