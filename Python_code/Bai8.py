def thongtin(n):
    tmp = n
    tong=0
    dem=0

    while tmp > 0:
        chu_so = tmp % 10
        tong+=chu_so
        dem+=1
        tmp //=10
    return dem, tong

n = int(input(" Nhap so ban muon: "))
if n > 0:
    so_chu_so, tong_chu_so = thongtin(n)
    print (f"so {n} co {so_chu_so} chu so va tong chu so {tong_chu_so}")
else:
    print ("khong hop le!")
