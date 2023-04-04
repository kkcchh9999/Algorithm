# 랜선 자르기 

K, N= map(int, input().split())
size = [int(input()) for _ in range(K)]

start, end = 1, max(size)

while start <= end : 
    mid = (start + end) // 2
    lines = 0

    for i in size : 
        lines += i // mid 

    if lines >= N : 
        start = mid + 1 
    else : 
        end = mid - 1

print(end) 

