num = int(input())

ans = []

for i in range(num) : 
    abc = input().split(" ")
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    
    if (c % a) == 0 : 
        h = int(c / a)
        f = a 
    else : 
        f = c % a
        h = int(c / a) + 1

    ans.append((str(f) + str(h).zfill(2)))

for i in ans :
    print(i)
