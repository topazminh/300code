def find_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

try:
    num1 = int(input("Nhap so nguyen thu nhat: "))
    num2 = int(input("Nhap so nguyen thu hai: "))
    num3 = int(input("Nhap so nguyen thu ba: "))

    max_number = find_max_of_three(num1, num2, num3)
    print(f"So lon nhat trong ba so la: {max_number}")
except ValueError:
    print("Vui long nhap so nguyen hop le.")
