# 피보나치 수 6

mod = 1000000007
n = int(input())

def mul(arr, arr2) : 
    n = len(arr) 
    result = [[0 for _ in range(n)] for _ in range(n)]

    for row in range(n) : 
        for col in range(n) : 
            for i in range(n) : 
                result[row][col] += arr[row][i] * arr2[i][col] 
            result[row][col] %= mod 

    return result 

def DnC(arr, time) : 
    if time == 1 : 
        for i in range(len(arr)) : 
            for j in range(len(arr)) : 
                arr[i][j] %= mod
        return arr 

    tmp = DnC(arr, time//2) 
    if time % 2 : 
        return mul(mul(tmp, tmp), arr)
    else : 
        return mul(tmp, tmp) 

fib_matrix = [[1, 1], [1, 0]]
print(DnC(fib_matrix, n)[0][1])
