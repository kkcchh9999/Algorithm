#나머지 합
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Narr = list(map(int, input().split()))

SUM = 0
mod = [0] * M

for i in range(N) : 
    SUM += Narr[i] 
    mod[SUM % M] += 1

result = mod[0] 

for i in mod : 
    result += i * (i-1) // 2 

print(result)
