n, m = map(int, input().split(" "))

arr = [i+1 for i in range (n)]

for k in range(m) : 
    i, j = map(int, input().split(" "))
    tmp = arr[i-1:j]
    tmp.reverse()
    arr[i-1:j] = tmp    

for i in arr :
    print(i, end = " ") 
