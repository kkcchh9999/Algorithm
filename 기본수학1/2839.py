N = int(input())

if N % 5 == 0 :
    print(int(N/5))
else :
    tmp = N
    count = 0
    while tmp % 5 != 0 :
        tmp -= 3
        count += 1
        if tmp < 0 : 
            print(-1)
            exit()

    print(int(tmp/5) + count)

