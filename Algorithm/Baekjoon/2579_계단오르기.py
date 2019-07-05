"""
2579 계단오르기

input)
6
10
20
15
25
10
20

2019.07.05 PBY 최초작성

comment)
이 문제를 풀 때 처음에는 계단들을 직접 그리고 가능한 경우를 나눠보면서 그림을 그렸고,
그 다음에는 상태 공간 트리로 내려가면서 규칙을 찾으려고 했다.
그 다음에 이전 점프수를 고려해야한다는 것을 깨닫고 점프가 0, 1, 2 경우뿐이라는 것을 생각했고
여기서 n-1 계단으로부터 뭘 고려해야하고, n-2 계단으로부터 뭘 고려해야하는지 알 수 있었다.
"""

# DP 연습문제

# input
N = int(input())
stairs = [0]*(N+1)
for i in range(N):
    stairs[i+1] = int(input())

# 메모이제이션 (+1은 시작점) [계단위치][누적점프수]
memo = [[0]*2 for _ in range(N+1)]

# 기저조건 설정
memo[1][0] = stairs[1] # 첫 계단 앞은 고려하지 않음 (계단이 아니니까)

# DP
for step in range(2, N+1):
    # n-1 위치 살펴보기
    memo[step][1] = memo[step-1][0]+stairs[step]
    # n-2 위치 살펴보기
    memo[step][0] = max(memo[step-2][0], memo[step-2][1])+stairs[step]

# output
print(max(memo[-1]))

# 세 계단을 밟을 수 없다는 걸 잘못 이해 => 문제의 그림을 보면 연속된 세 계단이 아예 밟히면 안 되고, 첫 계단 밟는 것만 예외임...
"""

# input
N = int(input())
stairs = [0]*(N+1)
for i in range(N):
    stairs[i+1] = int(input())

# 메모이제이션 (+1은 시작점) [계단위치][누적점프수]
memo = [[0]*3 for _ in range(N+1)]

# 기저조건 설정
memo[1][1] = stairs[1]
memo[2][2] = stairs[1]+stairs[2]

# DP
for step in range(3, N+1):
    # n-1 위치 살펴보기
    memo[step][1] = memo[step-1][0]+stairs[step]
    memo[step][2] = memo[step-1][1]+stairs[step]
    # n-2 위치 살펴보기
    memo[step][0] = max(memo[step-2][0], memo[step-2][1], memo[step-2][2])+stairs[step]


# output
print(max(memo[-1]))
"""
