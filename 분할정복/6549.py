# 히스토그램에서 가장 큰 직사각형

import sys

while True:
	#마지막에 stack에 있는 값을들 다 꺼내기 위해 마지막 h값은 0
    height = list(map(int, sys.stdin.readline().split())) + [0]
    n = height[0]
    if height[0] == 0:
        break

    stack = [(1, height[1])]
    square = 0
    for i in range(2,n+2):
        weight = i
        #나보다 stack에 있는 h가 더 높으면 꺼내서 (나의 높이 * 너비)
        while stack and stack[-1][1] > height[i]:
            weight, hi = stack.pop()
            square = max(square, (i-weight)*hi)
        stack.append((weight, height[i]))
    print(square)
