# 덱
import sys 
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([])

for i in range(n) : 
    op = input().strip()
    
    if op == "pop_front" : 
        try : 
            print(queue.popleft())
        except : 
            print(-1) 
            
    elif op == "pop_back" : 
        try :
            print(queue.pop())
        except :
            print(-1) 

    elif op == "size" : 
        print(len(queue))
    
    elif op == "empty" :
        if len(queue) == 0 :
            print(1)
        else : 
            print(0)
    
    elif op == "front" : 
        try : 
            print(queue[0]) 
        except : 
            print(-1)

    elif op == "back" : 
        try :
            print(queue[-1])
        except : 
            print(-1)

    elif "push_front" in op : 
        queue.appendleft(op.split()[1])

    elif "push_back" in op : 
        queue.append(op.split()[1]) 

                
