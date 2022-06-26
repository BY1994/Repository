"""
2470 두 용액

투 포인터

https://www.acmicpc.net/board/view/53660
7
-99 -2 -1 1 98 100 101
정답 -1 1
내 틀린 답 -99 98

https://www.acmicpc.net/board/view/70531
비슷한 문제들
2467 번과 동일한 문
"""

# 틀렸던 이유: 이전 값보다 이득이면 무조건 줄어들어봐야하는데,
# (지금 당장은 값이 커도 내려가보면 더 좋은 값일 수 있어서)
# 전체 min 값보다 이득이 아니면 멈춰버려서...
N = int(input())
solution = list(map(int, input().split()))
solution.sort()

ans = 2000000000
ansa, ansb = 0, 0

j = N-1
for a1 in range(N-1):
    last = 2000000000
    for a2 in range(j, a1, -1):
        cur = abs(solution[a1] + solution[a2])

        if ans >= cur:
            ans = cur
            ansa, ansb = a1, a2

        if last >= cur:
            j = a2
            last = cur
        else:
            break

print(solution[ansa], solution[ansb])

# 틀렸습니다
"""
N = int(input())
solution = list(map(int, input().split()))
solution.sort()

ans = 2000000000
ansa, ansb = 0, 0

j = N-1
for a1 in range(N-1):
    for a2 in range(j, a1, -1):
        cur = abs(solution[a1] + solution[a2])
        if ans >= cur:
            ans = cur
            ansa, ansb = a1, a2
            j = a2
        else:
            break

print(solution[ansa], solution[ansb])
"""

# 시간초과
"""
N = int(input())
solution = list(map(int, input().split()))
solution.sort()

ans = 2000000000
ansa, ansb = 0, 0

j = N-1
for a1 in range(N-1):
    for a2 in range(j, a1, -1):
        cur = abs(solution[a1] + solution[a2])
        if ans >= cur:
            ans = cur
            ansa, ansb = a1, a2
            j = a2

print(solution[ansa], solution[ansb])
"""

# 풀이 예시
# https://www.acmicpc.net/source/40938959
"""
    for (int l = 0, r = n - 1; l < r; l++) {
        while (r - 1 > l && abs(v[l] + v[r]) > abs(v[l] + v[r - 1])) r--;
        if (mn > abs(v[l] + v[r])) mn = abs(v[l] + v[r]), a = v[l], b = v[r];
    }
"""
