class NhanVien:
    def __init__(self, manhanvien, tennhanvien, luongcoban, chucvu,hesoluong):
        self. manhanvien = manhanvien
        self. tennhanvien = tennhanvien
        self. luongcoban = luongcoban
        self. chucvu = chucvu
        self. hesoluong = hesoluong
    def tinhluong(self):
        return self.luongcoban* self.hesoluong
    def hienthithongtin(self):
        return f"""
                id: {self.manhanvien},
                Tên: {self.tennhanvien},
                Chức vụ: {self.chucvu},
                Lương: {self.tinhluong()}"""


nv1= NhanVien("NV001","Nguyen dep trai", 1000, "Developer",3.5) 
print(nv1.hienthithongtin())

class Quanly(NhanVien):
    def __init__(self, manhanvien, tennhanvien, luongcoban, ChucVu, hesoluong, bonus):
        super().__init__(manhanvien, tennhanvien, luongcoban, ChucVu, hesoluong,)
        self.bonus=bonus
    def tinhluong(self):
        return (super().tinhluong())+self.bonus
quanly=Quanly(1,"quản lý",10,"QL",10,1000)
def hienthithongtin(self):
        return f"""
                id: {self.manhanvien},
                Tên: {self.tennhanvien},
                Chức vụ: {self.chucvu},
                Lương: {self.tinhluong()}"""

print(quanly.hienthithongtin())

class Giamdoc(NhanVien):
    def __init__(self, manhanvien, tennhanvien, luongcoban, chucvu, hesoluong):
        super().__init__(manhanvien, tennhanvien, luongcoban, chucvu, hesoluong)
        
giamdoc=Giamdoc(1,"giám 1",5,"GD",10)
def hienthithongtin(self):
        return f"""
                id: {self.manhanvien},
                Tên: {self.tennhanvien},
                Chức vụ: {self.chucvu},
                Lương: {self.tinhluong()}"""

print(giamdoc.hienthithongtin())

