# 행렬 제곱
import sys
input = sys.stdin.readline

N, B = map(int, input().split())
arr = []
for i in range(N) : 
    arr.append(list(map(int, input().split())))

def mul(N, a, b) : 
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N) : 
        for j in range(N) : 
            for k in range(N) : 
                result[i][j] += a[i][k] * b[k][j]
            result [i][j] %= 1000

    return result 

def DnC(N, b, A) : 
    if b == 1 : 
        for i in range(N) : 
            for j in range(N) : 
                A[i][j] %= 1000
        return A
    elif b == 2 : 
        return mul(N, A, A)
    else : 
        temp = DnC(N, b // 2, A) 
        
        if b % 2 == 0 : 
            return mul(N, temp, temp)
        else : 
            return mul(N, mul(N, temp, temp), A)

result = DnC(N, B, arr) 

for i in result : 
    print(*i)
   

