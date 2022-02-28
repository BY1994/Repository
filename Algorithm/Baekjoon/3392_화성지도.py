"""
3392 화성 지도

세그먼트 트리 응용 문제
해답을 알지 못해서 다른 풀이를 보고 공부
https://4legs-study.tistory.com/126
https://mangu.tistory.com/76?category=937146
https://jason9319.tistory.com/58

y 좌표만 세그먼트 트리로 관리
지도 점이 하나라도 존재하는 y 값들의 합을 구하도록

10 10 20 20
15 15 25 30

x = 10 일 때,
y = 10, 11, 12, ..., 20
=> 10 ~ 20 범위를 +1 시킴 => 이전 수직선과의 차이만큼 곱해 더하기
아님, 여기 10~19 까지만 해야함. 그래야 개수의 합이 20이 나옴
x = 11 일 때,
y = 10, 11, 12, ..., 20
...
x = 15 일 때, (두 사각형 겹침)
y = 10, 11, 12, 13, ..., 30
x = 16 일 때,
y = 10, 11, 12, 13, ..., 30
...
x = 20 일 때, 두 사각형 겹치지만, 밑에 사각형은 이 때 고려하면 안 됨
y = 25, 26, 27, 28, 29, 30
x = 21 일 때, 사각형 겹치지 않음
y = 25, 26, 27, 28, 29, 30
"""

#################################################
# segment tree
#################################################
def update(node, start, end, left, right, val):
    if end < left or start > right: return
    if left <= start and end <= right:
        cnt[node] += val # start +1, end -1
    else:
        mid = start + (end-start)//2
        update(node*2, start, mid, left, right, val)
        update(node*2+1, mid+1, end, left, right, val)
        # cnt = 0 # default value

    if cnt[node] > 0:
        seg[node] = end - start + 1
    else:
        # leaf node 는 합도 0 # if s == e 처리 해주면 seg, cnt 크기 *2 안 필요
        seg[node] = seg[node*2] + seg[node*2+1]

seg = [0] * 30001*2*4 # the total number of points in section not including overlap
cnt = [0] * 30001*2*4 # the total number of points in section, including overlap, 0 = no point, >1 = points exist

#################################################
# input & sort
#################################################
my_map = []
N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    my_map.append((x1, y1, y2-1, 1)) # start
    my_map.append((x2, y1, y2-1, -1)) # end
    

my_map.sort() # sort based on x

#################################################
# sweeping by segment tree
#################################################
ans = 0

# first x
x, y1, y2, val = my_map[0]
update(1, 0, 30000, y1, y2, val) # val = start or end

# from second x
for i in range(1, N*2):
    x_diff = my_map[i][0] - my_map[i-1][0]
    ans += x_diff * seg[1] # the total number of points
    update(1, 0, 30000, my_map[i][1], my_map[i][2], my_map[i][3])

print(ans)
