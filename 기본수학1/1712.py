numbers = input().split(" ")

A = int(numbers[0])
B = int(numbers[1])
C = int(numbers[2])

if B >= C : 
    print(-1)
    exit() 

tmp = int(A / (C - B))+1

print(tmp)

