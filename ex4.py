# 1+2+3+...k but k(max)<n
n = int(input("nhap vao n:"))
S=0
K=1
while S < n:
    S += K # 1 3 6 10
    K += 1 # 2 3 4 5
print(K-2)