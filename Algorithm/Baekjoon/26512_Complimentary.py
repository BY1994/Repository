"""
26512 Complimentary

2의 보수 문제
음수를 2의 보수 (반전 후 +1) 로 출력하기
8자리만 출력해야하기 때문에 zfill 을 사용했고,
음수를 format 하거나 bin 을 해도 - 가 그대로 나와서 8 자리로 제한해줬다.
"""

while True:
    X, Y = map(int, input().split())
    if X == 0 and Y == 0: break
    print(f"{X} = {format(X,'b').zfill(8)}")
    print(f"{Y} = {format(Y,'b').zfill(8)}")
    print(f"{-X} = {format((-X)&0xff,'b').zfill(8)}")
    print(f"{-Y} = {format((-Y)&0xff,'b').zfill(8)}")
    print(f"{X-Y} = {format((X-Y)&0xff,'b').zfill(8)}")
    print()
