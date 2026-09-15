def check_number(n):
    if n > 0:
        return "So ban nhap la so duong."
    elif n < 0:
        return "So ba nhap là so am."
    else:
        return "So ban nhap la so khong (Khong duong khong am)."

try:
    number = int(input("Nhap mot so nguyen: "))
    result = check_number(number)
    print(result)
except ValueError:
    print("Vui long nhap so nguyen hop le.")
    