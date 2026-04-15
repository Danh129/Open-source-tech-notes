# Nhập danh sách số
arr = list(map(int, input("Nhập các số (cách nhau bởi dấu cách): ").split()))

# Tách số chẵn và số lẻ
chan = [x for x in arr if x % 2 == 0]
le = [x for x in arr if x % 2 != 0]

# Sắp xếp
chan.sort(reverse=True)              # tăng dần
le.sort()    # giảm dần

# Ghép kết quả
result = chan + le

print("Kết quả:", result)