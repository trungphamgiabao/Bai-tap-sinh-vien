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
    def __init__(self, manhanvien, tennhanvien, luongcoban, tienthuong, hesoluong, danhsachphongban):
        super().__init__(manhanvien, tennhanvien, luongcoban, "Quản lý", hesoluong)
        self.tienthuong=tienthuong
        self.danhsachphongban=danhsachphongban
    
    def tinhluong(self):
        return super().tinhluong()+self.tienthuong
    def hienthithongtin(self):
        info=super().hienthithongtin()
        return f"{info}, Phòng ban quản lý:{','.join(self.danhsachphongban)}"
ql1=Quanly("QL001","Phan hanh phuc", 2000,4,500,["Ký thuật", "kế toán"])

class GiamDoc(NhanVien):
    def __init__(self, manhanvien, tennhanvien, luongcoban, tienthuong, hesoluong, danhsachchinhanh):
        super().__init__(manhanvien, tennhanvien, luongcoban, "Giám Đốc", hesoluong)
        self.tienthuong=tienthuong
        self.danhsachchinhanh=danhsachchinhanh
    def tinhluong(self):
        if len(self.danhsachchinhanh)>3:
            return super().tinhluong()+self.tienthuong+1000
        else:
            return super().tinhluong()+self.tienthuong
    def hienthithongtin(self):
        info= super().hienthithongtin()
        return f"{info}, Chi nhánh quản lý:{','.join(self.danhsachchinhanh)}"
gd1=GiamDoc("GD001","Nguyen thi thanh cong",5000,5,2000,["Chi nhánh A","Chi nhánh B","Chi nhánh C","Chi nhánh D"])