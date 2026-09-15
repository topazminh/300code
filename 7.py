def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

try:
    year = int(input("Nhap mot nam: "))
    if is_leap_year(year):
        print(f"Nam {year} la nam nhuan.")
    else:
        print(f"Nam {year} khong phai la nam nhuan.")
except ValueError:
    print("Vui long nhap mot so nguyen hop le.")