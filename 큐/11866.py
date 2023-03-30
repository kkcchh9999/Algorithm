# 요세푸스 문제0
from collections import deque

N, K = map(int, input().split())

queue = deque([]) 
result = [] 
for i in range(1, N+1) : 
    queue.append(i) 

while len(queue) > 0 : 
    for i in range(K-1) : 
        queue.append(queue.popleft())
    result.append(queue.popleft())

print('<', end = '')
for i in range(len(result)-1) : 
    print(result[i], end = ', ')

print('%d>' %result[-1])

