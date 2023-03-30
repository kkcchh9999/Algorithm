#구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

table = [0]
temp = 0
for i in arr :
    temp += i 
    table.append(temp)
        

for i in range(M) : 
    start, end = map(int, input().split())
    
    print(table[end]-table[start-1])
