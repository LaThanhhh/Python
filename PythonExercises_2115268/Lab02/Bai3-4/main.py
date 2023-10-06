from phan_so import PhanSo
from danh_sach_phan_so import DanhSachPhanSo

ds = DanhSachPhanSo()
ds.docTuFile("C:\Users\\cict\\Downloads\\PythonExercises_2115268\\Lab02\Bai3-4\\du_lieu.txt")
print("Danh sách phân số đọc từ tập tin: ")
ds.xuat()

print("-"*50)
print("Danh sách phân số âm: ")
kq = ds.layDsPsAm()
kq.xuat()
