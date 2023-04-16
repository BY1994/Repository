"""
Codejam2023 A round
Illumination Optimization

그리디 문제
최소한의 가로등으로 일직선 도로 최대한 커버하기
오른쪽에 있는 가로등이 내 영역까지 커버 가능하면 건너뛰도록 구현
혹은 왼쪽에서 할당한 가로등이 내 영역가지 커버하면 건너뛰도록 구현

그리고 다 덮지 못하는 경우도 탐지해야한다.
"""

for tc in range(int(input())):
    M, R, N = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 0
    last_right = 0
    if X[0]-R <= 0 and X[N-1]+R >= M:
        for i in range(N):
            if i < N-1 and max(X[i+1] - R, 0) <= last_right:
                continue
            else:
                if max(X[i]-R,0) > last_right:
                    ans = 0
                    break
                ans += 1
                last_right = min(X[i] + R,M)
            if last_right >= M:
                break
    if ans:
        print(f"Case #{tc+1}: {ans}")
    else:
        print(f"Case #{tc+1}: IMPOSSIBLE")

# 틀린 답안
"""
for tc in range(int(input())):
    M, R, N = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 0
    last = -1
    if max(X[0]-R,0) <= 0 and min(X[N-1]+R, M) >= M:
        for i in range(N):
            if last != -1 and min(X[last]+R, M) >= min(X[i]+R,M):
                continue
            if i < N-1 and max(X[i+1]-R, 0) <= max(X[i]-R, 0):
                continue
            if last != -1 and min(X[last]+R,M) < max(X[i]-R,0):
                ans = 0
                break        
            last = i
            ans += 1

    if ans:
        print(f"Case #{tc+1}: {ans}")
    else:
        print(f"Case #{tc+1}: IMPOSSIBLE")
"""
