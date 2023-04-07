# 소수

def isPrime(n) : 
    if n == 1 : 
        return False 

    flag = True 
    for i in range(2, n) : 
        if n % i == 0 :
            flag = False
            break

    return flag 

    
M = int(input())
N = int(input())

prime = []

for i in range(M, N+1) : 
    if isPrime(i) : 
        prime.append(i)

if len(prime) == 0 : 
    print(-1)
else : 
    print(sum(prime))
    print(prime[0])
