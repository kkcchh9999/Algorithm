n = int(input())
narr = list(map(int, input().split(' ')))
m = int(input())
marr = list(map(int, input().split(' ')))

have = {}
for i in narr :
    if i not in have : 
        have[i] = 1 
    else : 
        have[i] += 1 

for i in marr : 
    if i in have : 
        print(have[i], end=" ")
    else : 
        print(0, end = " ")
