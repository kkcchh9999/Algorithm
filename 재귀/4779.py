def kan(arr, flag) :
    if len(arr) == 1 and flag == True : 
        return ['-']
    elif flag == False : 
        return [' ' for _ in range(len(arr))]
  
 
    return kan(arr[ : len(arr)//3], True) + kan(arr[len(arr)//3 : len(arr)//3*2], False) + kan(arr[len(arr)//3*2 : ], True) 

while True : 
    try : 
        n = int(input()) 
    except : 
        break
    
    arr = ['-' for i in range(3**n)]

    arr = kan(arr, True) 
    for i in arr : 
        print(i, end = '')
    print() 
