n = int(input())

arr = []
for i in range(n) : 
    t = int(input())
    arr.append(t)

# 두 가로수 사이의 차이의 최대공약수 => 동일한 거리 

def GCD(a, b) : 
    while b != 0 :
        if a >= b : 
            b, a = a, b
        b %= a 
    return a

difference = [] 
for i in range(n-1, 0, -1) :
    difference.append(arr[i] - arr[i-1])

gcd = GCD(difference[0], difference[1])
for i in range(1, len(difference)) :
    gcd = GCD(gcd, difference[i])

SUM = 0
for i in difference : 
    SUM += (i // gcd) - 1

print(SUM)

