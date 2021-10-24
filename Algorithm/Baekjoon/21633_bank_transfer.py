"""
21633 Bank Transfer

Russia High School Programming Contest
"""


N = int(input())
com = 25 + (N * 0.01)
if com < 100:
    com = 100
if com > 2000:
    com = 2000
print("{:.2f}".format(com))
