re = int(input())
result = []
for j in range(re) :
    ox = input()
    count = 1
    score = 0
    for i in range(len(ox)) :
       if ox[i] == 'O' : 
           score += count
           count += 1 
       if ox[i] == 'X' : 
           count = 1 
    result.append(score) 

for i in range(len(result)) :
    print(result[i])
