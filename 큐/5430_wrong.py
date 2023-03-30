# AC
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for i in range(T) :  
    p = input() 
    n = int(input())
    try : 
        arr = deque(list(map(int, input().replace('[', '').replace(']', '').split(','))))
    except : 
        arr = [] 
    flag = False 
    
    re = 0
    for j in p : 
        if j == 'R' : 
           re += 1
        if j == 'D' : 
            try : 
                if re % 2 == 0 : 
                    arr.popleft() 
                else : 
                    arr.pop() 
            except : 
                flag = True
                break

    if flag : 
        print('error')
    else : 
        if re % 2 != 0 : 
            arr.reverse()
         
        print('[', end='')
        try : 
            for i in range(len(arr)-1) : 
                print(arr[i], end=',')
            print(arr[-1], end='')
        except : 
            pass 
        print(']')


