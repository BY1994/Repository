"""
14501 퇴사

DP

N+1 일 째 퇴사이기 때문에
DP 배열에 N+1 번째까지 배열이 있어야함 (1일 동안 얻는 이득을 +1 된 위치에 계산할 거니까)
DP 배열 인덱스 -1 할 때 예외 처리 귀찮아서 인덱스를 1부터 시작하게 함

아래 예제 4 틀린 이유는, nextday 만 업데이트를 시켜줬는데,
선택을 안 하고 넘어가는 경우를 고려 안 했음
선택하지 않고 이전 값을 그대로 넘겨받는 경우 추가하고 맞음
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
정답 90
내 답 80

지금 제출된 버전 코드에서 cursum[day] = cursum[day-1] 만 해도 될 듯
max 는 필요 없을 듯. 어차피 그 인덱스는 한 번만 방문하는 것이기 때문에.
=> 잘못 생각... 지금 인덱스가 비어있다고 생각했는데, 지금의 최대값고 과거에 어느 시점에 여길 nextday 라고 생각하고 업데이트한 것
참고 코드가 끝에서부터 채웠기 때문에 무조건 그 인덱스가 비어있었는데, 그걸 보고 착각함
"""

# 정답 코드
N = int(input())
arr = [[0 for i in range(2)] for j in range(N+1)]
for i in range(1, N+1):
    T, P = map(int, input().split())
    arr[i][0] = T
    arr[i][1] = P
cursum = [0]*(N+2)

ans = 0
for day in range(1,N+1):
    nextday = day + arr[day][0]
    # default - 선택하지 않은 day 도 고려. 이전동안 선택 최대 값을 가져옴
    cursum[day] = max(cursum[day], cursum[day-1])
    # 이번 턴에서 선택을 함
    if nextday <= N+1:
        cursum[nextday] = max(cursum[nextday], cursum[day] + arr[day][1])
        ans = max(ans, cursum[nextday])

print(ans)

# 참고
# https://www.acmicpc.net/source/18687242
"""
n = int(input())
plan = []
benefit = []
for i in range(n):
    plan.append(tuple(map(int,input().split())))
    benefit.append(-1)
benefit.append(0)

if plan[n-1][0] == 1:
    benefit[n-1] = plan[n-1][1]
else:
    benefit[n-1] = 0
    
for i in range(n-2,-1,-1):
    benefit[i] = benefit[i+1]
    if i + plan[i][0] - 1 < n: #선택할 수 있는 경우
        t = plan[i][1] + benefit[i+plan[i][0]]
        if benefit[i] < t:
            benefit[i] = t

print(benefit[0])
"""
