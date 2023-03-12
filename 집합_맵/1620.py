import sys
input = sys.stdin.readline() 

n, m = map(int, input().split(" "))

pocketmon = {}

for i in range(n) :
    pocketmon[input()] = i + 1

reverse_pocketmon = {v:k for k,v in pocketmon.items()} 

quest = []
for i in range(m) :
    quest.append(input())

for i in quest : 
    if i.isdigit() == True : 
        print(reverse_pocketmon[int(i)])
    else : 
        print(pocketmon[i])


