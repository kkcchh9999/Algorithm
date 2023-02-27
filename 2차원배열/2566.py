arr = []
Max = 0
x = 0
y = 0
for i in range(9) : 
    line = list(map(int, input().split(" "))) 
    arr.append(line)

for i in range(9) :
    for j in range(9) : 
        if Max < arr[i][j] :
            Max = arr[i][j]
            x = i
            y = j

print(Max)
print("%d %d" %(x+1, y+1))

