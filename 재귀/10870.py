def fivo(n) :
    if n == 1 : 
        return 1
    elif n == 0 : 
        return 0 
    else : 
        return fivo(n-1) + fivo(n-2)

print(fivo(int(input())))
