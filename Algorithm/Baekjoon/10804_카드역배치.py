"""
10804 카드 역배치

Google code jam reverse sort 와 같은 문제
"""


cards = list(range(1, 21))
for _ in range(10):
    start, end = map(int, input().split())
    cards[start-1:end] = cards[start-1:end][::-1]

print(*cards)
