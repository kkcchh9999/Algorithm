import math 

T = int(input()) 

for i in range(T) : 
    x1, y1, x2, y2 = map(int, input().split(' '))
    n = int(input()) 
    cnt = 0
    for i in range(n) : 
        cx, cy, r = map(int, input().split(' '))
        
        distance_start = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
        distance_end = math.sqrt((x2 - cx) ** 2 + (y2 - cy) ** 2) 

        if distance_start < r and distance_end > r : 
            cnt += 1 
        elif distance_start > r and distance_end < r : 
            cnt += 1
    
    print(cnt)

