import math

T = int(input())

for i in range(T) : 
    x1, y1, r1, x2, y2, r2 = map(int, input().split(' '))

    #두 원 사이의 거리 
    distance = math.sqrt(((x2-x1)**2 + (y2-y1)**2))

    #두 원의 중심 일치, 반지름이 같음 
    if distance == 0 and r1 == r2 : 
        print(-1)
    #내접 or 외접
    elif r1 + r2 == distance or abs(r1 - r2) == distance :
        print(1)
    #두 점에서 만날때 
    elif abs(r1 - r2) < distance < r1 + r2 :
        print(2)
    #이외의 경우 
    else :
        print(0) 



