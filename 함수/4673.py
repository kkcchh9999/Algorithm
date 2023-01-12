def d(n: int) :
    result = 0
    result += n 
    while n >= 1 :
        result += n % 10
        n /= 10
        n = int(n)
    
    return result

arr = list(range(10000))

for i in range(10000) : 
    num = d(i)
    if num in arr : 
        arr.remove(num)

for i in arr : 
    print(i) 

