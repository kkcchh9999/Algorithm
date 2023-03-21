n = int(input())
arr = [] 
for i in range(n) : 
    arr.append(list(map(int, input().split())))

if n == 1 : 
    print(arr[0][0])
else : 
    for i in range(n-2, -1, -1) : 
        for j in range(i+1) :
            try : 
                arr[i][j] = max(arr[i+1][j], arr[i+1][j+1]) + arr[i][j]
            except :     
                arr[i][j] = arr[i+1][j] + arr[i][j]

    print(arr[i][j])
