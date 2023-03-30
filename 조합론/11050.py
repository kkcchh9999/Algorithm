# 이항 계수1 
import math

N, K = map(int, input().split())

nfac = 1
for i in range(1, N+1) : 
    nfac *= i 

rfac = 1
for i in range(1, K+1) : 
    rfac *= i 

n_min_rfac = 1
for i in range(1, N - K + 1) : 
    n_min_rfac *= i

print(nfac // (rfac * n_min_rfac))
