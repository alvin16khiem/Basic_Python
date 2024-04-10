a = float(input("nhap vao a:"))
b = float(input("nhap vao b:"))
c = float(input("nhap vao c:"))
delta = b**2 - 4*a*c
print("can bac 2:" + str(a) + "x^2+" + str(b) + "x+" +str(c))
if (a==0):
        if (b==0):
            if (c==0):
                print("vo so nghiem")
else:
        if (delta>0):
            print("se co 2 nghiem phan biet")
        elif (delta==0):
            print("phuong trinh co nghiem kep")
        else:
            print("khong co nghiem")

