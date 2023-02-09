nums = input().split(" ")

a = int(nums[0])
b = int(nums[1])
c = int(nums[2])

if int((c - b) / (a - b)) == (c -b) / (a - b) : 
    print(int((c - b) / (a - b)))
else :
    print(int((c - b) / (a - b)) + 1)
