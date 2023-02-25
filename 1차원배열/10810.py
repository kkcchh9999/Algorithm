NM = input().split()
N = int(NM[0])
M = int(NM[1])
arr = [0 for i in range(N)]

for l in range(M) : 
    ijk = input().split(" ") 
    i = int(ijk[0])
    j = int(ijk[1])
    k = int(ijk[2]) 

    for m in range(i-1, j) : 
        arr[m] = k

for i in range(len(arr)) : 
    print(arr[i], end=" ")
