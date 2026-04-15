import random
def remove_all(arr, x):
    return [num for num in arr if num != x]

n=int(input("nhap so luong: "))

arr=[random.randint(1, 999) for _ in range(n)]

print ("Danh sach ban dau", arr)

x=int(input("Nhap gia tri can xoa: "))

arr=remove_all(arr, x)
print ("Danh sach sau khi xoa: ", arr)