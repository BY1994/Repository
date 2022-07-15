"""
1043 거짓말

Union Find, DFS, BFS 다 가능

※ 문제 잘못 이해한 부분
지민이는 모든 파티에 참여해야한다. (그리고 반드시 얘기를 진실/과장 중에 하나를 해야한다)
https://www.acmicpc.net/board/view/11147

설명을 만들어봤는데 문제를 이렇게 이해하면 될 듯..
원래 진실을 아는 사람들이 있는 파티에 참석하면 지민이가 어쩔 수 없이 진실을 말해야 하기 때문에 처음 듣는 얘기인데 진실을 알게 된 사람들이 있습니다.
그 사람들이 참석한 다른 파티에서도 또 지민이는 진실을 얘기해야하고, 이렇게 점점 진실을 얘기해야하는 파티가 퍼져나가게 됩니다.

풀이시 참고
DSU (Disjoint Set Union) 사용시 그때 그때 사용하면 틀린다는 내용
https://www.acmicpc.net/board/view/93121


반례
파티 참여 인원이 0명인 경우 (지민이 혼자 참석하는 파티)
https://www.acmicpc.net/board/view/69703
=> 각 파티마다 오는 사람의 수는 1 이상이라는 조건 추가
https://www.acmicpc.net/board/view/73458

풀이 로직의 반례
https://www.acmicpc.net/board/view/72203
4 5
1 1
1 1
1 2
1 3
2 4 2
2 4 1
답은 1, 내 출력은 2
진실을 아는 사람들이 정정해주는 것만 생각하고,
파티 참여자 본인인 지민이 진실을 말해서 그걸 들은 사람들이 생긴다는 건 생각 못함
=> union find 로 풀어야하는 이유

비슷한 반례
https://www.acmicpc.net/board/view/85017
8 4
1 1
3 1 2 3
3 4 5 6
3 6 7 8
2 3 8
답은 0, 내 출력은 2

내가 만들어본 반례
10 9
1 1
2 9 10
2 8 9
2 7 8
2 6 7
2 5 6
2 4 5
2 3 4
2 2 3
2 1 2
답은 0
union find 아 아니면 이렇게 긴 depth 처리가 안 됨

질문 게시판을 위한 반례
https://www.acmicpc.net/board/view/8019
10 9
1 1
2 5 6
2 4 5
2 3 4
2 2 3
2 1 2
2 9 10
2 8 9
2 7 8
2 6 7
답 0

질문 게시판을 위한 반례
=> 아래 반례 잘못됨... LL 을 붙이지 않아서 발생한 문제인데,
나는 int 범위 넘어가는 반례만 만들면 된다고 착각함
https://www.acmicpc.net/board/view/46461
37 9
1 1
5 33 34 35 36 37
5 29 30 31 32 33
5 25 26 27 28 29
5 21 22 23 24 25
5 17 18 19 20 21
5 13 14 15 16 17 
5 9 10 11 12 13
5 5 6 7 8 9
5 1 2 3 4 5
답 0

질문 게시판을 위한 반례
https://www.acmicpc.net/board/view/89906
4 6
1 1
1 1
1 2
1 3
2 4 2
2 4 1
1 3
(아래 반례 응용)
https://www.acmicpc.net/board/view/72203

및

4 4
0
2 1 2
1 3
3 2 3 4
2 1 2
정답 4 틀린 코드 3

질문 게시판을 위한 반례
party.remove(party[rem.pop()]) 이 로직에서 index 꼬일 우려
https://www.acmicpc.net/board/view/94147
12 10
1 1
2 5 6
2 4 5
2 3 4
2 11 12
2 1 2
2 9 10
2 1 2
2 8 9
2 7 8
2 6 8
정답 8 틀린 코드 7

8 7
1 1
2 5 6
2 4 5
2 3 4
2 7 8
2 1 2
2 7 8
2 1 2
정답 5 틀린 코드 4
"""

# 진실을 듣는 사람들은 parent 를 0 번으로 묶어줌
def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    if find(a) == find(b):
        return
    if a >= b:
        parent[parent[a]] = parent[b]
    else:
        parent[parent[b]] = parent[a]

N, M = map(int, input().split())
party = []
parent = [0] * 51

for i in range(N+1):
    parent[i] = i

truth = list(map(int, input().split()))
for i in range(1, truth[0]+1):
    union(truth[i], 0)

for i in range(M):
    people = list(map(int, input().split()))
    party.append(people)

    flag = 0
    for j in range(1, people[0]+1):
        if find(people[j]) == 0: # 한 명이라도 진실을 알면,
            flag = 1
            break

    if flag == 1:
        for j in range(1, people[0]+1):
            union(people[j], 0) # 파티에 온 모두가 진실을 알게 됨 (지민이 진실을 말할 거니까)
    else:
        for j in range(2, people[0]+1):
            union(people[j], people[1]) # 과장을 들어도 되는 사람끼리 묶임 (나중에 전부 진실을 들어야할 수도 있는 후보군임)
        
ans = 0
for i in range(M):
    flag = 0
    for j in range(1, party[i][0]+1):
        if find(party[i][j]) == 0:
            flag = 1
            break
    if flag == 0:
        ans += 1

print(ans)


# 모든 파티에 반드시 참여해서 "진실" 혹은 "과장"을 얘기해야함
# 그 부분이 고려가 안 됨
# 원할 때만 "과장" 을 얘기하고 아니면 아예 파티 참석 안 하는 (얘기 안 하는) 경우를 가정한 코드
"""
N, M = map(int, input().split())
know = [0] * 51
truth = list(map(int, input().split()))
for i in range(1, truth[0]+1):
    know[truth[i]] = 1

people = []
for i in range(M):
    party = list(map(int, input().split()))
    people.append(party)
    flag = 0
    for j in range(1, party[0]+1):
        if know[party[j]] == 1:
            flag = 1
            break
    if flag == 1:
        for j in range(1, party[0]+1):
            if know[party[j]] == 1:
                continue
            know[party[j]] = 2

ans = 0
for i in range(M):
    flag = 0
    for j in range(1, people[i][0]+1):
        if know[people[i][j]] > 0:
            flag = 1
            break
    if flag == 0:
        ans += 1

print(ans)
"""
