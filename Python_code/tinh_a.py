#Viết một chương trình tính giá trị của
#  a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.

#Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234
a = input("nhap so ban muon:")

#%s: vi tri chen chuoi
#%: toan tu thuc hien chen gia tri vao chuoi
#vd: a=1
n1=int("%s"%(a))                #1
n2=int("%s%s"%(a, a))           #11
n3=int("%s%s%s"%(a, a, a))      #111
n4=int("%s%s%s%s"%(a, a, a, a)) #1111

print("Ket qua:", n1+n2+n3+n4)