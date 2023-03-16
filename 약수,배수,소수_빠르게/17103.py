import math

arr = [True for i in range(1000000 * 2 + 1)] 
arr[0], arr[1] = False, False 
for i in range(2, int(math.sqrt(1000000 * 2)) + 1) : 
    if arr[i] == True : 
        j = 2
        while j * i < 1000000 * 2 + 1 : 
            arr[i * j] = False
            j += 1 

T = int(input())
for i in range(T) :
    N = int(input()) 
    
    if (N == 4) :
        print(1)
    else : 
        cnt = 0
        for i in range(1, N // 2 + 1, 2) :
            if arr[i] == True and arr[N - i] == True : 
                cnt += 1
        print (cnt) 
