A, B, C, X = map(int, input().split())
if A >= X:
    print(1.000000000000)
else:
    if B < X:
        print(0.000000000000)
    else:
        print(C / (B-A))
