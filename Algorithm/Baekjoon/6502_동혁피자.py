"""
6502 동혁 피자

피타고라스 정리
원형 테이블 안에 직사각형 피자가 들어오는지 검사
(대각선이 테이블의 지름보다 같거나 작으면 된다.)
"""

pizza = 0
while True:
    pizza += 1
    num = input()
    if num == '0': break
    r, w, l = map(int, num.split())
    if w**2 + l**2 <= (2*r) ** 2:
        print(f'Pizza {pizza} fits on the table.')
    else:
        print(f'Pizza {pizza} does not fit on the table.')
