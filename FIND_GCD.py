a = int(input("nhap vao a:"))
b = int(input("nhap vao b:"))
UCLN=1
for i in range(1,a+1):
    if i>b:
        break
    if a%i==0 and b%i==0:
        UCLN=i
        print(UCLN)