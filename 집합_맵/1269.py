n, m = map(int, input().split(" ")) 
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

answer = {} 
for i in range(n) :
    answer[A[i]] = i

for i in range(m) : 
    if B[i] not in answer : 
        answer[B[i]] = i 
    else : 
        del(answer[B[i]])

print(len(answer))
