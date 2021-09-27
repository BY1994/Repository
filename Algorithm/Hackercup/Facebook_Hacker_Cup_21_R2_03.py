"""
2021 Facebook Hackercup R2

C1
"""

import sys
sys.stdin = open("valet_parking_chapter_1_input.txt")
sys.stdout = open("valet_parking_chapter_1_output.txt", "wt")


for tc in range(int(input())):
    ans = 10000010

    r, c, k = map(int, input().split())
    garage = ['.'*c]
    cars_up = [0] * c
    cars_down = [0] * c
    index_up = [k] * c
    index_down = [k] * c

    for i in range(r):
        row = input()
        garage.append(row)
        for index, car in enumerate(row):
            if car == 'X':
                if i < k-1:
                    cars_up[index] += 1
                elif i > k-1:
                    cars_down[index] += 1

    garage.append('.'*c)

    # up
    # 위로 한 칸씩 밀면서 ring 쓰면 최소인지 확인
    # empty 개수 줄여가면서
    for i in range(r):
        temp = 0 # slide + 1
        #print(i)
        for j in range(c):
            #print(index_up[j], end=' ')
            if garage[index_up[j]][j] == 'X':
                temp += 1
                cars_up[j] += 1 # cars_up 에는 내 직전까지의 X 개수가 저장됨
            elif cars_up[j] >= k:
                temp += 1

            # slide 는 계속 시킴
            if index_up[j] <= r and cars_up[j] < k:
                index_up[j] += 1
        #print()
        #print(temp+i)

        if temp + i < ans:
            ans = temp + i

    # down
    for i in range(r):
        temp2 = 0
        #print(i)
        for j in range(c):
            #print(index_down[j], end=' ')
            if garage[index_down[j]][j] == 'X':
                temp2 += 1
                cars_down[j] += 1
            elif cars_down[j] >= r-k+1:
                temp2 += 1

            if index_down[j] > 0 and cars_down[j] < r-k+1:
                index_down[j] -= 1
        #print()

        #print(temp2 + i)
        if temp2 + i < ans:
            ans = temp2 + i
                
    print(f"Case #{tc+1}: {ans}")

    
"""
        for index, car in enumerate(row):
            if car == '.':
                if i + 1 <= k:
                    empty_up[index] += 1
                elif i + 1 >= k:
                    empty_down[index] += 1

"""

# 문제 잘못 이해 => 슬라이딩이 한방에 끝까지 된다고 착각함    
"""
for tc in range(int(input())):
    ans = 10000010
    min_values = [10000010]*3
    #min_up = 10000010
    #min_down = 10000010
    #min_nos = 10000010

    r, c, k = map(int, input().split())
    garage = []
    cars = [0] * c

    for i in range(r):
        row = input()
        garage.append(row)
        for index, car in enumerate(row):
            if car == 'X':
                cars[index] += 1

    # up
    temp = 0
    for car in cars:
        if car >= k:
            temp += 1
    if temp <= 10:
        min_values[0] = temp + 1

    # down
    temp = 0
    for car in cars:
        if r-car < k:
            temp += 1
    if temp <= 10:
        min_values[1] = temp + 1

    # no slide
    temp = 0
    for car in garage[k-1]:
        if car == 'X':
            temp += 1
    if temp <= 10:
        min_values[2] = temp

    # ans
    for value in min_values:
        if value < ans:
            ans = value

    print(f"Case #{tc+1}: {ans}")
"""
