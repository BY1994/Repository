"""
2660 회장 뽑기

2019.03.07 PBY 최초작성
"""

membernum = int(input())
memberChart = [[0 for _ in range(membernum+1)] for _ in range(membernum+1)]
memberScore = [0] * (membernum+1)

while True:
    cur_input = input().split()
    if cur_input[0] == "-1":
        break
    cur_input = list(map(int, cur_input))
    memberChart[cur_input[0]][cur_input[1]] = 1
    memberChart[cur_input[1]][cur_input[0]] = 1


for i in range(1, membernum+1):
    visited = [0] * (membernum + 1)

    queue = []
    depth = 1
    visited[i] = 1 # 나 자신 방문 체크 표시

    # 처음에 방문할 사람들
    for j in range(1, membernum + 1):
        if memberChart[i][j] == 1 and not visited[j]:  # 친구사이면 먼저 queue에 넣음
            queue.append(j)
            visited[j] = 1

    if all(visited[1:]):
        # 모든 사람이 다 친구면
        memberScore[i] = 1 # 1점 => 여기는 또 왜 j라고 써놨지 ㅠㅠㅠ 내 정보는 i에 있다!!
    else:
        while True:
            depth += 1
            # queue를 채우고 나면 그 queue를 돌면서 다음 친구를 또 찾음
            newqueue = []
            for j in queue: # 여기를 range로 하는 바람에 0부터 그냥 숫자 인덱스가 들어갔다.
                for k in range(1, membernum+1):
                    if memberChart[j][k] == 1 and not visited[k]:
                        newqueue.append(k)
                        visited[k] = 1
            # queue를 다 돌면서 newqueue를 채우고 나면
            if all(visited[1:]):
                memberScore[i] = depth # 나는 큐에 있는게 아니라 i에 내 정보가 있다.
                break #while문 탈출
            else:
                queue = newqueue[:] # 이걸로 새로 업데이트

# depth가 가장 적은 사람들 출력
minvalue = min(memberScore[1:])
ans = []
for i in range(1, membernum+1):
    if memberScore[i] == minvalue:
        ans += [i]

print(minvalue, len(ans))
print(' '.join(list(map(str, sorted(ans)))))

"""
def findFriend(num, depth):
    if memberScore[num] != 0:
        # 방문하지 않은 경우
        for f in range(membernum+1):
        # 친구를 찾으면
        if
        # 현재 뎁스를 스코어에 저장
            memberScore[num] = depth
            # 그리고 다음 친구 또 탐색
            findFriend(next, depth+1)
"""

# findFriend(i, 1) # 매 사람부터 다 시작해서 최대 뎁스 찾기
# 이건 DFS로 짜면 안 된다!!!!!!!!
# 친구의 친구 사이 가기 전에 친구 사이면 연결된 거로 처리하려면
# 나랑 제일 가까운 애들을 먼저 다 돌아야한다!!!!
# 그러면 재귀로 풀면 안 된다!!!!!

"""
자잘한 인덱스 오류 때문에 디버깅이 오래 걸렸다...
i랑 j를 바꿔쓴 부분이 제일 많았다.

queue를 하나씩 뽑아 써야 하는데 len() 이라고 써서 숫자가 들어간 것도 큰 문제였다...

"""