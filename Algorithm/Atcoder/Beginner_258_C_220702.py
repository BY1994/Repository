"""
Atcoder 258 (2022.07.02)

끝에 있는 글자를 맨 앞으로 이동 시키는 쿼리와,
이동된 상태에서 몇 번째 글자를 출력해달라는 쿼리가 들어옴

실제로 글자를 이동시킬 필요 없이, 원형 큐 생각하면서 offset 만 이동시켰다
"""

N, Q = map(int, input().split())
S = input()
offset = 0
for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        offset = (offset+N-x)%N
    else:
        print(S[(offset+x-1)%N])
        
