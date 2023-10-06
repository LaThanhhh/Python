import datetime
f = open("sinhvien.txt","r")
print(f.read())
class SinhVien:
    #Biến của lớp, chung cho tất cả các đối tượng thuộc lớp
    truong = "Đại học Đà Lạt"
    # Hàm khởi tạo, hàm tạo lập: khởi gán các thuộc tính của đối tượng
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    # cho phép truy xuất tới thuộc tính từ bên ngoài thông qua trường maSO

    @property
    def maSo(self):
        return self.__maSo
    # cho phép thay đổi giá trị thuộc tính maSO
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso
    # Phương thức tĩnh: ccas phương thức không truy xuất gì ddeeens thuộc tính, hành vi của lớp
    # những phương thức này không cần truyền tham số mặc định self
    # đây không phải lf một hành vi( phương thức) của một đối tượng thuộc lớp
    @staticmethod
    def laMaSoHopLe(maso:int):
        return len(str(maso))== 7
    # Phương thức của lớp, chỉ xuất tới các biến thành viên của lớp
    #không truy cuất được các thuộc tính riêng của đối tượng
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi
    # tương tự ghi đè phương thức toString()
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    # hành vi của đối tượng sinh viên
    def Xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")

