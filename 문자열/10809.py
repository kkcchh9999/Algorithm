alpha = list()
for i in range(26) : 
    alpha.append(-1)

s = input() 

for i in range(len(s)) : 
    if alpha[ord(s[i])-97] == -1 : 
       alpha[ord(s[i])-97] = i 

for i in alpha : 
    print(i, end=' ')

