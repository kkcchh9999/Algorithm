# 나무 자르기

N, M = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)

while start <= end : 
    mid = (start + end) // 2

    take = 0
    for i in tree : 
        if i - mid > 0 : 
            take += (i - mid)

    if take >= M :
        start = mid + 1
    else : 
        end = mid - 1

print(end) 


