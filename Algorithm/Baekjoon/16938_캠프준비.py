"""
16938 backtracking & bitmask

모든 경우의 수는 2**15 = 32768
1부터 32768 까지 순회하며 다 확인하는 방법도 가능할 것 같고,
가지치기가 가능하게 하고자 재귀로 작성하였다
(가지지치 안 넣고도 통과하였다)
"""

def select_problem(cur, visited, num, total, _max, _min):
    global ans, N, L, R, X
    if num >= 2 and total >= L and total <= R and _max - _min >= X:
        ans += 1

    for i in range(cur+1, N):
        select_problem(i, visited | (1 << cur), num+1, total + difficulties[i], max(_max, difficulties[i]), min(_min, difficulties[i]))
    
N, L, R, X = map(int, input().split())
difficulties = list(map(int, input().split()))
ans = 0

for i in range(N):
    select_problem(i, i, 1, difficulties[i], difficulties[i], difficulties[i])

print(ans)
