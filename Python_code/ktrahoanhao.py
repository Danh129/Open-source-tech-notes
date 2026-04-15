def ktrahoanhao(n):
    s=sum(i for i in range(1, n) if n%i == 0)
    return s == n

n=int(input("Nhap so can kiem tra:"))
if ktrahoanhao(n):
    print(n, "la so hoan hao")
else:
    print(n, "khong phai la so hoan hao")

