"""
17285 XORChic

input)
U^_U]SXEPYDS@SDOB^_XQ

2019.06.26 PBY 최초작성
"""

T = input()
key = ord(T[0])^ord('C')

for item in T:
    print(chr(ord(item)^key), end='')
