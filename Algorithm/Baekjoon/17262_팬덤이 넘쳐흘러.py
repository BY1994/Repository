"""
17262 팬덤이 넘쳐흘러

input)
3
2 5
1 4
2 4

2019.06.19 PBY 최초작성
"""

# 시간 단축해보기 - 2차 시도: realine사용 (160 ms)
# 참고: https://118k.tistory.com/697
import sys

N = int(input())
gohome = 100000
comehere = 0
for fan in range(N):
    s, e = map(int, sys.stdin.readline().split())
    if e < gohome:
        gohome = e
    if s > comehere:
        comehere = s

if comehere - gohome < 0:
    print(0)
else:
    print(comehere-gohome)


# 시간 단축해보기 - 1차 시도: 불필요한 반복문 제거 (4100 ms)
"""
N = int(input())
gohome = 100000
comehere = 0
for fan in range(N):
    s, e = map(int, input().split())
    if e < gohome:
        gohome = e
    if s > comehere:
        comehere = s

if comehere - gohome < 0:
    print(0)
else:
    print(comehere-gohome)
"""

# 시간 단축 전 (4368 ms)
"""
# 제일 빨리 가는 애 찾기
N = int(input())
fans = [[0, 0] for _ in range(N)]
gohome = 100000
for fan in range(N):
    fans[fan][0], fans[fan][1] = map(int, input().split())
    if fans[fan][1] < gohome:
        gohome = fans[fan][1]
        
# 그 이후 제일 늦게 오는 애 찾기
comehere = gohome
for fan in range(N):
    if fans[fan][0] > comehere:
        comehere = fans[fan][0]

print(comehere-gohome)
"""
