N = int(input())
tmp = N 
for i in range(2, tmp+1) : 
    while N % i == 0 : 
        print(i) 
        N /= i
