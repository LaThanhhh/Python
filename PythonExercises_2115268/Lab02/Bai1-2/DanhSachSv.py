from SinhVien import SinhVien
import datetime

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
    def themSinhVien(self,sv: SinhVien):
        self.dssv.append(sv)
    def xuat(self):
        for sv in self.dssv:
            print(sv)

    # Doc tu file
    def docTuFille(self, tenFile):
        with open(tenFile, 'sinhvien.txt', encoding="utf-8") as f :  
            for hang in f:
                du_lieu = hang.split('\t')
                self.themSinhVien(SinhVien(int(du_lieu[0]),int(du_lieu[1])))

                
    # Tìm sinh viên theo mssv, nếu có trả về sinh viên
    def timSVTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.mssv == mssv]
    # tìm sinh viên theo msssv. nếu có trả về vị trí của sinh viên trong danh sách
    def timVTSvTheoMssv(self, mssv:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1
    # xóa sinh viên có mã số mssv, thông báo xóa được hoặc không
    def xoaSVTheoMssv(self, maSo:int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
   # Tìm sinh viên tên "Nam"
    def timSvTheoTen(self):
        for i in range(len(self.dssv)):
            if self.dssv[i].ten == "Nam":
                return i
        return -1

    # Tìm những sinh viên sinh trước ngày
    def timSvSinhTruocNgay(self, ngay: datetime):
        for i in range(len(self.dssv)):
            if self.dssv[i].ngay < ngay:
                return i
        return -1
    # Sắp xếp tăng theo họ tên
    def sapXepTangTheoHoTen(self):
        self.dssv.sort(key=lambda sv: sv.hoTen)
    # sắp xeeos giảm theo họ tên
    def sapXepGiamTheoHoTen(self):
        self.dssv.sort(key=lambda sv: sv.hoTen, reverse=True)
    
ds_sv = DanhSachSv()
# Thêm sinh viên vào danh sách


# Sắp xếp tăng dần theo họ tên
ds_sv.sapXepTangTheoHoTen()
ds_sv.xuat()

# Sắp xếp giảm dần theo họ tên
ds_sv.sapXepGiamTheoHoTen()
ds_sv.xuat()
