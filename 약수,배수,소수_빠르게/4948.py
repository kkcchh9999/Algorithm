import math
import sys
input = sys.stdin.readline

arr = [True for i in range(123456 * 2 + 1)]
arr[0], arr[1] = False, False

for i in range(2, int(math.sqrt(123456 * 2) + 1)) : 
    if arr[i] == True : 
        j = 2
        while i * j < 123456*2 + 1 : 
            arr[i * j] = False 
            j += 1 

while True : 
    n = int(input())

    if n == 0 : 
        break

    cnt = 0
    for i in range(n+1, (2 * n) + 1) : 
        if arr[i] == True : 
            cnt += 1

    print(cnt) 
    
