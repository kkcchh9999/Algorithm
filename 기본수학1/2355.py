a, b = map(int, input().split())

big = max(a, b)
small = min(a, b)

if a == b: 
    print(a) 
elif (big - small) % 2 == 1 : 
    print((small + big) * ((big - small) // 2 + 1))
else :
    print((small + big - 1) * ((big - 1 - small) // 2 + 1) + big) 
