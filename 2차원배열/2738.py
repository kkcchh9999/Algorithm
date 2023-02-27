n, m = map(int, input().split(" "))
A = []
B = []

for i in range(n) :
    M = list(map(int, input().split(" ")))
    A.append(M)

for i in range(n) :
    M = list(map(int, input().split(" ")))
    B.append(M)

for i in range(n) :
    for j in range(m) : 
        print(A[i][j] + B[i][j], end = " ")
    print()

