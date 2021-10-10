"""
1085 직사각형 탈출

입력을 보고 푸는 방법을 생각하다가
당연히 오른쪽 상단 꼭지점으로 가야한다고 착각하였다.
상하좌우 어디든 가까운 곳에 가면 된다. x, y, w-x, h-y 중 가장 짧은 거리로 가면 된다.
"""
x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))

# 문제 잘못 이해함
"""
x, y, w, h = map(int, input().split())
print(w-x if w-x < h-y else h-y)
"""
