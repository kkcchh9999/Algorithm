# 프린터 큐
from collections import deque

N = int(input())
for i in range(N) : 
    n, m = map(int, input().split())
    val = deque(list(map(int, input().split())))
    cnt = 0 

    queue = deque([]) 
    for j in range(n) : 
        queue.append(j)
    
    queue[m] = -1
    
    while -1 in queue : 
        
        for j in range(len(val)) : 
            if val[0] != max(val) : 
                val.append(val.popleft())
                queue.append(queue.popleft()) 

            else : 
                val.popleft()
                queue.popleft() 
                cnt += 1
                break
        
    print(cnt)
        

    
    

