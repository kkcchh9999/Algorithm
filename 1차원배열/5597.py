student = range(1,31)

did_homework28 = []
for i in range(28) : 
    did_homework28.append(int(input()))

for i in range(30) : 
    if student[i] not in did_homework28 : 
        print(student[i])
