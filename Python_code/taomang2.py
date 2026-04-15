list=[]
n=int(input("nhap so luong:"))
for i in range(n):
    x=int(input(f"Nhap so {i+1}:"))
    list.append(x)
max=list[0]
for i in list:
    if max < i:
        max=i
print("So lon nhat la:", max)