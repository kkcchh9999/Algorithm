n, m = map(int, input().split(" "))
S = {} 
M = {}
for i in range(n) :
    S[input()] = 1

cnt = 0 
for i in range(m) :
    if input() in S : 
        cnt += 1 

print(cnt) 

