
#Khai báo lớp học sinh
class Student:
    # Biến lớp dùng để đếm số lượng học sinh
    # student_count = 0
    # Phương thức khởi tạo đối tượng học sinh
    def __init__(self, nam, mat, lit, eng):
        self.name = nam
        self.scores = {
            'Toán': mat,
            'Văn': lit,
            'Anh': eng
        }
        # # Mỗi khi tạo đối tượng mới thì tăng biến đếm
        # Student.student_count += 1
    
    #Phương thức tạo đối tượng học sinh từ một chuỗi
    @classmethod
    def from_string(cls, student_string):
        #Chia mỗi thông tin học sinh thành tên, điểm toán, Văn và Anh
        na, ma, lit, eng = student_string.split(',')
        #Chuyển điểm từ chuỗi sang số nguyên
        ma = int(ma)
        lit = int(lit)
        eng = int(eng)
        #Trả về đối tượng học sinh mới với thông tin vừa lấy được
        return cls(na, ma, lit, eng)
    #Phương thức trả về thông tin trường
    @staticmethod
    def get_school_info():
        #Trả về thông tin trường của học sinh
        return 'ICANTECH'
        
    # #Tạo phương thức static để trả về số lượng học sinh
    # @staticmethod
    # def count_students():
    #     return Student.student_count
        
    # Phương thức tính điểm trung bình
    def score_average(std1):
        return(std1.scores['Toán'] + std1.scores['Văn'] + std1.scores['Anh']) / 3
    
    # Phương thức xếp loại học sinh dựa trên điểm trung bình
    def show_rank(std1):
        # Lấy điểm trung bình và chuyển thành số nguyên
        avg_score = int(std1.score_average())
        # So sánh và đưa ra kết luận
        if avg_score >= 9:
            return 'Giỏi'
        elif avg_score >= 6:
            return 'Khá'
        elif avg_score >= 4:
            return 'Trung bình'
        else:
            return 'Yếu'
    # Phương thức hiển thị thông tin của học sinh
    def show_info_student(self):
        # In tên học sinh ra
        print('Học sinh: ', self.name, self.get_school_info(), 'có thông tin về điểm số như sau: ')
        for key in std1.scores:
            # In điểm
            print(f"Điểm môn {key}: {std1.scores[key]}")
        #Tính điểm trung bình
        average_return = std1.score_average()
        # Làm tròn 2 chữ số thập phân
        average_return = round(average_return, 2)
        #In điểm trung bình
        print('Điểm trung bình ba môn: ', average_return)
        #In xếp loại học sinh
        self.show_rank()
        

# Tạo đối tượng học sinh và hiển thị thông tin
#chạy chương trình và viết theo cú pháp ví dụ nhé
# Ví dụ: 'Nguyễn Thế Doanh, 10, 8, 9'
student_string = input('Thông tin học sinh: ')
std1 = Student.from_string(student_string)
std1.show_info_student()
    
    