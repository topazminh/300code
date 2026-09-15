#Viết chương trình để tìm ước số chung lớn nhất (USCLN) của hai số

def gcd(a, b):
    while b != 0:
        a, b = b, a % b 
    return a

try:
    num1 = int(input("Nhap so thu nhat: "))
    num2 = int(input("Nhap so thu hai: "))

    uscln = gcd(num1, num2)
    print(f"Uoc so chung lon nhat cua {num1} va {num2} la: {uscln}")
except ValueError:
    print("Vui long nhap cac so nguyen hop le.")