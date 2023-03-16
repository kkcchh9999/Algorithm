n = int(input()) 
arr = []

maxX, maxY, indexX, indexY = 0, 0, 0, 0

for i in range(6) : 
    direction, length = map(int, input().split(' '))
    arr.append([direction, length])

for i in range(6) : 
    if arr[i][0] == 1 or arr[i][0] == 2 : 
        if arr[i][1] >= maxX : 
            maxX = arr[i][1]
            indexX = i
    else : 
        if arr[i][1] >= maxY :
            maxY = arr[i][1] 
            indexY = i

small_sqare = abs(arr[(indexX - 1) % 6][1] - arr[(indexX + 1) % 6][1]) * abs(arr[(indexY - 1) % 6][1] - arr[(indexY + 1) % 6][1]) 
big_sqare = maxX * maxY 

print((big_sqare - small_sqare) * n)
