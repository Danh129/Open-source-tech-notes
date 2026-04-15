#tinh tuoi dua theo ngay thang nam sinh
#Sử dụng module datetime. Sử dụng datetime, chúng ta có thể tìm tuổi bằng cách trừ năm sinh cho năm hiện tại

import datetime
while True:
    ngay=int(input("Nhap ngay sinh: "))
    thang=int(input("Nhap thang sinh: "))
    nam=int(input("Nhap nam sinh: "))

# lay thong tin hien tai cua ngay thang nam
    current_ngay=datetime.date.today().day
    current_thang=datetime.date.today().month
    current_nam=datetime.date.today().year

    age_nam= current_nam-nam
    age_thang= current_thang - thang
    age_ngay= current_ngay - ngay

    print(f"Tuoi cua ban la: {age_nam} nam {age_thang} thang {age_ngay} ngay")