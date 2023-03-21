n = int(input())
arr = []
for i in range(n) : 
    arr.append(int(input()))

if n <= 2 : 
    res = 0
    for i in arr : 
        res += i
    print(res)
    exit()
dp = []
dp.append(arr[0])
dp.append(arr[0]+arr[1])
dp.append(max(arr[2]+arr[1], arr[0]+arr[2], dp[1]))

for i in range(3, n) : 
    dp.append(max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1]))

print(dp[n-1])
