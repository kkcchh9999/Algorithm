# 좌표 압축

n = int(input())
nums = list(map(int, input().split()))

tmp = sorted(list(set(nums)))
compress = {}
cnt = 0
for i in tmp : 
    compress[i] = cnt
    cnt += 1

for i in nums : 
    print(compress[i], end = ' ')
