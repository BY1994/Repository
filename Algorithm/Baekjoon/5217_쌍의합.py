"""
5217 쌍의 합

구현
"""

for tc in range(int(input())):
    n = int(input())
    print(f"Pairs for {n}:", end="")
    ans = []
    for i in range(1, n):
        for j in range(i+1, n):
            if i + j == n:
                ans.append(f" {i} {j}")
    print(','.join(ans))
