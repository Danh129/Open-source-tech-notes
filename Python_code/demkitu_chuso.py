s = input("Nhap chuoi: ")

dem_chu_so = 0
dem_ky_tu = 0
tong = 0

for ch in s:
    if ch.isdigit():
        dem_chu_so += 1
        tong += int(ch)
    elif ch.isalpha():
        dem_ky_tu += 1

print("So chu so:", dem_chu_so)
print("So ky tu chu:", dem_ky_tu)
print("Tong cac chu so:", tong)
