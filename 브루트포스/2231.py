N = int(input())

result = 0
for i in range(1, N+1) :
    A = list(map(int, str(i)))
    result = i + sum(A)

    if result == N : 
        print(i) 
        exit()

print(0)

