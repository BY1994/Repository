"""
10775 공항

그리디, union find

시간초과 2022.04.23
비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고,
=> 이 부분은 처음 문제 읽을 때 이해 못했는데,
예제 2번 보고 이해함
도킹 실패하면 거기서 바로 끝내라는 것

http://mmhs.ca/ccc/2015/2015s3MatthewLee.txt
https://www.acmicpc.net/board/view/60248

(이 방법은 clever counting 이라고 한다)
https://www.acmicpc.net/board/view/42880

재도전 통과 2022.09.17
i 부터 g 까지이기 때문에 그림으로 그려보면
무조건 왼쪽끝부터 길이가 다른 네모들이 그려지게 될 것이다.
[    ]
[  ]
[     ]
왼쪽으로 갈수록 겹칠 것이므로
지금값 중 가장 끝에서부터 채워가야 그리디하게 다 채울 수 있을 것이다.
* 나보다 작은 구간이 오면 나는 무조건 내가 가진 끝 값이어야할 것

그런데 이전 풀이가 시간초과가 났으므로 구간 중 가장 작은 거를 빠르게 찾을 방법이 필요하다
이전 부모 값을 가지고 있다가 그걸 업데이트하면 빠르게 찾아갈 수 있을 것
(시간 초과 원인이 10^5 를 readline 안 쓰고 input으로 받아서 그런 건 아닌가?)

원본 문제 input output
2015 년 Gates
http://mmhs.ca/ccc/index.htm#2005%20Problems

랜덤 생성 대형 반례 모음
https://www.acmicpc.net/board/view/43934

내가 틀린 부분 업데이트하는 코드 여기 참고
https://www.acmicpc.net/board/view/49229

docked[org_plane] = docked[plane-1]
이렇게 하면 plane 과 plane -1 의 관계가 업데이트가 안 되어서
다음에 요청에 plane 으로 들어오면 할당을 해버린다.
위의 링크에서 참고한 건 docked[plane] = plane - 1 였는데
경로 압축을 위하여 docked[plane] = docked[plane - 1] 으로 변경했다.

이 내용을 토대로 만들어본 반례 (4 를 두번 호출했을 때 2 의 값이 업데이트가 안 됨)
입력
4
5
3
4
4
1
2
정답 4 틀린 답 5
정답 docked [0 0 1 2 2]
틀린 docked [0 0 0 2 1]

+ 시간초과
docked[org_plane] 을 업데이트 안 하면 안 됨
재귀로 푸는 경우 경로압축이 잘 들어가 있어서 문제가 안 되었을 것
"""
import sys

G = int(input())
P = int(input())

docked = [0]*(G+1)
for i in range(1, G+1):
    docked[i] = i

ans = 0
flag = 1
for i in range(P):
    org_plane = int(sys.stdin.readline())
    if flag:
        plane = org_plane
        while docked[plane] != plane:
            plane = docked[plane]
        if plane:
            docked[org_plane] = docked[plane - 1]
            docked[plane] = docked[plane - 1]
            ans += 1
        else:
            flag = 0

print(ans)

# 시간초과
"""
G = int(input())
P = int(input())
plane = []
for i in range(P):
    plane.append(int(input()))

docked = [0]*(G+1)
ans = 0
for i in range(P):
    cur = plane[i]
    while cur > 1 and docked[cur] == 1:
        cur -= 1

    if docked[cur] == 1:
        break

    ans += 1
    docked[cur] = 1

print(ans)
"""

# 틀린 풀이
# sorting 해서 작은 거 부터 채워넣으면 된다고 생각했는데
# 비행기가 순서대로 들어오는 걸 고려 안 함...
"""
G = int(input())
P = int(input())
plane = []
for i in range(P):
    plane.append(int(input()))

plane.sort()

cur = 1
ans = 0
for i in range(P):
    if cur <= plane[i]:
        ans += 1
        cur += 1
    else: # 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 
        break
print(ans)
"""
