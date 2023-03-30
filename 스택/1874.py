# 스택 수열
import sys
input = sys.stdin.readline

cnt = 1
stack = []
flag = True
op = [] 

n = int(input())
for i in range(n) : 
    target = int(input())
    while cnt <= target : 
        stack.append(cnt)
        cnt += 1 
        op.append('+')

    if stack[-1] == target : 
        stack.pop()
        op.append('-') 

    else : 
        flag = False 
        break

if flag == False : 
    print('NO')

else : 
    for i in op : 
        print(i) 


