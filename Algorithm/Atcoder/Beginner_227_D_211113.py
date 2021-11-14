"""
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

project = 0
_prev = k-2
_next = k-1
#c = 0
# sliding
while True:
    #print(project, _next)
    if _next >= n or _prev < 0:
        break
    project += a[_next]
    #c = a[_next]
    _next += 1
    while a[_prev] - project <= 0 and _prev >= -1:
        _prev -= 1
        _next += 1

print(project)

# k를 뛰어넘으면 sample input 3 답 안 나옴
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

project = 0
prev = 0
# sliding
for i in range(0, n-k+1, k):
    project += a[i] - prev
    prev = a[i]

print(project)
"""
