n = int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(n)]
dp_re = [1 for i in range(n)]
for i in range(n) : 
    for j in range(i) : 
        if arr[i] > arr[j] : 
            dp[i] = max(dp[i], dp[j]+1)

for i in range(n-1, -1, -1) : 
    for j in range(n-1, i, -1) : 
        if arr[i] > arr[j] : 
            dp_re[i] = max(dp_re[i], dp_re[j]+1) 

for i in range(n) : 
    dp[i] = dp[i] + dp_re[i] 

print(max(dp) - 1)
