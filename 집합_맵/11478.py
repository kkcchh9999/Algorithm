S = input() 

part = set() 

for i in range(len(S)+1) : 
    for j in range(i+1, len(S) + 1) : 
        part.add(S[i:j])
print(len(part))

