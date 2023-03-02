n = int(input())

arr = []
for i in range(n) :
    arr.append(input()) 

arr = list(set(arr))

arr1 = sorted(arr, key = lambda x : (len(x), x))

for i in arr1 :
    print(i)
