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

4 3
1 2
1 3
2 4

1
"""

# visited로 인덱스 접근을 안해서 c not in  엄청 오래 걸렸을 거고
# 가지치기도 넣지 않았다.

def findOthers(std, h, cur):
    if arraynum[0][std] + arraynum[1][std] == N-1: # 가지치기. 이 작업을 안해서 시간초과?
        return
    # 다음 candidates 찾기
    if arraynum[h-1][cur] > 0:
        for c in array[h-1][cur]:
            if c not in array[h-1][std]:
                arraynum[h-1][std] += 1
                array[h-1][std].append(c)
                findOthers(std, h, c)

T = 1 #int(input())
for tc in range(T):
    N, M = map(int, input().split())
#    N = int(input())
#    M = int(input())
    # 인접리스트로 만들기
    array = [[[] for _ in range(N)], [[] for _ in range(N)]]
    arraynum = [[0 for _ in range(N)],[0 for _ in range(N)]]
    ans = 0
    for _ in range(M):
        a, b = map(int, input().split())
        array[0][a-1].append(b-1) # a가 b보다 작다
        arraynum[0][a-1] += 1
        array[1][b-1].append(a-1) # b가 a보다 크다
        arraynum[1][b-1] +=1

    for students in range(N):
        if arraynum[0][students] > 0: # 인접 리스트에 연결된 수가 있으면,
            for c in array[0][students]:
                if c >= students: # 나보다 낮은 수는 이미 재귀를 다 돌았으니까 들어갈 필요 없다.
                    findOthers(students, 1, c) # 내 인접 리스트에 연결된 것으로 따라감
                else: #나보다 낮은 수면 이미 결과가 나온 거니까 그냥 바로 추가해주면 됨
                    if arraynum[0][c] > 0:
                        for c2 in array[0][c]:
                            if c2 not in array[0][students]:
                                arraynum[0][students] += 1
                                array[0][students].append(c2)
        
        # 첫번째 예제는 c < students 가 없나봄
        if arraynum[1][students] > 0:
            for c in array[1][students]:
                if c >= students:
                    findOthers(students, 2, c)
                else: # 이 부분 안 넣어주면 틀렸습니다 뜬다.
                    if arraynum[1][c] > 0:
                        for c2 in array[1][c]:
                            if c2 not in array[1][students]:
                                arraynum[1][students] += 1
                                array[1][students].append(c2)

        # 본인 빼고 나머지의 키 순서가 다 저장되었는지 확인
        if arraynum[0][students] + arraynum[1][students] == N-1:
            ans += 1


    print(ans)
#    print("#%d %d" %(tc+1,ans))
    

"""
# 시간초과
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


"""
# 작성중이던 초기 컨셉
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
