a = list(map(int, input("Nhập các số: ").split()))
x = int(input("Nhập số cần tìm: "))

if x in a:
    print(x, "có trong list")
else:
    print(x, "không có trong list")