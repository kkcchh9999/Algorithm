# 스택
import sys
input = sys.stdin.readline

N = int(input())

stack = []

for i in range(N) : 
    oper = input().strip()
    if oper == 'top' : 
        try : 
            print(stack[-1]) 
        except : 
            print(-1)
    elif oper == 'pop' : 
        try : 
            print(stack.pop())
        except : 
            print(-1)
    elif oper == 'size' : 
        print(len(stack))
    elif oper == 'empty' : 
        if len(stack) == 0 : 
            print(1)
        else : 
            print(0)
    else : 
        stack.append(int(oper.split()[1]))

