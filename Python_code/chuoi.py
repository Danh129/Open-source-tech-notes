chuoi1 = "Tri tue nhan tao ngay nay co the thay the con nguoi trong mot so cong viec nhat dinh"
chuoi2 = "con nguoi ngay nay"

# Tách thành danh sách từ
ds1 = chuoi1.split()
ds2 = chuoi2.split()

# Lọc từ
ketqua = []
for tu in ds1:
    if tu not in ds2:
        ketqua.append(tu)

# Ghép thành chuỗi
chuoi_moi = " ".join(ketqua)

# Ghi vào file
with open("ketqua.txt", "w", encoding="utf-8") as f:
    f.write(chuoi_moi)

print("Chuoi moi:", chuoi_moi)
print("Da ghi vao file ketqua.txt")
