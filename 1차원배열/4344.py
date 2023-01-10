re = int(input())
array = []
result = []
for i in range(re) :
    line = input()
    array.append(line.split(' '))

for i in range(re) : 
    avg = 0 
    for j in range(1, len(array[i])) :
        avg += int(array[i][j])
    avg /= int(array[i][0])
    
    count = 0
    for j in range(1, len(array[i])) :
        if avg < int(array[i][j]) : 
            count += 1
    result.append(count/int(array[i][0])) 

for i in range(re) : 
    print('%.3f' %(result[i]*100), end='') 
    print('%')
