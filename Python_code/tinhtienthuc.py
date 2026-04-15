#Viết chương trình tính số tiền thực của
#một tài khoản ngân hàng dựa trên nhật ký giao dịch được nhập vào từ giao diện điều khiển.
#Vd: D la so tien nap; W la so tien rut


sotien=0

while True:
    s = input("nhap nhat ki giao dich (vd: D 200):")

    if not s:
        break
    values = s.split()
    thuchien=values[0]
    sotiengiaodich=int(values[1])

    if thuchien=="D":
        sotien+=sotiengiaodich
    elif thuchien=="W":
        sotien-=sotiengiaodich
    else:
        pass

print("So tien trong tai khoan ngan hang la:", sotien)