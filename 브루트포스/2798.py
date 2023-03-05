N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

most = 0
for i in range(len(arr)) : 
    for j in range(i+1, len(arr)) :
        for k in range(j+1, len(arr)) :
            if most < (arr[i] + arr[j] + arr[k]) and (arr[i] + arr[j] + arr[k]) <= M :
                most = arr[i] + arr[j] + arr[k]

print (most)
