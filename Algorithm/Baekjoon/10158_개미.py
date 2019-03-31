""" 
10158 개미
문제
가로 길이가 w이고 세로 길이가 h인 2차원 격자 공간이 있다. 이 격자는 아래 그림처럼 왼쪽 아래가 (0,0)이고 오른쪽 위가 (w,h)이다. 이 공간 안의 좌표 (p,q)에 개미 한 마리가 놓여있다. 개미는 오른쪽 위 45도 방향으로 일정한 속력으로 움직이기 시작한다. 처음에 (p,q)에서 출발한 개미는 1시간 후에는 (p+1,q+1)로 옮겨간다. 단, 이 속력으로 움직이다가 경계면에 부딪치면 같은 속력으로 반사되어 움직인다.
위 그림은 6×4 격자에서 처음에 (4,1)에서 출발한 개미가 움직인 길을 보여주고 있다. 처음에 (4,1)에 있는 개미는 2시간 후에 (6,3)에 있으며 8시간 후에 (0,1)에 있다. 만일 그 개미가 처음에 (5,3)에 있었다면 매 시간마다 (6,4), (5,3), (4,2), (3,1)로 움직인다. 
여러분은 크기 w×h인 격자 공간에서 처음에 (p,q)에서 출발하는 개미의 t시간 후의 위치 (x,y)를 계산하여 출력해야 한다. 개미는 절대 지치지 않고 같은 속력으로 이동한다고 가정한다. 
문제에서 w와 h는 자연수이며 범위는 2 ≤ w,h ≤ 40,000이다. 그리고 개미의 초기 위치 p와 q도 자연수이며 범위는 각각 0 < p < w과 0 < q < h이다. 그리고 계산할 시간 t의 범위는 1 ≤ t ≤ 200,000,000이다. 

입력
첫줄에는 w와 h가 공백을 사이에 두고 주어진다. 그 다음 줄에는 초기 위치의 좌표값 p와 q가 공백을 사이에 두고 주어진다. 3번째 줄에는 개미가 움직일 시간 t가 주어진다. 

출력
출력은 t 시간 후에 개미의 위치 좌표 (x,y)의 값 x와 y를 공백을 사이에 두고 출력한다.

최초작성 2019.03.15 PBY
수정 2019.03.23

입력
6 4
4 1
8
답 0 1

6 4
4 3
2
답 6 3

2 2
1 1
14
답 1 1

3 3
2 2
5
답 1 1

3 3
1 1
0
답 1 1

0 0
0 0
0

# 런타임 에러 찾음!!!!!!!
6 4
0 0
100303010 # 이런식으로 들어가면 - 값으로 무한대로 내려감....

"""

# 2 억번을 다 돌 필요 없이 점프해도 될 듯
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
m = 0
pd = 1
qd = 1
while m < t:
    if m < t-max(w,h):
        if pd == 1: # p 방향이 1
            if qd == 1: 
                # 더 빨리 벽에 부딪히는 경우
                if w-p >= h-q: # p가 더 빨리 부딪힘
                    m += w-p
                    p += w-p
                    q += w-p
                else:
            else:
                if w-p >= q:
    else:
        p = p+pd # 이걸 위에 올리면 0 0 에서 거꾸로 가는 경우 방지
        q = q+qd
        m += 1
        if p == w or p == 0:
            pd = -pd
        if q == h or q == 0:
            qd = -qd
# while문 나오면 m==t인 순간
print(p, q)


"""
# 시간초과 나는 코드 짧게 고친 버전
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
m = 0
pd = 1
qd = 1
while m < t:
    p = p+pd # 이걸 위에 올리면 0 0 에서 거꾸로 가는 경우 방지
    q = q+qd
    m += 1
    if p == w or p == 0:
        pd = -pd
    if q == h or q == 0:
        qd = -qd
# while문 나오면 m==t인 순간
print(p, q)
"""

"""
def antMove(curp,curq, pd, qd):
    global p, q, w, h, t
    print(curp, curq)
    global m
    if m == t:
        return
    m += 1
    if curp ==0 and curq ==0:
        pd = 1
        qd = 1
    elif curp == w and curq == h:
        pd = -1
        qd = -1 # 둘 다 방향 전환
    elif curp == w and curq == 0:
        pd = -1
        qd = 1
    elif curp == 0 and curq == h:
        pd = 1
        qd = -1
    elif curp == w or curp == 0:
        pd = -pd
    elif curq == h or curq == 0:
        qd = -qd

    if [curp + pd, curq + qd, pd, qd] in Moves:
        Moves.append([curp+pd, curq+qd, pd, qd])
        return
    Moves.append([curp+pd, curq+qd, pd, qd])
    antMove(curp+pd, curq+qd, pd, qd)

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
m = 0
Moves = [[p,q, 1, 1]]
antMove(p, q, 1, 1)
if t < len(Moves):
    ans = Moves[t]
else:
    for m in range(len(Moves)):
        if Moves[-1] == Moves[m]:
            start = m
            break
    end = len(Moves)-1
    if (t-(m-1))%(end-start) == 0:
        ans = Moves[end-1]
    else:
        ans = Moves[start+(t-(m-1))%(end-start)-1]
print(ans[0], ans[1])

"""

"""
a,b=map(int,input().split())
c,d=map(int,input().split())
t=int(input())
c+=t
d+=t
c%=a+a
d%=b+b
if c>a:
    c=a+a-c
if d>b:
    d=b+b-d
print(c,d)
"""


"""
w, h = list(map(int, input().split()))
p, q = list(map(int, input().split()))
t = int(input())

x, y, direct = p, q, 1
for time in range(t):
    print(x, y)
    if direct == 1:# 오른쪽 위로 움직이는 중
         if x == w: # 벽에 부딪히면 반사
             if y == h:
                 x -= 1
                 y -= 1
                 direct = 2
             else:
                 x -= 1
                 y += 1
             direct = 3 # 꺾임
         else: # 아니면 계속 오른쪽 위로 이동
             x += 1
             y += 1
    elif direct == 2: # 왼쪽 아래로 움직이는 중
        if y == 0: # 바닥에 부딪힘
            if x == 0:
                
            x -= 1
            y += 1
            direct = 4
        else: # 아니면 계속 왼쪽 아래로 이동
            x -= 1
            y -= 1
    elif direct == 3:
        if y == h:
            x -= 1
            y -= 1
            direct = 2
        else: # 왼쪽 위로 이동
            x -= 1
            y += 1
    elif direct == 4:
        if x == 0: # 왼쪽 벽에 부딪힘
            x += 1
            y += 1
            direct = 1
        else: # 왼쪽 위로 이동
            x -= 1
            y += 1
            direct = 1

print(x, y)
"""
