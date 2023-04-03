# 색종이 만들기

n = int(input())
paper = []
for i in range(n) :
    paper.append(list(map(int, input().split())))

blue = 0
white = 0

def dc(x, y, length) :
    global blue
    global white
    
    check = paper[x][y]
    for i in range(x, x + length) :
        for j in range(y, y + length) :
            if paper[i][j] != check :
                dc(x, y, length // 2)
                dc(x + length // 2, y, length // 2)
                dc(x, y + length // 2, length // 2)
                dc(x + length // 2, y + length // 2, length // 2)
                return

    if check == 0 :
        white += 1
    else :
        blue += 1


dc(0, 0, n)

print(white)
print(blue)
