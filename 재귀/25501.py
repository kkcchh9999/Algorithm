global t 
t = 0

def recursion(s, l, r) :
    global t

    if l >= r :
        t += 1 
        return 1
    elif s[l] != s[r] :  
        t += 1 
        return 0
    else : 
        t += 1 
        return recursion(s, l + 1, r - 1) 

def isPalindrome(s) : 
    global t 

    t = 0
    return recursion(s, 0, len(s) -1)

T = int(input()) 

for i in range(T) : 
    S = input() 
    print(isPalindrome(S), t) 
