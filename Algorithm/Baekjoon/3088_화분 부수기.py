"""
BOJ 3088 화분 부수기

2019.06.13 PBY 최초작성
"""

N = int(input())
flowers = [[0]*3 for _ in range(N)]
numbers = [0] * 1000001
for i in range(N):
    flowers[i][0], flowers[i][1], flowers[i][2] = map(int, input().split())

# 앞에서부터 깨기 (어차피 오른쪽 바로가 안 깨지면 그걸 깨러 와야하니까?)
broken = 0

for i in range(N):
    flag = 0
    for k in range(3):
        if numbers[flowers[i][k]] == 1:
            flag = 1
    if flag == 0:
        broken += 1

    # 화분에 서로 다른 세 정수라는 말이 없어서 혹시 몰라 for문 밖으로 빼냈다.
    numbers[flowers[i][0]] = 1
    numbers[flowers[i][1]] = 1
    numbers[flowers[i][2]] = 1

print(broken)

"""
1. 틀렸습니다 => 문제 해석 잘못함
"""

"""
N = int(input())
flowers = [[0]*3 for _ in range(N)]
for i in range(N):
    flowers[i][0], flowers[i][1], flowers[i][2] = map(int, input().split())

# 뒤에서부터 오면서, 깨야하는 화분 개수 세기
broken = 1
flag = 0

for i in range(N-1, -1, -1):
    if flag == 1:
        broken += 1
        flag = 0

    for k in range(3):
        if i != 0 and flowers[i][k] in flowers[i-1]:
            break
    else:
        flag = 1

print(broken)

"""


