# 제로
import sys
input = sys.stdin.readline

K = int(input())

arr = []
for i in range(K) : 
    num = int(input().strip())
    if num == 0 : 
        arr.pop()
    else : 
        arr.append(num) 

print(sum(arr))
