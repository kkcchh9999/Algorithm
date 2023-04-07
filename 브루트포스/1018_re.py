N, M = map(int, input().split())
chess = [input() for _ in range(N)]

answer = 64
for i in range(N - 7) : 
    for j in range(M - 7) : 
        
        wstart = 0
        bstart = 0
        for k in range(i, i+8) : 
            for l in range(j, j+8) : 
                if (k + l) % 2 == 0 :
                    if chess[k][l] == 'W' : 
                        wstart += 1
                    else : 
                        bstart += 1
                else : 
                    if chess[k][l] == 'W' : 
                        bstart += 1
                    else : 
                        wstart += 1 

        answer = min(wstart, bstart, answer) 

print(answer)
