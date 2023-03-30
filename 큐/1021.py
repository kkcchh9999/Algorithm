# 회전하는 큐 
from collections import deque

N, M = map(int, input().split())
Lqueue = deque([i for i in range(1, N+1)])
Rqueue = deque([i for i in range(1, N+1)]) 

target = list(map(int, input().split()))
cnt = 0

for i in target : 
    pop_left = 0
    pop_right = 0
    
    for j in range(len(Lqueue)) : 
        if Lqueue[0] == i : 
            Lqueue.popleft() 
            break
        else :
            Lqueue.append(Lqueue.popleft())
            pop_left += 1

    for j in range(len(Rqueue)) :
        if Rqueue[0] == i :
            Rqueue.popleft()
            break
        else : 
            Rqueue.appendleft(Rqueue.pop())
            pop_right += 1

    cnt += min(pop_left, pop_right)

print(cnt)
