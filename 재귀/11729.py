def hanoi(k, start, end) : 
    if k == 1 :
        print(start, end) 
        return

    hanoi(k-1, start, 6-start-end)
    print(start, end)
    hanoi(k-1, 6-start-end, end)

k = int(input())

print(2**k - 1)
hanoi(k, 1, 3) 
