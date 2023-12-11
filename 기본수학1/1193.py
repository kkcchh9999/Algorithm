
n = int(input())


max = 1
sum = 0

while sum < n : 
	sum += max
	max += 1

re = sum - n
a = 1
b = 1   

if (max-1) % 2 == 0 : 
    a = max-1
    for i in range(0, re) : 
        a -= 1
        b += 1
else : 
    b = max-1 
    for i in range(0, re) : 
        a += 1
        b -= 1
        
print(a, end = "")
print("/", end = "")
print(b)