"""
2720 세탁소

그리디
동전 개수 최소화하는 문제
"""

for tc in range(int(input())):
    c = int(input())
    print(c//25, end=" ")
    c %= 25
    print(c//10, end=" ")
    c %= 10
    print(c//5, end=" ")
    c %= 5
    print(c, end=" ")
    print()
