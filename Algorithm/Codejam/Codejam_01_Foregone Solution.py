# Qualification Round 2019 - 1 Foregone Solution
# 2019.04.06 PBY
"""
input)
3
4
940
4444
"""

# attempt 1 (6 points + Time Limit Exceeded)
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    for i in range(1, N):
        a = i
        b = N-i
        if '4' not in str(a) and '4' not in str(b):
            break
    print("Case #{}: {} {}".format(tc, a, b))
"""

# attempt 2 (6 points + 10 points!)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    b = ''
    for i in str(N):
        if i == '4':
            b += '1'
        else:
            b += '0'
    a = N - int(b)
    
    print("Case #{}: {} {}".format(tc, a, int(b)))
