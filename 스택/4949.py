# 균형잡힌 세상
import sys
input = sys.stdin.readline

while True : 
    arr = []
    text = input().rstrip()
    if text == '.' :
        break
    
    flag = False 
    for i in text : 
        if i == '(' or i == '[' : 
            arr.append(i)
        if i == ']' : 
            try : 
                if arr.pop() != '[' : 
                    flag = True 
                    break
            except : 
                flag = True
                break
        if i == ')' : 
            try : 
                if arr.pop() != '(' :
                    flag = True
                    break
            except : 
                flag = True
                break

    if flag == False and len(arr) == 0 : 
        print('yes')
    else : 
        print('no')

