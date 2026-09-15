def calculate_taxi_fare(km):
    if km <= 1:
        fare = 10000
    elif km <= 10:
        fare = 10000 + (km - 1) * 8500
    else:
        fare = 10000 + 9 * 8500 + (km - 10) * 7500
    return fare 

try:
    distance = float(input("Nhap so km da di: "))
    if distance < 0:
        print("So km dã di khong hop le. Vui lonh nhap so duong.")
    else:
        total_fare = calculate_taxi_fare(distance)
        print(f"Tong tien taxi la: {total_fare} VNĐ")
except ValueError:
    print("Vui long nhap mot so hop le.") 