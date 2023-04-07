# 파일 합치기
import heapq as hq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) : 
    pages = int(input())
    size = list(map(int, input().split()))
    hq.heapify(size)
    dp = [] 

    while len(size) > 1 : 
        tmp = hq.heappop(size) + hq.heappop(size) 
        print('tmp:', tmp, 'size:', size)
        dp.append(tmp)
        hq.heappush(size, tmp)
        print('size:', size)

    print(sum(dp))

