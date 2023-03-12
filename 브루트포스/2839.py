n = int(input()) 

if n % 5 == 0 : 
    print(n // 5) 
    exit()
elif n % 5 == 3 : 
    print(n // 5 + 1)
    exit()
else : 
    for i in range(1, n//5 + 1) : 
        div = (n // 5) - i 
        rest = n % 5 + i * 5
        if rest % 3 == 0 :
            print(div + (rest // 3))
            exit()

print(-1)

    
    
