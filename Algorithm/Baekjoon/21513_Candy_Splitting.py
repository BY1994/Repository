"""
12513 Candy Splitting (Small)
12514 Candy Splitting (Large)

비트마스킹
2011 Codejam Qualification Round

input 시간 오래 걸리는 거 수정해야하는데 안 했음
2^15 이므로 완전 탐색 => 실버 난이도
합의 받아올림 빼는 계산 = XOR 계산

large 를 풀기 위해서 알아야하는 것은
2 덩이로 쪼갤 필요도 없다는 것
전체 XOR 한 결과가 0이라면 1개만 제외하면 나머지가 동일하단 의미이기 때문이다.
(2 덩이가 같다면 둘을 XOR 한 결과도 0이라는 것이고, 전체가 0 이면 1개를 제외한 나머지도 같아짐)
"""

# small
"""
for tc in range(int(input())):
    N = int(input())
    C = list(map(int, input().split()))
    ans = -1
    for i in range(1, (1 << N)-1): # 넣을지 말지 결정, 0 이랑 1 << N 빼기 -1 => 다 뺐는 것
        A, B, Sean = 0, 0, 0
        for j in range(N):
            if (i >> j) & 1:
                B ^= C[j]
                Sean += C[j]
            else: A ^= C[j]
        if A == B:
            ans = max(ans, Sean)
    if ans == -1:
        print(f"Case #{tc+1}: NO")
    else:
        print(f"Case #{tc+1}: {ans}")
"""

# large
for tc in range(int(input())):
    N = int(input())
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans ^= C[i]
    if ans == 0:
        C.sort()
        print(f"Case #{tc+1}: {sum(C[1:])}")
    else:
        print(f"Case #{tc+1}: NO")

