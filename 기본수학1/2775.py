loop = int(input())

for i in range(loop) : 
    k = int(input())
    n = int(input())
    underflore = list(range(1, n+1))

    for j in range(k) :
        kflore = [] 
        for q in range(n) :
            kflore.append(sum(underflore[0:q+1]))
        underflore = kflore.copy()

    print(underflore[n-1])
