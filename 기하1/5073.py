while True :
    a, b, c = map(int, input().split())
    if a == b == c == 0 :
        break
    if a == b == c :
        print('Equilateral')
    elif max(a, b, c) >= a+b+c - max(a,b,c) : 
        print('Invalid')
    elif a == b or b == c or c == a :
        print('Isosceles')
    else : 
        print('Scalene')
