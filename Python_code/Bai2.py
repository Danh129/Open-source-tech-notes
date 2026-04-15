a=int(input("Nhap so thu nhat (gia tri min)"))
b=int(input("Nhap so thu hai (gia tri max)"))

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end="")