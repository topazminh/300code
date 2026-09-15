def count_even_odd(numbers):
    count_even = 0
    count_odd = 0
    for number in numbers:
        if number % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd

try:
    input_list = input("Nhap cac so nguyen, cach nhau bang dau cach: ")
    numbers = [int(num) for num in input_list.split()]

    even_count, odd_count = count_even_odd(numbers)
    print(f"So luong so chan: {even_count}")
    print(f"So luong so le: {odd_count}")
except ValueError:
    print("Vui long nhap cac so nguyen hop le.")