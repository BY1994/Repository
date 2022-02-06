"""
24408 Mult

ICPC > Regionals > North America > North America Qualification Contest > ICPC North America Qualifier 2021 H번
"""

import sys
input = sys.stdin.readline

n = int(input())
while n:    
    first = int(input())
    n -= 1
    while n:
        compare = int(input())
        n -= 1
        if compare % first == 0:
            print(compare)
            break
