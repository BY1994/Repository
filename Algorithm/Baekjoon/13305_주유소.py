"""
13305 주유소

그리디
"""
import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split())) # N-1
oil = list(map(int, input().split())) # N

min_oil = oil[0]
cost = road[0] * min_oil

for i in range(1, N-1):
    if oil[i] < min_oil:
        min_oil = oil[i]
    cost += road[i] * min_oil

print(cost)
