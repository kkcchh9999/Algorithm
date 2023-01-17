a = input().split()
num1 = int(a[0][2])*100 + int(a[0][1])*10 + int(a[0][0])
num2 = int(a[1][2])*100 + int(a[1][1])*10 + int(a[1][0])

if num1 > num2 : 
    print(num1) 
else : 
    print(num2) 

