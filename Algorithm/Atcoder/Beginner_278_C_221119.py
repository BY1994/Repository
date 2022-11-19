# 처음 내서 틀린 거
"""
N, Q = map(int, input().split())
follow = {}
for i in range(Q):
    T, A, B = input().split()
    if T == '1': # follow
        if A in follow:
            if follow[A]:
                if B not in follow[A]: # 틀린 부분!! 0 인 경우도 업데이트 시켜줘야함!!!
                    follow[A][B] = 1
            else:
                follow[A] = {B:1}
        else:
            follow[A] = {B:1}
    elif T == '2': # unfollow
        if A in follow:
            if follow[A]:
                if B in follow[A]:
                    follow[A][B] = 0
    else: # query
        flag = 0
        if A in follow and follow[A]:
            if B in follow[A]:
                if follow[A][B] == 1:
                    flag += 1
        if B in follow and follow[B]:
            if A in follow[B]:
                if follow[B][A] == 1:
                    flag += 1
        if flag == 2:
            print('Yes')
        else:
            print('No')
"""
N, Q = map(int, input().split())
follow = {}
for i in range(Q):
    T, A, B = input().split()
    if T == '1': # follow
        if A in follow:
            if follow[A]:
                follow[A][B] = 1
            else:
                follow[A] = {B:1}
        else:
            follow[A] = {B:1}
    elif T == '2': # unfollow
        if A in follow:
            if follow[A]:
                follow[A][B] = 0
    else: # query
        flag = 0
        if A in follow and follow[A]:
            if B in follow[A]:
                if follow[A][B] == 1:
                    flag += 1
        if B in follow and follow[B]:
            if A in follow[B]:
                if follow[B][A] == 1:
                    flag += 1
        if flag == 2:
            print('Yes')
        else:
            print('No')

"""
from collections import defaultdict

N, Q = map(int, input().split())
d = defaultdict(set)

for i in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        d[A].add(B)
    elif T == 2:
        if B in d[A]:
            d[A].remove(B)
    else:
        if B in d[A] and A in d[B]:
            print('Yes')
        else:
            print('No')
"""
