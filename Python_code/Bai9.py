tong=0
dem=0
min=None
max=None

while True:
    a=int(input("Nhap so nguyen: "))
    

    if max is None:
        max = min = a
    elif max < a:
        max = a
    elif min > a:
        min = a

    tong+=a
    dem+=1
    if a == 0:
        break
    else:
        tb = tong/dem
    print (f"tong cac so", tong)
    print (f"Gia tri max", max)
    print (f"Gia tri min", min)
    print (f"Tb cong", tb)