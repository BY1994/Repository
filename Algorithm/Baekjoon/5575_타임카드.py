"""
5575 타임 카드

사칙 연산 (시간 계산)
"""
for i in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    time = (h2*3600 + m2*60 + s2) - (h1*3600 + m1*60 + s1)
    print(time//3600, (time%3600)//60, (time%60))
