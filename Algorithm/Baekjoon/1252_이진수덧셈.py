"""
1252 이진수 덧셈
"""

a, b = input().split()
anum = 0
bnum = 0
for i in a:
    anum *= 2
    anum += ord(i) - 48
for i in b:
    bnum *= 2
    bnum += ord(i) - 48

print(bin(anum+bnum)[2:])
