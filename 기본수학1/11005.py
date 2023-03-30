# 진법 변환 2

N, B = map(int, input().split())
system = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = str()

while N != 0 : 
    answer += system[N % B]
    N //= B

print(answer[::-1]) 
