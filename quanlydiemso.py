
#Khai báo lớp học sinh
class Student:
    #Khai báo thuộc tính
    name = '' # Tên học sinh
    scores = {} # Lưu trữ điểm của học sinh trong dictionary
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
        
    # Phương thức tìm điểm cao nhất
    def max_score(std1):
        max_subject = max(std1.scores, key=std1.scores.get)
        max_mark = std1.scores[max_subject]
        return max_subject, max_mark
        
    # Phương thức hiển thị thông tin của học sinh
    def show_info_student(std1):
        # In tên học sinh ra
        print('Họ tên học sinh: ', std1.name)
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
        print('Học sinh xếp loại: ', std1.show_rank())
        
        # Hiển thị môn có điểm cao nhất
        subject, score = std1.max_score()
        print(f'Môn có điểm cao nhất: {subject} ({score} điểm)')
        
std1 = Student()
std1.name = "Nguyễn Văn A"
std1.scores = {
    'Toán': 10,
    'Văn' : 7,
    'Anh' : 9
}
std1.show_info_student()
    
    