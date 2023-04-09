"""
4435 중간계 전쟁

구현, 사칙연산
"""

g = (1, 2, 3, 3, 4, 10)
s = (1, 2, 2, 2, 3, 5, 10)
for tc in range(int(input())):
    gn = list(map(int, input().split()))
    sn = list(map(int, input().split()))
    gsum = sum(g[i]*gn[i] for i in range(6))
    ssum = sum(s[i]*sn[i] for i in range(7))
    if gsum > ssum: print(f"Battle {tc+1}: Good triumphs over Evil")
    elif gsum < ssum: print(f"Battle {tc+1}: Evil eradicates all trace of Good")
    else: print(f"Battle {tc+1}: No victor on this battle field")
