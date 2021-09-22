"""
2869 달팽이는 올라가고 싶다

미리 반례로 생각해 볼 것
A 가 V보다 큰 경우? => 문제 조건을 보면 그런 경우는 없다.

참고
이분 탐색 방법이 가능하다고 하다

java 로 푸는 경우 빠른 입출력 사용이 필요하다
https://www.acmicpc.net/board/view/61920

(V-B-1)/(A-B)+1로 푸는 이유: 나누어 떨어지는 경우와 그렇지 않은 경우 한 번에 만족하도록
https://www.acmicpc.net/board/view/53443
"""

A, B, V = map(int, input().split())

step = A - B
dist = V - A
ans = 1 + (dist // step) + int(not(not(dist % step)))

print(ans)


#days = (V // step) + int(not(not(V % step)))
#if (days -1) * step + A >= V: ans = days-1
#else: ans = days
