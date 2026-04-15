import random

diem=1000
while diem > 0:

    xs1=random.randint(1, 6)
    xs2=random.randint(1, 6)
    xs3=random.randint(1, 6)

    tong=xs1 + xs2 + xs3
    print(f"Tong 3 xs: {xs1} + {xs2} + {xs3} = {tong}")

    if xs1 == xs2 == xs3:
        print ("Ban thua")
        continue

    doan=input("nhap (T/t) Tai, (X/x) Xiu: ").strip().lower()

    if 3 <= tong <= 10:
        kq = "x"
    else:
        kq = "t"

    if doan == kq:
        print(" Ban da thang")
        diem+=100
        print("Diem con lai cua ban la:", diem)
    else:
        print("Ban bi tru diem")
        diem-=10
        print("Diem con lai cua ban la:", diem)
