import functools
import math
from pathlib import Path
from phan_so import PhanSo

class DanhSachPhanSo:
    def __init__(self) -> None:
        self.ds =[]
    def them(self, ps:PhanSo):
        self.ds.append(ps)
    def xuat(self):
        for ps in self.ds:
            print (ps, end='\t')
        print()
    
    def docTuFile(self, tenfile):

        with open(tenfile, 'r', encoding='utf-8') as f:
            for hang in f:
                du_lieu = hang.split('/')
                self.them(PhanSo(int(du_lieu[0]), int(du_lieu[1])))
    # Dem so phan so am trong bang
    def demPhanSoAm(self):
        dem = 0
        for ps in self.ds:
            if ps.tu_so * ps.mau_so <0:
                dem +=1
        return
    # lấy danh sách tất cả phân số âm
    def layDsPsAm(self):
        return DanhSachPhanSo([ps for ps in self.ds if ps < 0])
    # Tim phan so duong nho nhat 
    
      
            
    #Tim tat cac vi tri cua phan so x trong mang
    def timViTriPhanSoX(self, x):
        vitri =[]
        for i, ps in enumerate(self.ds_phanso):
            if ps.numerator == x.numerator and ps.denominator == x.denominator:
                vitri.append(i)
        return vitri

    
            
        
    #Tong tat ca cac phan so am trong mang
    def tinhTongPsAm(self):
        tongAm = PhanSo()
        for ps in self.ds:
            if ps < 0:
                tongAm += ps
        return tongAm
            
    #Xoa phan so x trong mang
    def xoaPhanSo(self, x:PhanSo):
        for ps in self.ds:
            if ps == x:
                self.ds.remove(ps)
    #Xoa tat cac phan so co tu la x
    # Sap xep phan so theo chieu tang, giam
   
    

    
    