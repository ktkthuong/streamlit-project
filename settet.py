# class HinhTron:
#     def __init__(self, r=0):
#         self.bankinh = r
#         self.PI = 3.14
#     # Khai báo phương thức diện tích là 1 getter
#     @property    
#     def dientich(self):
#         return self.bankinh * self.bankinh * self.PI
    
# cirle1 = HinhTron(r=3)

# print(cirle1.dientich())
# cirle1.dientich = 5 # sai chỗ này vì diện tích bản chất là phương thức, không thể gán giá trị

import math
class cirlce:
    def __init__(self, r=0):
        self.bankinh = r
        self.PI = 3.14
    # Khai báo phương thức diện tích là 1 getter
    @property    
    def dientich(self):
        return self.bankinh * self.bankinh * self.PI
    
    #Khai báo phương thức getter - > setter gán ngược lại giá trị cho bán kính
    @dientich.setter
    def dientich(self, dientichmoi):
        self.bankinh = math.sqrt(dientichmoi / math.pi)
    
cirle1 = cirlce(r=3)
#in ra bán kính mới sau khi đã gán diện tích
cirle1.dientich = 3.14
print("Ban kính mới: ", cirle1.bankinh)
