import random

class Game:
    def __init__(self, type = 'xúc xắc'):
        self.type = type #Khởi tạo thuộc tính trò chơi
        self.scorelist = [] #Khởi tạo danh sách điểm số rỗng
        
    @property
    def score(self):
        if (self.type == 'đồng xu'):
            #Trả về 0 hoặc 1 ngẫu nhiên cho trò chơi đồng xu
            return random.randint(0, 1)
        elif (self.type == 'xúc xắc'):
            # Trả về 1 số nguyên từ 1-6 ngẫu nhiên cho trò chơi xúc xắc
            return random.randint(1, 6)
        
    #Khai báo phương thức quantity
    @property
    def quantity(self):
        #Trả về số lượng lần gieo trong danh sách điểm số
        return len(self.score_list)
    @quantity.setter
    def quantity(self, new_quantity):
        for _ in range(new_quantity):
            #Thêm điểm số của mỗi lần gieo vào danh sách điểm số
            self.score_list.append(self.score)
    @quantity.deleter
    def quantity(self):
        self.score_list = [] # Đưa danh sách điểm số về rỗng
        
    #Định nghĩa một thuộc tính tổng điểm của tất cả các lần gieo
    @property
    def total_score(self):
        return sum(self.score_list) #trả về tổng của danh sách điểm số
    
    def play(self, quantity=0):
        del self.quantity # Xóa một thuộc tính đối tượng hiện tại
        self.quantity = quantity # Gán một thuộc tính số lượng mới
        print(f"Điểm: {self.quantity} lần gieo {self.type}: {self.score_list}\nTổng điểm {self.type}: {self.total_score}")
 
#tạo đối tượng game1, game2 thuộc lớp Game và thực hiện các phương thức đã cài đặt           
game1 = Game(type='đồng xu')
game1.play(quantity=5)
game2 = Game(type='xúc xắc')
game2.play(quantity=3)