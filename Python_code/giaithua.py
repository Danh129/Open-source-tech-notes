n = int(input("Nhap n: "))

gt = 1
for i in range(1, n + 1):
    gt *= i

print(f"{n}! =", gt)
