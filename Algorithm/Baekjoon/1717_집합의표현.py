"""
1717 집합의 표현
union find

2022.06.01 통과 PBY

실수 포인트
1. Recursion Error
recursion limit 풀어주는 거 안 함
2. 틀렸습니다
parent[parenta] = parentb 로 안 하고
parent[a] = parentb 로 해서
parenta 는 부모가 바뀌지 않았음
3. 틀렸습니다
for 문을 n 까지 돌아야하는데,
n+1 이 아니라 n 으로 해서 잘못됨
4. 틀렸습니다
비교시 find(a) == find(b) 이렇게 해서
최상위 부모를 비교해야하는데,
parent[a] == parent[b] 이렇게 비교해서
union 되었을 때 a 의 부모로 parenta 가 들어있을 때,
parenta 의 부모가 parentb 인 경우가 있을 수 있음
그럴 때는 find(a) == find(b) 해야만 커버됨
"""
import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def find(a):
    if parent[a] == a:
        return a
    parenta = find(parent[a])
    parent[a] = parenta
    return parenta

def union(a, b):
    parenta = find(a)
    parentb = find(b)

    if parenta != parentb:
        parent[parenta] = parentb

n, m = map(int, input().split())
parent = [0]*1000001

for i in range(n+1):
    parent[i] = i

for i in range(m):
    op, a, b = map(int, input().split())
    if op:
        print("YES" if find(a) == find(b) else "NO")
    else:
        union(a, b)
