import math

arr = [True for i in range(10001)] 
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(10000) + 1)) : 
    if arr[i] == True : 
        j = 2;

        while i * j <= 10000 : 
            arr[i * j] = False
            j += 1

    
k = int(input())
 
for re in range(k) :
    n = int(input())
    a = n//2
    b = n//2

    while a > 0 : 
        if arr[a] and arr[b] : 
            print(a, b) 
            break 
        else : 
            a -= 1 
            b += 1
