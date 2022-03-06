"""
index가 10**18 라는 제한이 있어서
숫자가 엄청 커지면 최초 부모 index 가 결국 0 밖에 안 됨
재귀로는 // 2 해서 log 로 들어감

ABC
->
BCCAAB
//2 해서 transfrom N 번 전 상태로 가서
구해와야함...

1번 transform 하고 1번 구하라고 하면
0//2 -> 0
A 에서 1번 transform 해서 BC 구하고,
BC 중 1번... (0번)

1번 trasnform 하고 2번 구하라고 하면
1//2 -> 0
A에서 1번 transfrom 해서 BC 구하고,
BC 중 2번

A B C
BC CA AB
CA AB AB BC BC CA
AB BC BC CA BC CA CA AB CA AB AB BC
BC CA CA AB
// 한 값이 부모, % 한 값이 첫번째인지 두 번째인지
"""
# 내 답안 (재귀 아닌 버전) - 시간초과
"""
child = {'A':'BC', 'B':'CA', 'C':'AB'}
S = input()
Q = int(input())
for _ in range(Q):
    t, k = map(int, input().split())
    k -= 1
    parent_id = k // (2**t)
    parent = S[parent_id]
    for i in range(t):
        if k & (1<<i):
            parent = child[parent][1]
        else:
            parent = child[parent][0]
    print(parent)
"""
# Atcoder 모범 답안
# 다른 참가자 답안 참고 https://atcoder.jp/contests/abc242/submissions/29854010
"""
S = input()
Q = int(input())
 
def g(s,add):
    return chr((ord(s)-ord('A')+add)%3+ord('A'))
 
def f(t,k):
    if k == 0:
        return g(S[0],t)
    if t == 0:
        return S[k]
    return g(f(t-1,k//2),k%2+1)
 
for i in range(Q):
    t,k = map(int,input().split())
    print(f(t,k-1))
"""
# 내 답안 (재귀 버전) - 시간초과
import sys
sys.setrecursionlimit(2**31-1)

def recursive(transform, index):
    if transform == 0:
        return S[index]
    parent = recursive(transform-1, index//2)
    return child[parent][index%2]

child = {'A':'BC', 'B':'CA', 'C':'AB'}
S = input()
Q = int(input())
for _ in range(Q):
    t, k = map(int, input().split())
    print(recursive(t, k-1))

