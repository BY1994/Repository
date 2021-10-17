"""
C

문제에 거리와 속도가 나왔으니까
시간을 구해서 반을 나누면 된다.

거리 = 속도 x 시간
시간 = 거리 / 속도
"""

N = int(input())
total_time = 0
total_dist = 0
a = []
for _ in range(N):
    dist, speed = map(int, input().split())
    a.append([dist, speed])
    total_time += dist / speed

total_time /= 2
for i in range(N):
    dist = a[i][0]
    speed = a[i][1]
    if total_time >= dist / speed:
        total_time -= dist / speed
        total_dist += dist
    else:
        total_dist += speed * total_time
        break
    
print(total_dist)
    
