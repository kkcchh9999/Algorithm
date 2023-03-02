n = 5
arr = []
for i in range(n) :
    k = int(input())
    arr.append(k) 

arr = sorted(arr) 
add = 0
for i in arr : 
    add += i

print (add // 5) 
print (arr[2])
