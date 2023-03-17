n = int(input())
arr = list(map(int, input().split(' ')))

ans = [0]
ans[0] = arr[0] 

for i in range(len(arr)-1) : 
    ans.append(max(ans[i]+arr[i+1], arr[i+1]))

print(max(ans))
