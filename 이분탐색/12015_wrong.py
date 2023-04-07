# 가장 긴 증가하는 부분 수열2 

n = int(input())
arr = list(map(int, input().split()))
search = [0]

for i in arr : 
    if search[-1] < i : 
        search.append(i)
    else : 
        start = 0
        end = len(search) 

        while start < end : 
            mid = (start + end) // 2 
            
            if search[mid] < i : 
                start = mid + 1
            else : 
                end = mid

        search[end] = i 


print(len(search)-1) 
