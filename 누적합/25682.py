# 체스판 다시 칠하기2
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = []
for i in range(N) : 
    board.append(input())

Bstart = [[0] * (M + 1) for _ in range(N + 1)] 
Wstart = [[0] * (M + 1) for _ in range(N + 1)] 

for i in range(1, N+1) : 
    for j in range(1, M+1) : 
        if (i + j) % 2 == 0 : 
            if board[i-1][j-1] == 'B' : 
                Wstart[i][j] = Wstart[i-1][j] + Wstart[i][j-1] - Wstart[i-1][j-1] + 1
                Bstart[i][j] = Bstart[i-1][j] + Bstart[i][j-1] - Bstart[i-1][j-1]
            if board[i-1][j-1] == 'W' : 
                Bstart[i][j] = Bstart[i-1][j] + Bstart[i][j-1] - Bstart[i-1][j-1] + 1
                Wstart[i][j] = Wstart[i-1][j] + Wstart[i][j-1] - Wstart[i-1][j-1]

        else : 
            if board[i-1][j-1] == 'W' : 
                Wstart[i][j] = Wstart[i-1][j] + Wstart[i][j-1] - Wstart[i-1][j-1] + 1
                Bstart[i][j] = Bstart[i-1][j] + Bstart[i][j-1] - Bstart[i-1][j-1]               
            if board[i-1][j-1] == 'B' : 
                Bstart[i][j] = Bstart[i-1][j] + Bstart[i][j-1] - Bstart[i-1][j-1] + 1
                Wstart[i][j] = Wstart[i-1][j] + Wstart[i][j-1] - Wstart[i-1][j-1]
result1 = K**2

for i in range(1, N-K+2) : 
    for j in range(1, M-K+2) :
        x = i + K - 1
        y = j + K - 1
        
        minW = Wstart[x][y] - Wstart[i-1][y] - Wstart[x][j-1] + Wstart[i-1][j-1]
        minB = Bstart[x][y] - Bstart[i-1][y] - Bstart[x][j-1] + Bstart[i-1][j-1]

        result1 = min(result1, minW, minB)

print(result1)



