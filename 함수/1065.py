def find (n: int) :

    if n < 100 : 
        return True 
    else : 
        arr = list()
        while n >= 1 : 
            arr.append(n % 10)
            n = int(n / 10) 
        check = list()
        for i in range(len(arr)-1) :
            check.append(arr[i] - arr[i+1])
        check = set(check)
        if len(check) == 1 : 
            return True 
        else :
            return False 

num = input() 
count = 0

for i in range(1, int(num)+1) :
    if find(i) == True :
        count += 1

print(count)
