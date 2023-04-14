"""
3135 라디오

그리디

반례
1 3
1
5
오답 3
정답 2
https://www.acmicpc.net/board/view/60200

_min > abs(A-B) 라고 조건을 써서 틀렸었는데,
같은 경우에 결국 print 는 _min+1 이 되므로
같으면 무조건 abs(A-B) 가 이겨야하는게 맞다.
아니면 _min+1 > abs(A-B) 를 비교하거나 해야한다.
"""

A, B = map(int, input().split())
_min = 9999
for i in range(int(input())):
    f = int(input())
    _min = min(_min, abs(B-f))
if _min >= abs(A-B):
    print(abs(A-B))
else:
    print(_min+1)
