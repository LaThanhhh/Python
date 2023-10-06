import math
from hinh_hoc import HinhHoc

class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

#Sử dụng ct
hinh_chu_nhat = HinhChuNhat(3, 4)
print("Hình chữ nhật có chiều dài:", hinh_chu_nhat.chieu_dai)
print("Hình chữ nhật có chiều rộng:", hinh_chu_nhat.chieu_rong)
print("Diện tích hình chữ nhật:", hinh_chu_nhat.tinh_dien_tich())
