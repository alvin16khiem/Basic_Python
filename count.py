a = int(input("nhap vao a:"))
k=10
count=1
while a >= k:  # lap lai den khi nao dieu kien dung
    k *= 10  # neu input a = 200 , 10 * 10 * 10 (3)
    count += 1 # => 1+1+1
print(count)