class HinhTron:
    def __init__(self, r=0):
        self.bankinh = r
        self.PI = 3.14
    # Khai báo phương thức diện tích là 1 getter
    @property    
    def dientich(self):
        return self.bankinh * self.bankinh * self.PI
    
cirle1 = HinhTron(r=3)
print(cirle1.dientich)