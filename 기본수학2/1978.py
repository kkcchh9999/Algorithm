def isPrime(a: int) :
    if a == 1 :
        return False

    for i in range(2, a) :
        if a % i == 0 : 
            return False

    return True

n = int(input())

arr = input().split(" ")

count = 0
for i in arr :
    if isPrime(int(i)) == True :
        count += 1

print(count)


