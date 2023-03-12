import sys
input = sys.stdin.readline

n = int(input())
narr = list(map(int, input().split(' ')))
m = int(input())
marr = list(map(int, input().split(' ')))

answer = {}
for i in range(n) : 
    answer[narr[i]] = 1

for i in range(m) : 
    if marr[i] in answer : 
        print(1, end = " ")
    else : 
        print(0, end = " ")
