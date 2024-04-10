a = float(input("nhap vao a:"))
b = float(input("nhap vao b:"))
c = float(input("nhap vao c:"))

if(a+b>c and b+c>a and a+c>b):
    if(a==b==c):
        print("tam giac deu")
    elif(a==b or b==c or c==b):
        print("tam giac can")
    elif(a**2==b**2+c**2 or a**2+b**2==c**2 or b**2==a**2+c**2):
        print("tam giac vuong")
    else:
        print("khong phai tam giac")
else:
    print("khong phai tam giac")