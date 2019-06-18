"""
facebook Hacker Cup 2019 Qualification Round 
Leapfrog: Ch.1

Input)
8
A.
AB.
ABB
A.BB
A..BB..B
A.B..BBB.
AB.........
A.B..BBBB.BB

2019.06.15 PBY 최초 작성
"""

# input
N = int(input())
for case in range(N):
    colony = input()
    numB = 0
    numdot = 0
    for lilypad in colony:
        if lilypad == "B":
            numB += 1
        elif lilypad == ".":
            numdot += 1
    ans = "N"
    if numdot > 0 and numB >= numdot:
        ans = "Y"
    print("Case #%d: %s" %(case+1, ans))
