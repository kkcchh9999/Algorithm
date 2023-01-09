num = input()
array = list(input().split())
find = input()

count = 0
for i in array : 
    if i == find : 
        count += 1

print(count)
