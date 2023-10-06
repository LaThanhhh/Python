
class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so
    
    def rut_gon(self):
        ucln = self.tim_ucln(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln
    
    @staticmethod
    def tim_ucln(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"
    
    def __add__(self, other):
        tu_so_moi = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau_so_moi = self.mau_so * other.mau_so
        phan_so_moi = PhanSo(tu_so_moi, mau_so_moi)
        phan_so_moi.rut_gon()
        return phan_so_moi
    
    def __sub__(self, other):
        tu_so_moi = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        mau_so_moi = self.mau_so * other.mau_so
        phan_so_moi = PhanSo(tu_so_moi, mau_so_moi)
        phan_so_moi.rut_gon()
        return phan_so_moi
    
    def __mul__(self, other):
        tu_so_moi = self.tu_so * other.tu_so
        mau_so_moi = self.mau_so * other.mau_so
        phan_so_moi = PhanSo(tu_so_moi, mau_so_moi)
        phan_so_moi.rut_gon()
        return phan_so_moi
    
    def __truediv__(self, other):
        tu_so_moi = self.tu_so * other.mau_so
        mau_so_moi = self.mau_so * other.tu_so
        phan_so_moi = PhanSo(tu_so_moi, mau_so_moi)
        phan_so_moi.rut_gon()
        return phan_so_moi

a = PhanSo(2,3)
b = PhanSo(3, 5)

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")  
print(f"{a} * {b} = {a*b}") 
print(f"{a} / {b} = {a/b}")

