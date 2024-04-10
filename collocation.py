#8 5 6
#5 8 6
#5 6 8

a = float(input("nhap vao a:"))
b = float(input("nhap vao b:"))
c = float(input("nhap vao c:"))
if(a>b):
    a,b = b,a
if(b>c):
    b,c = c,b
print(a,b,c)