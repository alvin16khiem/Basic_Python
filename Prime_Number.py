#Prime number
a = int(input("nhap so a:"))
if(a > 1):
    count = 0
    for i in range(1,a+1):
        if(a % i ==0):
            count+=1
    if count == 2:
        print(a,"la so nguyen")
    else:
        print(a,"khong phai la so nguyen")

else:
    print(a,"khong la so nguyen")