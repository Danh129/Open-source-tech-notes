def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        print (" Khong thoa ct! ")
    else:
        return a / b

while True:
    print (f"May tinh mini: ")
    print ("1. Cong")
    print ("2. Tru")
    print ("3. Nhan")
    print ("4. Chia")
    print ("5. Thoat")

    chon=int(input("Nhap lua chon (1-5): "))
    if chon < 1 or chon > 5:
        print (" Vui long nhap lai (1-5)! ")
        continue
    if chon == 5:
        print ("Tam biet")
        break

    #a, b = map(float, input(" Nhap 2 so de thuc hien: ").split(','))
    a = float(input(" Nhap so thu nhat: "))
    b = float(input(" Nhap so thu hai: "))

    if chon == 1:
        print (f"Phep cong: {a} + {b} = {cong(a, b)}")
    elif chon == 2:
         print (f"Phep tru: {a} - {b} = {tru(a, b)}")
    elif chon == 3:
         print (f"Phep nhan: {a} x {b} = {nhan(a, b)}")
    elif chon == 4:
         if isinstance(chia(a, b), str):
             print (chia(a, b))
         else:
             print (f"Phep chia: {a} : {b} = {chia(a, b)}")
    