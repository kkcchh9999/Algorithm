tmp = input()
word = tmp.lower()

count = []
alpha = 0
ans = ''
for i in range(26) : 
    count.append(word.count(chr(i+97)))


for i in range(26) :  
    if count[i] > alpha : 
        alpha = count[i]
        ans = chr(i+65)

if count.count(alpha) != 1 : 
    print('?')
else : 
    print(ans)
