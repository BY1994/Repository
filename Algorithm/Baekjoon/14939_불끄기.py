"""
14939 불 끄기

불가능한 경우 고려해야함

완전히 그리디하게 풀려고 했는데
위에 켜진 경우에 이게 아래에서 눌러서 켜진 건지,
오른쪽에서 눌러서 켜진 건지 판단할 방법이 없다.
당장 근처의 O 를 확인해본다고 하더라도
중첩되어서 # 가 되어있다면 찾을 수 없다

=> 일반적으로 많이 사용한 풀이를 따라할 수 밖에 없다.
첫째줄은 greedy 하게 할 수 없으니 완전 탐색으로 답을 찾고,
그 다음줄부터는 판단이 가능하니 greedy 하게 할 수 있다.

첫째줄이 가능한 모든 경우의 수 2**10 에 대해서
각각 두번째 줄부터 greedy 하게 돌려본다.
"""

switch = [[0 for i in range(10)] for j in range(10)]
origin = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    s = input()
    for j in range(10):
        switch[i][j] = 1 if s[j] == 'O' else 0
        origin[i][j] = switch[i][j]

ans = 10001
cur = 0

def reverse(x, y):
    #global cur => 4개 다 끄는 거로 잘못 이해

    switch[x][y] = (switch[x][y]+1)%2
    #cur += 1
    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 10:
            continue
        switch[nx][ny] = (switch[nx][ny]+1) % 2
        #cur += 1

for click in range(2**10):
    cur = 0
    # 복원
    for i in range(10):
        for j in range(10):
            switch[i][j] = origin[i][j]
    
    # 첫번째 줄
    for i in range(10):
        if (click >> i) & 1:
            cur += 1
            reverse(0, i)

    # 두번째 줄
    for i in range(1, 10):
        for j in range(10):
            # 내 위가 켜져있으면 날 누르기
            if switch[i-1][j] == 1:
                cur += 1
                reverse(i, j)

    flag = 0
    for i in range(10):
        for j in range(10):
            if switch[i][j] == 1:
                flag = 1
                break
        if flag == 1:
            break

    if flag == 0:
            ans = min(ans, cur)

if ans == 10001:
    print(-1)
else:
    print(ans)

# 짜다가 포기
# 완전히 그리디하게 풀려고 시도했으니 잘못된 걸 알아챔
"""
switch = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    s = input()
    for j in range(10):
        switch[i][j] = 1 if s[j] == 'O' else 0

ans = 0

def reverse(x, y):
    global ans

    switch[nx][ny] = (switch[nx][ny]+1)%2
    ans += 1
    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if nx < 0 or nx >= 10 or ny < 0 or ny >= 10:
            continue
        switch[nx][ny] = (switch[nx][ny]+1) % 2
        ans += 1

for i in range(10):
    for j in range(10):
        # 왼쪽 아래가 없거나 꺼져있으면 내 오른쪽을 눌러야함
        if switch[i][j] == 1:
            if j < 1: # 잘못됨 => 아래 눌러도 켜짐
                # 오른쪽
                reverse(i, j+1)
            elif switch[i+1][j-1] == 0:
                # 오른쪽
                pass
            else:
                # 아래
                reverse(i+1, j)
        # 불가능한 경우 고려

print(ans)
"""
