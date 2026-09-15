def calculate_average(scores):
    return sum(scores) / len(scores)

def classify_student(average):
    if average >= 9.0:
        return "Xuat sac"
    elif average >= 8.0:
        return "Gioi"
    elif average >= 6.5:
        return "Kha"
    elif average >= 4.0:
        return "Trung binh"
    else:
        return "Yeu"

try:
    scores = []
    num_subjects = int(input("Nhap so luong mon hoc: "))
    if num_subjects <= 0:
        print("So luong mon hoc phai lon hon 0.")
    else:
        for i in range(num_subjects):
            score = float(input(f"Nhap diem mon hoc thu {i+1}: "))
            if score < 0 or score > 10:
                print("Diem so phai tư 0 den 10. Vui long nhap lai.")
                break
            scores.append(score)

        if len(scores) == num_subjects:
            average_score = calculate_average(scores)
            classification = classify_student(average_score)
            print(f"Diem trung binh: {average_score:.2f}")
            print(f"Xep loai: {classification}")
except ValueError:
    print("Vui long nhap mot so hop le.")    
