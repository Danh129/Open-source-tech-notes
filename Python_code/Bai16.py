import random
def rotate_right(arr, k):
    n=len(arr)
    if n == 0:
        return arr
    k = k % n

#thuc hien xoay phai
    return arr[-k:] + arr[:-k]


def rotate_left(arr, k):
    n=len(arr)
    if n == 0:
        return arr
    k = k % n

#thuc hien xoay trai
    return arr[k:] + arr[:k]


n=int(input("Nhap do dai: "))
arr=[random.randint(1, 99) for _ in range(n)]
print("Danh sach ban dau", arr)

k=int(input("Nhap so vi tri k: "))
kq1=rotate_right(arr, k)
kq2=rotate_left(arr, k)

print(f"Danh sach sau khi xoay phai: ", kq1)
print(f"Danh sach sau khi xoay trai: ", kq2)