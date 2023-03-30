import sys
input = sys.stdin.readline

n = int(input())
a = [] 
for i in range(n) : 
    a.append(list(map(int,input().split())))

a.sort(key = lambda x : x[0])

dp = [1] * n 
for i in range(n) :
    for j in range(i) : 
        if a[i][1] > a[j][1] : 
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

