n, m = map(int, input().split(' '))

s = [] 

def dfs() : 
    flag = True 
    for i in range(len(s) - 1) : 
        if s[i] >= s[i+1] :
            flag = False 

    if len(s) == m and flag == True: 
        print(' '.join(map(str,s)))
        return 
    
    for i in range(1, n+1): 
        if i not in s : 
            s.append(i) 
            dfs()
            s.pop() 

dfs()


