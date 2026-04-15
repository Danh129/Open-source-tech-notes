class SinhVien:
    def __init__(self, ma, ten, diem):
        self.ma = ma
        self.ten = ten
        self.diem = diem

    def hien_thi(self):
        print(f"{self.ma:<8}{self.ten:<15}{self.diem:<5}")


# ====== NHẬP DANH SÁCH ======
def nhap_ds(ds):
    n = int(input("Nhap so sinh vien: "))
    for _ in range(n):
        ma = input("Ma SV: ")
        ten = input("Ten SV: ")
        diem = float(input("Diem: "))
        ds.append(SinhVien(ma, ten, diem))


# ====== XUẤT DANH SÁCH ======
def xuat_ds(ds):
    print(f"{'Ma':<8}{'Ten':<15}{'Diem':<5}")
    for sv in ds:
        sv.hien_thi()


# ====== TÌM THEO TÊN ======
def tim_theo_ten(ds, ten):
    found = False
    for sv in ds:
        if sv.ten.lower() == ten.lower():
            sv.hien_thi()
            found = True
    if not found:
        print("Khong tim thay sinh vien")


# ====== TÌM THEO ĐIỂM ======
def tim_theo_diem(ds, diem):
    found = False
    for sv in ds:
        if sv.diem == diem:
            sv.hien_thi()
            found = True
    if not found:
        print("Khong tim thay sinh vien")


# ====== SẮP XẾP THEO ĐIỂM ======
def sap_xep_theo_diem(ds, giam=False):
    ds.sort(key=lambda sv: sv.diem, reverse=giam)


# ====== CHƯƠNG TRÌNH CHÍNH ======
def main():
    ds = []

    nhap_ds(ds)

    print("\nDanh sach ban dau:")
    xuat_ds(ds)

    print("\nSap xep diem TANG dan:")
    sap_xep_theo_diem(ds)
    xuat_ds(ds)

    print("\nSap xep diem GIAM dan:")
    sap_xep_theo_diem(ds, giam=True)
    xuat_ds(ds)

    print("\nTim sinh vien theo ten 'An':")
    tim_theo_ten(ds, "An")

    print("\nTim sinh vien co diem = 8:")
    tim_theo_diem(ds, 8)

if __name__ == "__main__":
    main()

