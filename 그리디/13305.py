# 주유소
import sys
input = sys.stdin.readline

N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

cnt = length[0] * price[0] 
min_price = price[0]

for i in range(1, N-1) : 
    if min_price > price[i]: 
        min_price = price[i] 

    cnt += min_price * length[i] 

print(cnt) 

