total = int(input())

arr = []
for i in range(total) : 
    arr.append(input())

for q in range(total) : 

    S = arr[q].split(" ")

    re = int(S[0])
    string = S[1]

    for i in range(len(string)) : 
        for j in range(re) : 
            print(string[i], end = "")

    print("")
