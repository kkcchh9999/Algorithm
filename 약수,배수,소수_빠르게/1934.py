T = int(input())

answer = []
for i in range(T) :
    a, b = map(int, input().split(' '))
    
    minx = 1 
    if a >= b : 
        for i in range(b, 0, -1) : 
            if a % i == 0 and b % i == 0 : 
                minx = i 
                break;
    elif b > a : 
        for i in range(a, 0, -1) : 
            if a % i == 0 and b % i == 0 : 
                minx = i 
                break;

    print(a * b // minx) 
            
