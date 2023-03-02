n = int(input())

strinput = input() 
arr = list(map(int, strinput.split(" ")))

norepeat = sorted(list(set(arr)))


dic = {norepeat[i] : i for i in range(len(norepeat))}

for i in arr : 
    print(dic[i], end = ' ') 
