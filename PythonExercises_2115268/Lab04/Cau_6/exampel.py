import tkinter as tk
from tkinter import messagebox
import re


def validate_student_id():
    student_id = entry_student_id.get()
    if not student_id.isdigit() or len(student_id) != 7:
        messagebox.showerror("Lỗi", "Mã số sinh viên phải là 7 chữ số.")
    else:
        return True

def validate_email():
    email = entry_email.get()
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        messagebox.showerror("Lỗi", "Email không hợp lệ.")
    else:
        return True

def validate_phone_number():
    phone_number = entry_phone_number.get()
    if not phone_number.isdigit() or len(phone_number) != 10:
        messagebox.showerror("Lỗi", "Số điện thoại phải có 10 chữ số.")
    else:
        return True

def validate_semester():
    semester = entry_semester.get()
    if semester not in ["1", "2", "3"]:
        messagebox.showerror("Lỗi", "Học kỳ chỉ có thể là 1, 2 hoặc 3.")
    else:
        return True

def validate_date_of_birth():
    date_of_birth = entry_date_of_birth.get()
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    if not re.match(pattern, date_of_birth):
        messagebox.showerror("Lỗi", "Ngày sinh phải có định dạng dd/mm/yyyy.")
    else:
        return True

def save_to_excel():
    student_id = entry_student_id.get()
    email = entry_email.get()
    phone_number = entry_phone_number.get()
    semester = entry_semester.get()
    date_of_birth = entry_date_of_birth.get()
    academic_year = entry_academic_year.get()

    if (validate_student_id() and validate_email() and validate_phone_number()
            and validate_semester() and validate_date_of_birth()):
        subjects = [subject1.get(), subject2.get(), subject3.get()]

        # Kiểm tra người dùng đã chọn môn học nào chưa
        if not any(subjects):
            messagebox.showerror("Lỗi", "Vui lòng chọn ít nhất một môn học.")
            return
        
        data = {
            'Mã số sinh viên': [student_id],
            'Email': [email],
            'Số điện thoại': [phone_number],
            'Học kỳ': [semester],
            'Ngày sinh': [date_of_birth],
            'Năm học': [academic_year]
        }

        for i, subject in enumerate(subjects):
            if subject:
                data[f'Môn học {i+1}'] = [subject]

        df = pd.DataFrame(data)
        df.to_excel('danh_sach_dang_ky.xlsx', index=False)
        messagebox.showinfo("Thông báo", "Đăng ký thành công.")

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Đăng kí học phần")

# Tạo các nhãn và trường nhập liệu cho mã số sinh viên
label_student_id = tk.Label(window, text="Mã số sinh viên")
label_student_id.grid(row=0, column=0)
entry_student_id = tk.Entry(window)
entry_student_id.grid(row=0, column=1)

# Tạo các nhãn và trường nhập liệu cho email
label_email = tk.Label(window, text="Email")
label_email.grid(row=1, column=0)
entry_email = tk.Entry(window)
entry_email.grid(row=1, column=1)

# Tạo các nhãn và trường nhập liệu cho số điện thoại
label_phone_number = tk.Label(window, text="Số điện thoại")
label_phone_number.grid(row=2, column=0)
entry_phone_number = tk.Entry(window)
entry_phone_number.grid(row=2, column=1)

# Tạo các nhã