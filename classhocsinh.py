class hocsinh:
    so_luong = 0
    #Khởi tạo đối tượng với thuộc tính tên , thuộc tính số lượng tăng lên 1
    def __init__(self, ten):
        self.ten = ten
        hocsinh.so_luong +=1
        
        #Phương thức lớp trả về số lượng đối tượng
    @classmethod
    def so_luong_hs(cls):
        return cls.so_luong
        
    #Phương thức tĩnh trả về tên trường
    @staticmethod
    def ten_truong():
        return 'ICANTECH'
        
        #Tạo 2 đối tượng có tên An và Bình
hs1 = hocsinh("An")
hs2 = hocsinh("Binh")

# in ra nội dung " Số lượng học sinh lớp ICANTECH là 2"
print('Số lượng học sinh lớp', hocsinh.ten_truong(), 'là', hocsinh.so_luong_hs())
        