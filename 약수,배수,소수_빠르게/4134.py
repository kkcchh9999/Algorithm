import math

def isPrime(k) : 
    if k == 0 or k == 1 : 
        return False 

    for i in range(2, int(math.sqrt(k)) + 1) : 
        if k % i == 0 : 
            return False 

    return True

n = int(input())

for i in range(n) : 
    k = int(input())

    while True : 
        if isPrime(k) == True : 
            print(k) 
            break
        else : 
            k += 1 


