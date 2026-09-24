#Viết hàm để tính chu vi và diện tích hình chữ nhật

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def rectangle_area(length, width):
    return length * width

try:
    length = float(input("Nhap chieu dai cua hinh chu nhat: "))
    width = float(input("Nhap chieu rong cua hih chu nhat: "))

    if length < 0 or width < 0:
        print("Chieu dai và chieu rong phai la nhung so khong am.")
    else:
        perimeter = rectangle_perimeter(length, width)
        area = rectangle_area(length, width)
        print(f"Chu vi cua hinh chu nhat la: {perimeter}")
        print(f"Dien tich cua hinh chu nhat la: {area}")
except ValueError:
    print("Vui long nhap mot gia tri hop le cho chieu dai va chieu rong.")
    