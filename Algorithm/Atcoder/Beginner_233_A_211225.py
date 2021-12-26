# 233 Atcoder

a, b = map(int, input().split())
stamp = b - a
if stamp <= 0:
    print(0)
else:
    print((stamp+9) // 10)
