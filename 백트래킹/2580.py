arr = []
for i in range(9) : 
    arr.append(list(map(int, input().split())))

zero = []
for i in range(9) :
    for j in range(9) : 
        if arr[i][j] == 0 : 
             zero.append([i, j]) 

def horizon(x) : 
    tmparr = []
    zcount = 0 
    for i in range(9) : 
        tmparr.append(arr[x[0]][i])
        if arr[x[0]][i] == 0 :
            zcount += 1
    print(tmparr)
    print(zcount)

    if zcount == 1 : 
        for i in range(1, 10) : 
            if i not in tmparr : 
                print('hor  x : ', x, 'i: ', i)
                arr[x[0]][x[1]] = i 
                zero.remove(x)
                return 1
    return 0
    
def vertical(x) : 
    tmparr = []
    zcount = 0
    for i in range(9) : 
        tmparr.append(arr[i][x[1]])
        if arr[i][x[1]] == 0 : 
            zcount += 1 

    if zcount == 1 : 
        for i in range(1, 10) :
            if i not in tmparr :
                print('ver  x : ', x, 'i: ', i)
                arr[x[0]][x[1]] = i
                zero.remove(x)
                return 1
    return 0

def x3square(x) : 
    tmpX = x[0] // 3 
    tmpY = x[1] // 3 
    
    tmparr = []
    zcount = 0
    for i in range(tmpX*3, (tmpX+1)*3) : 
        for j in range(tmpY*3, (tmpY+1)*3) : 
            tmparr.append(arr[i][j]) 
            if arr[i][j] == 0 :
                zcount += 1 

    if zcount == 1 : 
        for i in range(1, 10) : 
            if i not in tmparr : 
                print('3x3  x : ', x, 'i: ', i)
                arr[x[0]][x[1]] = i 
                zero.remove(x)
                return 1 
    return 0
print()

while len(zero) > 0 : 
    for i in zero :
        flag = x3square(i)
        if flag == 0 : 
            flag = vertical(i)
        if flag == 0 : 
            flag = horizon(i)
for i in range(9) : 
    for j in range(9) : 
        print(arr[i][j], end = " ")
    print()
