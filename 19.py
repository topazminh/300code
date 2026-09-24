#Viết hàm tính chu vi và diện tích hình tròn

import math

def circumference(radius):
    return 2 * math.pi * radius

def area(radius):
    return math.pi * radius * radius

try:
    radius = float(input("Nhap ban kinh cua hinh tron: "))
    if radius < 0:
        print("Ban kinh phai la mot so khong am.")
    else:
        circ = circumference(radius)
        ar = area(radius)
        print(f"Chu vi cua hinh tron la: {circ}")
        print(f"Dien tich cua hinh tron la: {ar}")
except ValueError:
    print("Vui long nhap mot gia tri hop le cho ban kinh.")
    