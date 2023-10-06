from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien_phi_chinh_quy import SinhVienPhiCQ
from sinh_vien import SinhVien
from datetime import datetime

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
    
    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)
    
    def xuat(self):
       for sv in self.dssv:
           print(sv)

    def timSVTheoMs(self, ms:str):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == ms:
                return i
        else:
            return -1
    
    def timSvTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ) ]   
    
    # tim sinh vien co diem ren luyen tu 80 tro len
    
    
    # tim sinh vien co trinh do cao dang sinh truoc 15/8/1999
   



