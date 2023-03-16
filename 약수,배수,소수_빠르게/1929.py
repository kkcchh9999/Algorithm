m, n = map(int, input().split(' '))

arr = [True for i in range(n + 1)]

arr[0], arr[1] = False, False

for i in range(2, len(arr)) : 
    if arr[i] == True : 
        n = 2
        while i * n < len(arr) :
            arr[i * n] = False
            n += 1 

for i in range(m, len(arr)) : 
    if arr[i] == True : 
        print(i) 
