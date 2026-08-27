def check_even_odd(n):
    if n % 2 == 0:
        return "So ban nhap la so chan."
    else:
        return "So ban nhap la so le."

try:
    number = int(input("Nhap mot so nguyen: "))
    result = check_even_odd(number)
    print(result)
except ValueError:
    print("Vui long nhap so nguyen hop le.")
