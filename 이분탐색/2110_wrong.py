# 공유기 설치

N, C = map(int, input().split())
position = sorted([int(input()) for _ in range(N)]) 

start, end = 1, position[-1] - position[0]

while start <= end : 
    mid = (start + end) // 2

    cnt = 1
    last_station = position[0] 
    for i in position : 
        if i - last_station >= mid : 
            cnt += 1 
            last_station = i 

    if cnt >= C :
        start = mid + 1
    else : 
        end = mid - 1

print(end) 
        


