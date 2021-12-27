"""
2776 암기왕
"""

import sys

def binary_search(value):
    global N
    left = 0
    right = N-1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        if note1[mid] == value:
            return 1
        elif note1[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return 0
    

for _ in range(int(input())):
    N = int(input())
    note1 = list(map(int, sys.stdin.readline().split()))
    note1.sort()
    M = int(input())
    note2 = list(map(int, sys.stdin.readline().split()))

    for i in range(M):
        print(binary_search(note2[i]))
