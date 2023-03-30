# 괄호

T = int(input())

arr = []
for i in range(T) : 
    test = input()
    cnt = 0
    for i in test : 
        if i == '(' : 
            cnt += 1
        else : 
            cnt -= 1
        
        if cnt < 0 : 
            break
    if cnt == 0 : 
        print('YES')
    else : 
        print('NO')


