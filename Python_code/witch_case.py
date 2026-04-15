
print("1. Kiem tra so hoan hao:")
chon=int(input("Nhap lua chon:"))
n=int(input("Nhap so can kiem tra:"))

if chon == 1:
    s=sum(i for i in range(1, n) if n%i == 0)
    if s == n:
        print("So hoan hao")
    else:
        print("Khong phai la so hoan hao")

