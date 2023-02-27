n = int(input())
arr =[[0 for i in range(100)] for i in range(100)]
result = 0

for i in range(n) :
    a, b = map(int, input().split(" "))
    for j in range(a-1, a+9) :
        arr[j][b-1:b+9] = [1 for k in range(10)]

for i in range(100) : 
    for j in range(100) :
        result += arr[i][j]

print(result)
