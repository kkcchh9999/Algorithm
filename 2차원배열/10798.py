arr = []
for i in range(5) :
    line = input()
    arr.append(line)

for j in range(15) :
    for i in range(5) : 
        try:    
            print(arr[i][j], end = "")
        except: 
            pass
