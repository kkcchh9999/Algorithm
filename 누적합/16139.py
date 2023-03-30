# 인간-컴퓨터 상호작용
import sys
input = sys.stdin.readline

S = input()
q = int(input())
arr = [[0] * (len(S) + 1) for i in range(26)]

for j in range(26) : 
    for i in range(1, len(S) + 1) : 
        if S[i-1] == chr(97+j) : 
            arr[j][i] = arr[j][i-1] + 1
        else : 
            arr[j][i] = arr[j][i-1] 

for i in range(q) :    
    alpha, start, end = input().split(' ')
    print(arr[ord(alpha)-97][int(end)+1] - arr[ord(alpha)-97][int(start)])


