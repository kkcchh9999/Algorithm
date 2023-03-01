a1, a2 = map(int, input().split(" ")) 
c = int(input())
n = int(input())

if a1 * n + a2 > c * n or c < a1 : 
    print(0) 
else : 
    print(1) 
