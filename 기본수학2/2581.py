def isPrime(a: int, z: int) : 
    prime = []
    switch = 0
    for i in range(a, z+1) : 
        if i == 1 : 
            switch = 1

        for j in range(2, i) :
            if i % j == 0 : 
                switch = 1
                
        if switch == 0 : 
            prime.append(i)  
        switch = 0
    
    print(prime)
    return prime

a = int(input())
z = int(input())

arr = isPrime(a, z)
if len(arr) == 0 : 
    print(-1)
else :
    print(sum(arr))
    print(arr[0])

