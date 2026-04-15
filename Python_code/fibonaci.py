def is_fibonacci(n):
    if n < 0:
        return False

    a= 0
    b=1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False


n = int(input("Nhập số: "))
if is_fibonacci(n):
    print(n, "là số Fibonacci")
else:
    print(n, "không phải là số Fibonacci")
