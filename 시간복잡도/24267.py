n = int(input())

cnt = 0
n -= 2
j = n
for i in range(1, j+1) : 
     cnt += i * n 
     n -= 1

print(cnt)
print(3)
