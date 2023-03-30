#잃어버린 괄호

string = input()
oper = []
for i in string : 
    if i == '-' or i == '+' :
        oper.append(i)

nums = list(map(int, string.replace('-', '+').split('+')))

flag = False 
result = nums[0]
for i in range(len(oper)) : 
    if oper[i] == '-' :
        flag = True 

    if flag == False : 
        result += nums[i+1] 
    else :  
        result -= nums[i+1]

print(result)
