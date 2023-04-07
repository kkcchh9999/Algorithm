# 오큰수

from collections import deque as dq

N = int(input())
A = list(map(int, input().split()))

big = A[-1] 
stack = [A[-1]]
answer = [-1]

for i in range(N-2, -1, -1) : 
    if i > big : 
        big = i 
        answer.append(-1)
        stack.append(i)
    else : 
        if stack[-1] > i : 
            answer.append(stack[-1])
            stack.append(i) 
        else : 
            stack.pop()
            answer.append(stack[-1])
            stack.append(i)

print(answer)
