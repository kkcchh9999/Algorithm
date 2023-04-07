# 최대 힘
import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n) : 
    x = int(input())

    # heap에 (-x, x) 삽입, heapq는 min heap 지원, 제일 작은게 앞으로
    # 3 1 5 삽입시 1 3 5로 정렬 
    # (-3,3) (-1,1) (-5,5) 삽입시 (-5,5) (-3,3) (-1,1) 로 정렬 

    if x : 
        hq.heappush(heap, (-x, x))
    else :
        if len(heap) >= 1 :
            print(hq.heappop(heap)[1]) 
        else : 
            print(0) 
