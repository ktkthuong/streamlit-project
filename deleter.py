import math
class cirlce:
    def __init__(self, r=0):
        self.bankinh = r
        self.PI = 3.14
    # Khai báo phương thức diện tích là 1 getter
    @property    
    def dientich(self):
        if self.bankinh is not None:
            return self.bankinh * self.bankinh * self.PI
        else:
            return print("Không có bán kính để tính diện tích.")
    
    #Khai báo phương thức deleter
    @dientich.deleter
    def dientich(self):
        self.bankinh = None # Xóa một thuộc tính bán kính
    
cirle1 = cirlce(r=3)
#in ra bán kính mới sau khi đã gán diện tích
cirle1.dientich = 3.14
del cirle1.dientich
print(cirle1.dientich)
