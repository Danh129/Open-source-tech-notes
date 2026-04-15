min=int(input("Nhap so nho nhat: "))
max=int(input("Nhap so lon nhat: "))

numbers=list(range(min, max + 1))

chiahet=list(filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers))

tong = sum(chiahet)

print (f" Cac so chia het cho 3 va 5 {min} den {max} : {chiahet} ")
print (f"ket qua", tong)

