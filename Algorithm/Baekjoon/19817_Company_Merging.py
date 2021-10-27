"""
19817 Company Merging

heap 코드 공식 문서
https://docs.python.org/ko/3/library/heapq.html

그냥 2개씩 계속 합쳐가도 되고, 좌/우 중 누가 큰지 보고
(정렬하면 안 봐도 되고)
max 값 구해서 각 값과 맥스값의 차이를 구해도 되고

결론은 heap 필요 없고 단순 수학이었다.
증명만 할 수 있으면 아주 간단한 코드로 풀 수 있다

아래와 같이 도형처럼 표현을 하면,
어떤 식으로 합쳐도
결과적으로 가장 max 인 것을 기준으로
생겨나는 빗금친 부분은 항상 동일하다

금액축
|
|
|//ㅁ//
|//ㅁㅁ
|ㅁㅁㅁ
__________ 인원수


금액축
|
|
|////ㅁ
|//ㅁㅁ
|ㅁㅁㅁ
__________ 인원수

"""

# 시간초과 => append를 배열로 접근?
# pypy 로 제출하고 맞았다
n = int(input())
totalm = 0
ans = 0
h = []
#h = [[0, 0] for _ in range(n)]

for i in range(n):
    info = list(map(int, input().split()))
    m = max(info[1:])
    if totalm < m: totalm = m
    #h[i][0] = m
    #h[i][1] = info[0]
    h.append([m, info[0]])

for i in range(n):
    ans += (totalm - h[i][0]) * h[i][1]

print(ans)

"""
import heapq

ans = 0
h = []
for _ in range(int(input())):
    info = list(map(int, input().split()))
    heapq.heappush(h, (max(info[1:]), info[0]))

print(h)

while (len(h) > 1):
    firstm, firstnum = heapq.heappop(h)
    secondm, secondnum = heapq.heappop(h)
    ans += (secondm - firstm) * firstnum

    heapq.heappush(h, (secondm, secondnum+firstnum))
    
print(ans)
"""
