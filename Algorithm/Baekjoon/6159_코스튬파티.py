"""
6159 코스튬 파티

투 포인터
소를 2마리 선택하기 때문에 투 포인터 문제가 됨

잘못 생각한 부분 p1 p2 만족되었을 때 p1 을 증가시킬 일은 없고 p2 만 계속 증가시킴
쌍이 더 있는데 찾지 않고 종료됨

p1 p2 를 양 끝에 두고, p2 를 S 범위 안에 들어오도록 줄여감
개수 합산하고 다 구하면 p1 을 하나 증가하고 p2 를 더 줄임
"""

# 로직 점검하고 다시 짰는데 코드가 오히려 간단해짐!!
N, S = map(int, input().split())
cow = []
for i in range(N):
    cow.append(int(input()))
cow.sort()

p1, p2 = 0, N-1
ans = 0

while p1 < p2:
    if cow[p1] + cow[p2] <= S:
        ans += p2 - p1
        p1 += 1
    else:
        p2 -= 1

print(ans)

# 생각대로 동작하지 않았음
# 잘못된 코드
"""
p1, p2 = 0, 1
ans = 0

N, S = map(int, input().split())
cow = []
for i in range(N):
    cow.append(int(input()))
cow.sort()

while p2 < N and p1 < p2:
    if cow[p1] + cow[p2] <= S:
        ans += 1
        p2 += 1
    else:
        p1 += 1

print(ans)
"""
