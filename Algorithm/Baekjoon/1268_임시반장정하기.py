"""
1268 임시 반장 정하기

brute force
1000 학생 수 5학년 탐색이므로
1000 * 1000 * 5 면 완전 탐색 가능

내 실수
같은 학년인 경우를 학생마다 한 번만 카운트해야하는데 중복 시켜버림
내가 만든 반례
5
1 2 3 4 5
1 2 3 1 1
4 5 1 4 1
5 5 2 2 2
2 3 1 5 4
정답 3 틀린답 1

질문 답변 게시판에 위 반례 공유함
https://www.acmicpc.net/board/view/96048
"""

N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

count = [0] * N

for i in range(N):
    for j in range(N):
        # 자기 자신
        if i == j :
            continue
        # 1 ~ 5학년 동안 같은 반인 적 있었는지 확인
        for k in range(5):
            if matrix[i][k] == matrix[j][k]:
                count[i] += 1
                #break

ans = 0
_max = 0
for i in range(N):
    if count[i] > _max:
        _max = count[i]
        ans = i

print(ans+1)

# 틀린 코드
# 같은 반이 여러번 되면 중복 카운트 발생함
"""
N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

count = [0] * N

for i in range(N):
    for j in range(N):
        # 자기 자신
        if i == j :
            continue
        # 1 ~ 5학년 동안 같은 반인 적 있었는지 확인
        for k in range(5):
            if matrix[i][k] == matrix[j][k]:
                count[i] += 1

ans = 0
_max = 0
for i in range(N):
    if count[i] > _max:
        _max = count[i]
        ans = i

print(ans+1)
"""
