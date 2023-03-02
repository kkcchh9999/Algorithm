def quick_sort(arr) :
    if len(arr) <= 1: 
        return arr 

    pivot = arr[len(arr) // 2]

    less, equal, greater = [], [], []

    for i in arr :
        if i < pivot :
            less.append(i) 
        elif i > pivot : 
            greater.append(i)
        else : 
            equal.append(i) 

    return quick_sort(less) + quick_sort(equal) + quick_sort(greater) 

n = int(input())
arr = []
for i in range(n) :
    num = int(input())
    arr.append(num)

result = quick_sort(arr) 

for i in arr :
    print(i) 


