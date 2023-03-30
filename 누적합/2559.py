# 수열

N, K = map(int,input().split())
temp = list(map(int, input().split()))

tmp = 0
for i in range(K) : 
    tmp += temp[i] 

big = tmp
for i in range(K, N) : 
    tmp += temp[i]
    tmp -= temp[i-K]

    if tmp > big : 
        big = tmp 

print(big) 
