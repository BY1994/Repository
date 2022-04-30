"""
A Punched Cards
"""

for tc in range(1, int(input())+1):
    R, C = map(int, input().split())
    print(f"Case #{tc}:")
    # 2 line
    print(".." + "+-"*(C-1)+"+")
    print(".." + "|."*(C-1)+"|")
    for row in range(R-1):
        print("+-"*(C)+"+")
        print("|."*(C)+"|")
    print("+-"*(C)+"+")
