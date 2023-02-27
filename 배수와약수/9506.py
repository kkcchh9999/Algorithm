while True : 
    n = int(input())
    if n == -1 :
        exit() 
    arr = []
    add = 0
    for i in range(1, n) : 
        if n % i == 0 :
            arr.append(i)
    for i in arr :
       add += i
    if add == n : 
        print("%d = " %n, end = "")
        for i in arr : 
            print(i, end = " ")
            if i != arr[-1]: 
                print("+ ", end = "")
    else : 
        print("%d is NOT perfect." %n)

