# 큐2
import sys
from collections import deque
input = sys.stdin.readline

queue = deque([])

N = int(input())
for i in range(N) : 
    op = input().strip()
    if op == 'front' : 
        try :
            print(queue[0])
        except : 
            print(-1)

    elif op == 'back' : 
        try : 
            print(queue[-1])
        except : 
            print(-1)

    elif op == 'size' : 
        print(len(queue))

    elif op == 'empty' : 
        if len(queue) == 0 : 
            print(1)
        else :
            print(0)

    elif op == 'pop' : 
        try : 
            print(queue.popleft())
        except : 
            print(-1)

    else : 
        queue.append(int(op.split()[1]))


