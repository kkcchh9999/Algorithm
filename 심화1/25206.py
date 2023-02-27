total = 0
div = 0
score = [["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"],
        [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]]

for i in range(20) : 
    grade = input().split(" ")
    for j in range(len(score[0])) : 
        if grade[2] == score[0][j] : 
            div += float(grade[1])
            total += score[1][j] * float(grade[1])
print(round(total / div, 6))
