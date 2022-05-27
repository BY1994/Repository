"""
4195

Disjoint set 및 union find 문제

풀이 참고
https://assaeunji.github.io/python/2020-05-05-bj4195/

※ Union find 문제를 풀 때는 find 할 때 부모를 최상위 부모로 업데이트할 것!!!!
(시간 단축 됨)
"""

# 시간 단축을 위해 parent 찾으면 그걸로 변경
import sys
sys.setrecursionlimit(100000000)

def find(index):
    global parents
    if parents[index] == index:
        return index

    p = find(parents[index])
    parents[index] = p
    return p

def union(a, b):
    global friends, parents
    parenta = find(friends[a])
    parentb = find(friends[b])

    if parenta == parentb:
        return count[parentb]

    count[parentb] += count[parenta]
    parents[parenta] = parentb
    return count[parentb]

for tc in range(int(input())):
    F = int(input())
    friends = {}
    frind = 0
    parents = []
    count = []
    for i in range(F):
        a, b = input().split()
        if a not in friends:
            friends[a] = frind
            parents.append(frind)
            count.append(1)
            frind += 1
        if b not in friends:
            friends[b] = frind
            parents.append(frind)
            count.append(1)
            frind += 1

        print(union(a, b))

# 시간초과 난 코드
"""
import sys
sys.setrecursionlimit(100000000)

def find(index):
    global parents
    return index if parents[index] == index else find(parents[index])

def union(parenta, parentb):
    global parents
    count[parentb] += count[parenta]
    parents[parenta] = parentb

for tc in range(int(input())):
    F = int(input())
    friends = {}
    frind = 0
    parents = []
    count = []
    for i in range(F):
        a, b = input().split()
        if a not in friends:
            friends[a] = frind
            parents.append(frind)
            count.append(1)
            frind += 1
        if b not in friends:
            friends[b] = frind
            parents.append(frind)
            count.append(1)
            frind += 1
        parenta = find(friends[a])
        parentb = find(friends[b])
        if parenta != parentb:
            union(parenta, parentb)
        print(count[parentb])
"""
