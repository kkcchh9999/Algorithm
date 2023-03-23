arr = [list(map(int,input().split())) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]

def is_available(i, j) : 
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

    for x in range(9) : 
        if arr[x][j] in nums : 
            nums.remove(arr[x][j])
        if arr[i][x] in nums : 
            nums.remove(arr[i][x])

    tmpi = i//3 
    tmpj = j//3 
    for x in range(tmpi * 3, (tmpi+1) * 3) : 
        for y in range(tmpj * 3, (tmpj+1) * 3) : 
            if arr[x][y] in nums : 
                nums.remove(arr[x][y])

    return nums 

def dfs(a) : 
    
    if a == len(zero) :
        for i in arr : 
            print(*i)
        exit()
    else : 
        (i, j) = zero[a] 
        nums = is_available(i, j)

        for x in nums : 
            arr[i][j] = x 
            dfs(a+1) 
            arr[i][j] = 0 

dfs(0)

