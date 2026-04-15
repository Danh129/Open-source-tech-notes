n=list(map(int, input("nhap day 3 so: ").split()))
Max=n[0]
Min=n[0]

for x in n:
    if x > Max:
        Max=x
    elif x < Min:
        Min=x
    else:
        print("khong hop le")
print("min la:", Min)
print("max la:", Max)
