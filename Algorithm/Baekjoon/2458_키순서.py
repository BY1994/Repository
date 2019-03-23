"""
2458 키순서

2019-03-23 PBY 최초작성

입력)
6 6
1 5
3 4
5 4
4 2
4 6
5 2

출력)
1
"""

def findOthers(std, h, cur):
    # 다음 candidates 찾기
    candidates = makeCandidates(cur, h)

    # candidates로 재귀 이동
    for c in candidates:
        array[std][c] = h # 다음 거를 찾으면 다 std에 정보가 오도록
        findOthers(std, h, c)

def makeCandidates(student, h):
    candidates = []
    for i in range(N):
        if array[student][i] == h:
            candidates.append(i)
    return candidates

T = int(input())
for tc in range(T):
    N = int(input())
    M = int(input())
    array = [[0 for _ in range(N)] for __ in range(N)]
    ans = 0
    for _ in range(M):
        a, b = map(int, input().split())
        array[a-1][b-1] = 1 # a가 b보다 작다
        array[b-1][a-1] = 2 # b가 a보다 크다

    for students in range(N):
        cand = makeCandidates(students, 1)
        for c in cand:
            for j in range(N):
                if array[c][j] == 1:
                    array[students][j] = 1
            if c > students: # 나보다 작으면 이미 다 돌았을 것
                findOthers(students, 1, c)

        cand = makeCandidates(students, 2)
        for c in cand:
            for j in range(N):
                if array[c][j] == 2:
                    array[students][j] = 2
            if c > students:
                findOthers(students, 2, c)
            
        # 본인 빼고 나머지의 키 순서가 다 저장되었는지 확인
        cnt = 0
        for i in range(N):
            if array[students][i] != 0:
                cnt += 1
        if cnt == N-1:
            ans += 1

    print("#%d %d" %(tc+1,ans))



"""
def findOthers(std, h, cur):
    # 다음 candidates 찾기
    candidates = []
    for i in range(N):
        if array[cur][i] == h: # 다음 갈 수 있는 길
            candidates.append(i)

    # candidates로 재귀 이동
    for c in candidates:
        array[std][c] = h # 다음 거를 찾으면 다 std에 정보가 오도록
        findOthers(std, h, c)


N, M = map(int, input().split())
array = [[0 for _ in range(N)] for __ in range(N)]
ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    array[a-1][b-1] = 1 # a가 b보다 작다
    array[b-1][a-1] = 2 # b가 a보다 크다

for students in range(N):
    findOthers(students, 1, students)
    findOthers(students, 2, students)

    # 본인 빼고 나머지의 키 순서가 다 저장되었는지 확인
    cnt = 0
    for i in range(N):
        if array[students][i] != 0:
            cnt += 1
    if cnt == N-1:
        ans += 1

print(ans)
"""
