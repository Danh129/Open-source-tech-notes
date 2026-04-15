#Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào
#  và tạo ra một mảng 2 chiều. Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.
#Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.

#Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

input_str = input("Nhập X, Y: ")

#tach chuoi
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0] #so x (cot)
colNum=dimensions[1] #so y (dong)

#tao ma tran 2 chieu toan so 0
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

# tao so trong mang
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col # hang 0 [toan so 0]
                                     # hang 1 [1*0, 1*1, 1*2..... ]
                                     # hang 2 [2*0, 2*1, 2*2......]
                                     
print(multilist)