import math

class HinhTron:
    def __init__(self, ban_kinh) :
        self.ban_kinh = ban_kinh
    def tinh_dien_tich(self):
        return math.pi * self.ban_kinh ** 2
