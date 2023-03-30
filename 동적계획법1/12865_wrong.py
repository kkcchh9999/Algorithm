#평범한 배낭

N, K = map(int, input().split())
arr = [[0,0]]
for i in range(N) : 
    arr.append(list(map(int, input().split())))
    
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1) : 
    for j in range(1, K+1) : 
        weight = arr[i][0]
        value = arr[i][1]
        
        if j < weight : 
            dp[i][j] = dp[i-1][j] 
        else :
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])

print(dp[-1][-1])


