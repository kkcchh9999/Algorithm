from collections import Counter
import sys
input = sys.stdin.readline 

n = int(input())

arr = []
for i in range(n) :
    arr.append(int(input()))

arr.sort()

avg = 0
for i in arr : 
    avg += i
print(round(avg/n)) 

print(arr[n//2])

cnt = Counter(arr)
if n > 1 : 
    if cnt.most_common()[0][1] == cnt.most_common()[1][1] : 
        print(cnt.most_common()[1][0]) 
    else : 
        print(cnt.most_common()[0][0])
else : 
    print(arr[0])
#범위
print(arr[-1] - arr[0]) 

