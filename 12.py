#Viết hàm để tính tổng các số từ 1 đến n

def sum_of_numbers(n):
    if n < 1:
        return "Vui long nhap mot so nguyen duong lon hon hoac bang 1."
    return n * (n + 1) // 2

try:
    number = int(input("Nhap mot so nguyen duong: "))
    if number < 1:
        print("Vui long nhap mot so nguyen duong lon hon hoac bang 1.")
    else:
        print(f"Tong cac so tu 1 den {number} la: {sum_of_numbers(number)}")
except ValueError:
    print("Vui long nhap mot so nguyen hop le.")
    