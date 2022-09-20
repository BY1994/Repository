"""
16937 두 스티커

브루트 포스 기하학

1. brute force 로 복잡하게 말고, 맨 위 하나 맨 끝 하나 양 대각선을 시작점으로 해서 붙이는 방법이 가능하다고 한다.
2. 90 도 회전하는 것이 두 스티커 다 가능해야함
3. 첫번째 스티커가 무조건 판 안에 들어온다는 보장이 없음
https://www.acmicpc.net/board/view/77553
2 2
2
100 1
1 1
내 출력 101 정답 0

내가 만들어본 내 코드 반례
if 조건과 possible 이 따로 놀면 안 될 것 같다.
1 3
2
3 1
1 1
틀린 답 4 정답 0

2022.09.16 틀렸습니다
2022.09.20 통과
"""

# 아래, 오른쪽 + 회전시킨 후 아래, 오른쪽
def possible(x1, y1, x2, y2):
    if x2 <= H - x1 and y2 <= W:
        return True
    elif x2 <= H and y2 <= W - y1:
        return True
    if y2 <= H - x1 and x2 <= W:
        return True
    elif y2 <= H and x2 <= W - y1:
        return True
    return False

H, W = map(int, input().split())
N = int(input())
stickers = []
for i in range(N):
    stickers.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    first = stickers[i][0]*stickers[i][1]
    for j in range(i+1, N):
        total = first + stickers[j][0]*stickers[j][1]

        if stickers[i][0] <= H and stickers[i][1] <= W:
            if possible(stickers[i][0], stickers[i][1], stickers[j][0], stickers[j][1]):
                ans = max(ans, total)

        if stickers[i][0] <= W and stickers[i][1] <= H:
            if possible(stickers[i][1], stickers[i][0], stickers[j][0], stickers[j][1]):
                ans = max(ans, total)

print(ans)

# 첫번째 스티커 크기 조건 넣었으나
# 틀렸습니다
"""
H, W = map(int, input().split())
N = int(input())
stickers = []
for i in range(N):
    stickers.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    if (stickers[i][0] <= H and stickers[i][1] <= W) or (stickers[i][0] <= W and stickers[i][1] <= H):
        cur = stickers[i][0]*stickers[i][1]
        possible = [(H - stickers[i][0], W), (H, W - stickers[i][1]), (W, H - stickers[i][0]), (W - stickers[i][1], H), \
                    (H - stickers[i][1], W), (H, W - stickers[i][0]), (W, H - stickers[i][1]), (W - stickers[i][0], H)]

        for j in range(i+1, N):
            for R, C in possible:
                if stickers[j][0] <= R and stickers[j][1] <= C:
                    ans = max(ans, cur + stickers[j][0]*stickers[j][1])
                    break

print(ans)
"""

# 이렇게 하니 문제 예제 안 나옴
# 시작점도 90도 회전시켜야함
# 로직 잘못된 부분 i+1, N 순회하면서 가능하다고 break 되면 안 됨 뒤에 더 큰 스티커가 있을 수 있어서
"""
H, W = map(int, input().split())
N = int(input())
stickers = []
for i in range(N):
    stickers.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    cur = stickers[i][0]*stickers[i][1]
    for j in range(i+1, N):
        if stickers[j][0] <= H - stickers[i][0]:
            cur += stickers[j][0]*stickers[j][1]
            break
        if stickers[j][1] <= W - stickers[i][1]:
            cur += stickers[j][0]*stickers[j][1]
            break
        # 90 도 회전
        if stickers[j][1] <= H - stickers[i][0] and stickers[j][0] <= W:
            cur += stickers[j][0]*stickers[j][1]
            break
        if stickers[j][1] <= H  and stickers[j][0] <= W - stickers[i][1]:
            cur += stickers[j][0]*stickers[j][1]
            break
    else:
        cur = 0

    ans = max(ans, cur)

print(ans)
"""
