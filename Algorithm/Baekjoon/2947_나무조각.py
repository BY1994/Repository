"""
2947 나무 조각

나무조각 순서 바꾸는 규칙대로 시뮬레이션
=> 버블소트
"""

wood = list(map(int, input().split()))
flag = 1
while flag:
    flag = 0
    for i in range(4):
        if wood[i] > wood[i+1]:
            flag = 1
            wood[i], wood[i+1] = wood[i+1], wood[i]
            print(*wood)
