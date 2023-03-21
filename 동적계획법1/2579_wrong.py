n = int(input())

arr = []
for i in range(n) : 
    arr.append(int(input()))

if n <= 2 : 
    ans = 0
    for i in arr : 
        ans += i 
    print(ans)
    exit()

dp = []
dp.append(arr[0])
dp.append(arr[0] + arr[1]) 
dp.append(max(arr[1] + arr[2], arr[0] + arr[2]))

for i in range(3, n) : 
    dp.append(max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i]))
print(dp[n-1])
