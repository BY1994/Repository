"""
2096 내려가기

메모리 초과
https://www.acmicpc.net/board/view/69615
int형 숫자를 3개씩 10만번 입력받는 것 만으로도 4Mb 초과입니다.

"""
N = int(input())
_min = [0, 0, 0]
_max = [0, 0, 0]

# 3 개를 받은 다음에...
# 지금 가지고 있는 3개랑 최대 최소 계산
# 그리고 자기거 더함

for _ in range(N):
    cur = list(map(int, input().split()))
    max1 = max(_max[0], _max[1])
    max2 = max(_max[1], _max[2])
    min1 = min(_min[0], _min[1])
    min2 = min(_min[1], _min[2])

    _max[0] = cur[0] + max1
    _max[1] = cur[1] + max(max1, max2)
    _max[2] = cur[2] + max2

    _min[0] = cur[0] + min1
    _min[1] = cur[1] + min(min1, min2)
    _min[2] = cur[2] + min2

    # 예제가 안 나온 이유
    """
    _max[0] = cur[0] + max(_max[0], _max[1])
    _max[1] = cur[1] + max(_max[0], _max[1], _max[2])
    _max[2] = cur[2] + max(_max[1], _max[2])

    _min[0] = cur[0] + min(_min[0], _min[1])
    _min[1] = cur[1] + min(_min[0], _min[1], _min[2])
    _min[2] = cur[2] + min(_min[1], _min[2])
    """

    #print(_max, _min)

print(max(_max), min(_min))

"""
N = int(input())
origin = []
for _ in range(N):
    origin.append(list(map(int, input().split())))

_max = [[0 for i in range(3)] for j in range(N)]
_min = [[0 for i in range(3)] for j in range(N)]

# 첫칸은 1, 2번이 주는 거 중 max
# 두번째 칸은 1, 2, 3 번이 주는 거 중 max
# 세번째 칸은 2, 3 번이 주는 거 중 max

for i in range(3):
    _max[0][i] = origin[0][i]
    _min[0][i] = origin[0][i]

for i in range(1, N):
    _max[i][0] = origin[i][0] + max(_max[i-1][0], _max[i-1][1])
    _max[i][1] = origin[i][1] + max(_max[i-1][0], _max[i-1][1], _max[i-1][2])
    _max[i][2] = origin[i][2] + max(_max[i-1][1], _max[i-1][2])

    _min[i][0] = origin[i][0] + min(_min[i-1][0], _min[i-1][1])
    _min[i][1] = origin[i][1] + min(_min[i-1][0], _min[i-1][1], _min[i-1][2])
    _min[i][2] = origin[i][2] + min(_min[i-1][1], _min[i-1][2])

print(max(_max[N-1]), min(_min[N-1]))
"""
