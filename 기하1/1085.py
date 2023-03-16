x, y, w, h = map(int, input().split(' '))

short_x = 0 
short_y = 0

if w - x >= x : 
    short_x = x 
else : 
    short_x = w - x 

if h - y >= y : 
    short_y = y
else : 
    short_y = h - y

if short_x >= short_y : 
    print(short_y) 
else :
    print(short_x)
