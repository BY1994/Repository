"""
1330 두 수 비교하기
"""

A, B = map(int, input().split())
D = A-B
print(['==','>'][not not D] if D >= 0 else '<')

# 아래 풀이가 52 ms
"""
a, b = map(int, input().split())
print('>' if a > b else ('<' if a < b else '=='))
"""
"""
a, b = [int(x) for x in input().split()]
print('>' if a > b else ('<' if a < b else '=='))
"""

# 숏코딩
# True False를 이용!!!
"""
a,b=map(int,input().split())
print(['><'[a<b],'=='][a==b])
"""

"""
​a, b = map(int, input().split())
​print(['==', '<>'[a > b]][len({a, b}) - 1]
"""
