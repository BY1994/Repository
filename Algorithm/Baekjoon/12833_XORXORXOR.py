"""
12833 XORXORXOR

(A^B)^B 하면
A 나옴

짝수번 하면 A
홀수번하면 xor
"""

A, B, C = map(int, input().split())

print(A^(B*(C % 2)))
