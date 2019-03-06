"""
2303 숫자게임

2019.03.06 PBY 최초작성
"""

people = int(input())
maxpeople = 1
maxvalue = 0
for n in range(people):
    cards = list(map(int, input().split()))
    # 카드들 중 세장의 카드를 골라 합을 구한다.
    for i in range(5):
        for j in range(5):
            if i == j:
                continue
            for k in range(5):
                if i == k or j == k:
                    continue
                cursum = (cards[i] + cards[j] + cards[k]) % 10
                if cursum >= maxvalue: # 같은 경우 뒷 사람을 출력해야하니까 =을 추가함 => 이거 안 해서 한 번 틀림
                    maxvalue = cursum
                    maxpeople = n+1

print(maxpeople)