import tkinter as tk
from tkinter import messagebox
import sqlite3

# Kết nối đến cơ sở dữ liệu
conn = sqlite3.connect('QLMonAn.db')
cursor = conn.cursor()

# Tạo bảng món ăn nếu chưa tồn tại
cursor.execute('''
    CREATE TABLE IF NOT EXISTS MonAn (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ten_mon_an TEXT,
        gia INTEGER
    )
''')
conn.commit()

class QuanLyMonAnApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý món ăn")

        self.create_widgets()

    def create_widgets(self):
        # Label và Entry cho tên món ăn và giá
        tk.Label(self.root, text="Tên món ăn").grid(row=0, column=0, padx=10, pady=5)
        self.ten_mon_an_entry = tk.Entry(self.root)
        self.ten_mon_an_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Giá").grid(row=1, column=0, padx=10, pady=5)
        self.gia_entry = tk.Entry(self.root)
        self.gia_entry.grid(row=1, column=1, padx=10, pady=5)

        # Button để thêm món ăn
        tk.Button(self.root, text="Thêm món ăn", command=self.them_mon_an).grid(row=2, column=0, columnspan=2, pady=10)

    def them_mon_an(self):
        ten_mon_an = self.ten_mon_an_entry.get()
        gia = self.gia_entry.get()

        if ten_mon_an and gia:
            try:
                gia = int(gia)
                cursor.execute("INSERT INTO MonAn (ten_mon_an, gia) VALUES (?, ?)", (ten_mon_an, gia))
                conn.commit()
                messagebox.showinfo("Thông báo", "Thêm món ăn thành công")
            except ValueError:
                messagebox.showerror("Lỗi", "Giá phải là số nguyên")
        else:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin món ăn")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuanLyMonAnApp(root)
    root.mainloop()
