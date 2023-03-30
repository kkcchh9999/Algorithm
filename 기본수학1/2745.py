# 진법 변환

N, B = input().split()
B = int(B) 

answer = 0
for i in range(len(N)-1, -1, -1) : 
    try : 
        answer += int(N[i]) * (B**(len(N)-i-1))
    except : 
        answer += (ord(N[i])-55) * (B**(len(N)-i-1))

print(answer)
  

           
 
