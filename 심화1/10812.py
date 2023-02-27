n, m = map(int, input().split(" "))

arr = [i+1 for i in range(n)]

for i in range(m) : 
    i, j, k = map(int, input().split(" "))
    begin = arr[i-1:k-1]
    end = arr[k-1: j]
    arr[i-1:j] = end+begin

for i in arr :
    print(i, end=" ")
