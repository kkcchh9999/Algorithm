import math

t = int(input())
for i in range(t) : 
    n = int(input())
    
    arr = [True for i in range(n)]
    arr[0] = False
    arr[1] = False
    
    
    for j in range(2, int(math.sqrt(n))+1) : 
        if arr[j] == True : 
            k = 2
            
            while j * k < n : 
                arr[j * k] = False
                k += 1;
   
    prime = []
    for j in range(n) : 
        if arr[j] == True :
            prime.append(j) 
    
    ans = []
    for j in range(len(prime)) :
        for k in prime[j: ] :
            if prime[j] + k == n : 
                ans.append([prime[j], k, k-j])
    tmp = 10000
    answer = []
    for j in ans : 
        if tmp > j[2] : 
            tmp = j[2] 
            answer = j

    print("%d %d" %(answer[0], answer[1]))
