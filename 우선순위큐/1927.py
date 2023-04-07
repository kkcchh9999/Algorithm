# 최소 힙

import heapq as hq
import sys
input = sys.stdin.readline

heap = [] 
n = int(input())
for _ in range(n) : 
    num = int(input()) 

    if num : 
        hq.heappush(heap, num)
    else : 
        if len(heap) > 0 : 
            print(hq.heappop(heap))
        else :
            print(0)
