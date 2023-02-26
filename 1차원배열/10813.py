nm = input().split(" ")
n = int(nm[0])
m = int(nm[1]) 

arr = [i for i in range(1, n+1)]

for k in range(m) :
    ij = input().split(" ")
    i = int(ij[0])-1
    j = int(ij[1])-1
    
    tmp1 = arr[j]
    arr[j] = arr[i]
    arr[i] = tmp1
    
for i in arr :
    print(i, end = " ")

