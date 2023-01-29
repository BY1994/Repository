"""
4880 다음수

등차수열, 등비수열
"""

while True:
    a1, a2, a3 = map(int, input().split())
    if a1 == 0 and a2 == 0 and a3 == 0:
        break
    if a3 - a2 == a2 - a1:
        print(f"AP {a3 - a2 + a3}")
    else:
        print(f"GP {a3*(a3//a2)}")
