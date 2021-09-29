"""
Codeforces Round #744 (Div.3)

B의 개수가 A의 개수 + C의 개수이면 됨

6
ABACAB
ABBA
AC
ABC
CABCBB
BCBCBCBCBCBCBCBC
"""

t = int(input())
for _ in range(t):
    string = input()
    print("YES" if string.count('B') == string.count('A')+string.count('C') else "NO")
