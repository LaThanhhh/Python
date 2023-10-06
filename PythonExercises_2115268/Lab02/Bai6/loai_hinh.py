from hinh_chunhat import HinhChuNhat
from hinh_tron import HinhTron
from hinh_vuong import HinhVuong
loai_hinh = input("Nhập loại hình (chunhat, tron, vuong): ")

if loai_hinh == "chunhat":
    chieu_dai = float(input("Nhập chiều dài: "))
    chieu_rong = float(input("Nhập chiều rộng: "))
    hcn = HinhChuNhat(chieu_dai, chieu_rong)
    dien_tich = hcn.tinh_dien_tich()
    chu_vi = hcn.tinh_chu_vi()
    print("Diện tích:", dien_tich)
    print("Chu vi:", chu_vi)
elif loai_hinh == "tron":
    ban_kinh = float(input("Nhập bán kính: "))
    ht = HinhTron(ban_kinh)
    dien_tich = ht.tinh_dien_tich()
    chu_vi = ht.tinh_chu_vi()
    print("Diện tích:", dien_tich)
    print("Chu vi:", chu_vi)
elif loai_hinh == "vuong":
    canh = float(input("Nhập cạnh: "))
    hv = HinhVuong(canh)
    dien_tich = hv.tinh_dien_tich()
    chu_vi = hv.tinh_chu_vi()
    print("Diện tích:", dien_tich)
    print("Chu vi:", chu_vi)
else:
    print("Loại hình không được hỗ trợ.")