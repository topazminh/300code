#Viết hàm để kiểm tra một chuỗi có phải là palindrome không

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalum())
    return s == s[::-1]

input_string = input("Nhap mot chuoi: ")

if is_palindrome(input_string):
    print(f'"{input_string}" la palindrome.')
else:
    print(f'"{input_string}" khong phai la palindrome.')