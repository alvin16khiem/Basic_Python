toan = float(input("so diem"))
van = float(input("so diem"))
anh = float(input("so diem"))
avg = (toan + van + anh)/3

if(0<=toan<=10 and 0 <= van <= 10 and 0 <= anh <= 10):
    if (avg>=8 and toan>=6.5 and van >=6.5 and anh>=6.5):
        print("hoc sinh gioi")
    elif (avg>=6.5 and toan>=5 and van >=5 and anh>=5):
        print("hoc sinh kha")
    elif (avg>=5 and toan>=3.5 and van >=3.5 and anh>=3.5):
        print("hoc sinh trung binh")
    else:
        print("rot mon")
else:
    print("nhap sai")