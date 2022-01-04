"""
15961 회전 초밥

틀렸습니다 => 회전 초밥인데, 회전을 고려 안 함!

반례
8 30 4 30
9
25
7
9
7
30
2
7
5가 나와야하는데, 4가 나왔음

회전 고려 안 한 추가 반례
8 30 4 30
2
3
9
9
9
9
2
3
답 5 나와야함 2 3 2 3 + 30 해서

그래도 틀렸습니다 => 빼고 더해서 여전히 1일 수도 있음
if ==1 체크를 빼고 더할 때 직후에 해야함
반례
8 30 4 30
7
9
7
30
2
9
7
25
답 5인데, 7이 나왔음

# 질문답변을 보고 반례 만들기
https://www.acmicpc.net/board/view/80235
처음 k 안에 30 이 없어서 a 변수 체크 안 되게...
8 30 4 30
7
9
7
2
30
2
9
7
그러면 답은 4가 나와야함

8 30 4 30
7
9
7
30
2
9
7
30
4가 나옴

8 30 4 30
7
9
7
25
2
7
9
30

8 30 4 30
2
3
4
5
30
30
2
30

8 30 4 30
2
3
4
30 (B+1 시키고)
30 (A[k] == c 로 counter +1)
2
3
30
답 4

a+1 되고, 2,3,4,30 으로 답은 4
8 30 4 30
2
3
4
4
2
3
4
4

반례 만들기 실패...
"""

N, d, k, c = map(int, input().split())
dish = []
eat = [0]*(d+1)
for _ in range(N):
    dish.append(int(input()))

# 초기 k 접시 & c 쿠폰 사용
ans = 0
cur = 1
eat[c] += 1
for i in range(k):
    eat[dish[i]] += 1
    if eat[dish[i]] == 1:
        cur += 1
ans = cur

for i in range(1, N):
    # 맨 앞은 빼고, 맨 뒤는 넣고
    _prev = (i-1) % N
    _next = (i-1+k) % N

    # sliding window 벗어난 범위 -1
    eat[dish[_prev]] -= 1
    if eat[dish[_prev]] < 1:
        cur -= 1

    # sliding window 들어오는 범위 +1
    eat[dish[_next]] += 1
    if eat[dish[_next]] == 1: # 계속 1개만 있으면 cur 이 +1 이 계속 될 수도
        cur += 1

    if ans < cur:
        ans = cur
    
print(ans)


# 틀린 코드
"""
N, d, k, c = map(int, input().split())
dish = []
eat = [0]*(d+1)
for _ in range(N):
    dish.append(int(input()))

# init
ans = 0
cur = 1
eat[c] += 1
for i in range(k):
    eat[dish[i]] += 1
    if eat[dish[i]] == 1:
        cur += 1
ans = cur

for i in range(1, N-k+1):
    # 맨 앞은 빼고, 맨 뒤는 넣고
    _prev = i-1
    _next = i-1+k
    eat[dish[_prev]] -= 1
    eat[dish[_next]] += 1
    if eat[dish[_prev]] < 1:
        cur -= 1
    if eat[dish[_next]] == 1:
        cur += 1

    if ans < cur:
        ans = cur
    
print(ans)
"""
