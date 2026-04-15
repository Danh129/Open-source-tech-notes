#Viết chương trình Python nhập một dãy số nguyên, sau đó kiểm
#  tra xem nó có khả đối xứng không? Nếu có, hãy biến đổi nó để được một dãy đối xứng.

#Gợi ý:

#Bạn có thể dùng hàm kiem_tra_doi_xung để kiểm tra tính đối xứng của dãy
#  số bằng cách so sánh dãy số ban đầu với dãy số đảo ngược. Nếu chúng bằng nhau, dãy số là đối xứng.
#Nếu dãy số chưa đối xứng, hãy thử dùng hàm sx_doi_xung để biến đổi dãy số thành dãy số 
# đối xứng: bằng cách điều chỉnh giá trị của một phần tử ở một vị trí sao cho nó khớp với phần tử đối xứng của nó.

def ktradoixung(s):
    #s = s.lower().replace(" ", "")
    return s == s[::-1]

def sxdoixung(s):
    n=len(s)
    new_s=s[:]
    for i in range(n // 2):
        if new_s[i] != new_s[-i-1]:
            new_s[i]=new_s[-i-1]
    return new_s
    
#nhap cach ra: vd: 1 2 3 4 5 
s=list(map(int, input("nhap day can kiem tra:").split()))

if ktradoixung(s):
    print(s, "la so doi xung")
else:
    daydoixung=sxdoixung(s)
    if ktradoixung(daydoixung):
        print("Co kha nang sap xep doi xung va bien thanh day doi xung:", daydoixung)
    else:   
        print("khong phai la so doi xung")