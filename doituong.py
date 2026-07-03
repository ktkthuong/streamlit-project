class Dog:
    leg = 4
    breed = ''
    #Khai báo phương thức show với tham số doituong đại diện cho 1 đối tượng lớp Dog
    def show(doituong):
        print("Chó sẽ có: ", doituong.leg, 'chân')
        print('Và giống chó: ', doituong.breed)
        
#Khai báo đối tượng cho1 thuộc lớp dog
cho1 = Dog()

#đặt thuộc tính breed của đối tượng là pitpull
cho1.breed = "pitbull"
#Truy cập thuộc tính leg của đối tượng cho1
#Gán thuộc tính leg của đối tượng chó 1 vào biến chan
chan = cho1.leg
#Gán thuộc tính breed của đối tượng cho1 vào biến giong_cho
giong_cho = cho1.breed

#In kết quả của thuộc tính
print(chan, 'chân')
print('giống chó: ', giong_cho)

