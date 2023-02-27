n = input()
count = 1
for i in range(int(len(n)/2)):
    if n[i] != n[-1 * i -1] : 
        count = 0

print(count)
