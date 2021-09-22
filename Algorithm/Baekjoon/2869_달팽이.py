"""
2869 달팽이는 올라가고 싶다

미리 반례로 생각해 볼 것
A 가 V보다 큰 경우? => 문제 조건을 보면 그런 경우는 없다.

참고
이분 탐색 방법이 가능하다고 하다
"""

A, B, V = map(int, input().split())

step = A-B

days = V - A
ans = 1 + (days // step) + int(not(not(days % step)))

print(ans)


#days = (V // step) + int(not(not(V % step)))
#if (days -1) * step + A >= V: ans = days-1
#else: ans = days
