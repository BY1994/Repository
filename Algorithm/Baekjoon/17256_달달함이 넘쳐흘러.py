"""
17256 달달함이 넘쳐흘러

input)
15 16 17
19 32 90

2019.06.20 PBY 최초작성
"""

ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

print(cx-az, cy//ay, cz-ax)
