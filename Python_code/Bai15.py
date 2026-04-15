def remove_dupplicate(arr):
    result = []
    for ch in arr:
        if ch not in result:
            result.append(ch)
    return result

print ("nhap ki tu (nhap ' 'de dung) ")

chars = []
while True:
    a=input(" nhap ki tu: ")
    if a == ' ':
        break
    chars.append(a)

print(f"Danh sach ban dau", chars)

uni_char = remove_dupplicate(chars)
print(f"Danh sach sau khi loai bo trung lap", uni_char)