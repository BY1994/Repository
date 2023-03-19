"""
3060 욕심쟁이 돼지

1. 시뮬레이션
배열 2차원으로 [0][6], [1][6]
t = (t+1) % 2로 계속 번갈아 가면서 접근하면 매번 이전 배열과 현재 배열
구분할 수 있을 것

2. 수학으로 풀이하기
전체 돼지들이 원하는 양은
본인 양 + 양 옆 + 맞은 편 돼지 양이므로
한 돼지의 양이 총 4배로 늘어나게 될 것

돼지 밥 -> 돼지 밥 * 4 -> 돼지밥 * 4 * 4
로 4의 제곱수가 곱해질 것
돼지 밥 * 4 ^ x > N 을 구하기
(x <= (log(N) - log(total_pigs)) / log(4) 이면 가능)
(x > (log(N) - log(total_pigs)) / log(4) 부터 불가능)
log 내의 곱은 + 로 변경 가능
지수는 log 의 앞에 곱해진 상수로 변경 가능

(첫째날, 둘째날 변경되는 거 따져보기)
1 2 3 4 5 6
1 2 3 4 5 6 = 21
13 11 15 13 17 15 = 84

랜덤 인풋 생성을 해보니 N 범위를 크게 했을 때는 오히려 반례가 안 나왔는데
N 이 작을 때 반례가 나왔다
-1 이 나오는 경우가 있었다.
log 연산 결과 음수가 나오는 걸 다 0으로 처리해야할 것 같다.

반례
1
5
36 50 39 29 7

최종 제출 솔루션이
O(1) 인데 왜 반복문을 돈 코드는 36 ms 이고, 내 코드는 40 ms 인지 모르겠다...
"""
# 속도 개선 용으로 input 넣어보기 (68 ms -> 40 ms)
# => https://www.acmicpc.net/source/52481640 1등 python3 코드 참고

import math
import sys
input = sys.stdin.readline
for tc in range(int(input())):
    N = int(input())
    pigs = map(int, input().split())
    total_pigs = sum(pigs)
    day = math.floor(1 + (math.log(N) - math.log(total_pigs)) / math.log(4))
    if day <= 0: # log 로 인한 음수 예외처리
        print(1)
    else:
        print(day+1)

# 36 ms python3 코드
# https://www.acmicpc.net/source/52481640
"""
import sys;input=sys.stdin.readline
for _ in range(int(input())):
  k=int(input());d=s=0
  p=[*map(int,input().split())]
  s=sum(p)
  while 1:
    d+=1
    if sum(p)>k:break
    w=[0]*6
    for i in range(6):
      w[i]=p[i]+p[(i+5)%6]+p[(i+1)%6]+p[(i+3)%6]
    p=w
  print(d)
"""

# 틀린 코드
"""
import math

for tc in range(int(input())):
    N = int(input())
    pigs = map(int, input().split())
    total_pigs = sum(pigs)
    # x * log(4) + log(total_pigs) > log(N)
    #x <= (log(N) - log(total_pigs)) / log(4) 이면 가능
    print(math.floor(2 + (math.log(N) - math.log(total_pigs)) / math.log(4)))
"""

# 비교 정답 코드
# https://wondytyahng.tistory.com/entry/%EB%B0%B1%EC%A4%80-3060-%EC%9A%95%EC%8B%AC%EC%9F%81%EC%9D%B4%EB%8F%BC%EC%A7%80?category=1017393
"""
for _ in range(int(input())):
    N = int(input())
    food = sum(list(map(int, input().split())))
    day = 1
    while N >= food:
        day += 1
        food *= 4
    print(day)
"""
