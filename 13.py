#Viết hàm để kiểm tra một số có phải là số nguyên tố không

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5 
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    number = int(input("Nhap mot so nguyen: "))
    if is_prime(number):
        print(f"{number} la so nguyen to.")
    else:
        print(f"{number} khong phai la so nguyen to.")
except ValueError:
    print("Vui long nhap so nguyen hop le.")