#Viết hàm để tính tổng các chữ số của một số

def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

try:
    number = int(input("Nhap mot so nguyen: "))
    print(f"Tong cac chu so cua {number} la: {sum_of_digits(number)}")
except ValueError:
    print("Vui long nhap mot so nguyen hop le.")
    