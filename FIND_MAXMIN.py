n = int(input("nhap vao n:"))
Max = None
Min = None
while n != -1:
    if Max == None or Max < n:
        Max = n
    if Min == None or Min > n:
        Min = n
    n = int(input("nhap vao n:"))
print("MAX :",Max)
print("Min :",Min)

