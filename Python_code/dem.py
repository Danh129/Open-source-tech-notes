#Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.
s=input("nhap vao chuoi:")

demhoa=0
demthuong=0

for c in s:
    if c.isupper():
        demhoa+=1
    elif c.islower():
        demthuong+=1
    else:
        pass

print("Dem chu hoa:", demhoa)
print("Dem chu thuong:", demthuong)