# 문자열 폭발

text = input()
boom = input()

stack = []

for i in text : 
    stack.append(i)

    if i == boom[-1] : 
        if ''.join(map(str, stack[-(len(boom)):])) == boom : 
            for i in range(len(boom)) : 
                stack.pop()

if len(stack) == 0 :
    print("FRULA")
else :     
    for i in stack : 
        print(i, end = '')
