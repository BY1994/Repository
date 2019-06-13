"""
BOJ 3088 화분 부수기

2019.06.13 PBY 최초작성
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
1. 틀렸습니다 => 문제 해석 잘못함
"""

# 연결 리스트를 두 종류를 만들어서
# 가장 많은 수의 화분이 해당하는 숫자부터 깨뜨리기...


