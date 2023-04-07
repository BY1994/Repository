"""
1817 짐 챙기는 숌

그리디

cur = 0 대신
cur = M 을 미리 넣으면 if 문으로 처리하기 어려움
"""

N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    books = list(map(int, input().split()))
    box = 1
    cur = 0
    for book in books:
        if cur + book > M:
            box += 1
            cur = book
        else:
            cur += book
    print(box)
