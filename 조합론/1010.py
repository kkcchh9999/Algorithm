# 다리 놓기

T = int(input())
for i in range(T) : 
    N, M = map(int, input().split())
    mfac = 1
    for i in range(2, M+1) : 
        mfac *= i

    nfac = 1
    for i in range(2, N+1) : 
        nfac *= i

    m_min_nfac = 1
    for i in range(2, M-N+1) : 
        m_min_nfac *= i 

    print(mfac//(nfac * m_min_nfac))

