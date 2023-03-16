x = []
y = [] 

for i in range(3) :
    xint, yint = map(int, input().split(' ')) 
    x.append(xint)
    y.append(yint)

for i in range(3) :
    if x.count(x[i]) == 1 : 
        ansx = x[i] 
    if y.count(y[i]) == 1 : 
        ansy = y[i] 

print(ansx, ansy)
