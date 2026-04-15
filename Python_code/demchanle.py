
n = int(input("Nhập số phần tử: "))
a = []

for i in range(n):
    x = int(input(f"a[{i}]= "))
    a.append(x)

chan = 0
le = 0

for x in a:
    if x % 2 == 0:
        chan += 1
    else:
        le += 1

print("Số chẵn:", chan)
print("Số lẻ:", le)
