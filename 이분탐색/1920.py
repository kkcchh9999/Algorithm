# 수 찾기

n = int(input())
arr = {}
for i in list(map(int, input().split())) : 
    arr[i] = 1

m = int(input())
for i in list(map(int, input().split())) : 
    if i in arr : 
        print(1) 
    else : 
        print(0) 

