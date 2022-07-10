"""
11723 집합

비트연산 연습
수행해야하는 연산의 수가 3,000,000 이기 때문에,
empty 를 비트를 이용하여 한번에 하지 않으면 시간 복잡도 안에 들어오지 못할 것
"""

import sys
input = sys.stdin.readline
myset = 0
M = int(input())
for i in range(M):
    cmd = input()[:-1]
    if cmd == "all":
        myset = 0x1FFFFE
    elif cmd == "empty":
        myset = 0
    else:
        cmd, x = cmd.split()
        x = int(x)
        if cmd == "add":
            myset |= (1 << x)
        elif cmd == "remove":
            myset &= ~(1 << x)
        elif cmd == "check":
            print((myset >> x)&0x1)
        elif cmd == "toggle":
            myset ^= (1 << x)

