#Viết chương trình nhập: số giờ làm mỗi tuần, thù lao trên mỗi giờ làm tiêu chuẩn, 
# từ đó tính ra số tiền thực lĩnh của nhân viên. 
# Biết rằng: số giờ tiêu chuẩn mỗi tuần là 44 giờ, và mỗi giờ vượt chuẩn được trả gấp rưỡi so với giờ làm chuẩn.

so_gio_lam=float(input("Nhap so gio ban lam duoc: "))
luong_gio=float(input("Nhao luong theo gio(vd 23k/h: nhap 23): "))

gio_tieu_chuan=44
gio_vuot_chuan=max(0,so_gio_lam - gio_tieu_chuan)
luong=gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5

print(f"tonng luong ban lam duoc la:", luong)
