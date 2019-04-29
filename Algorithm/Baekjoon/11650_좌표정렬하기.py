"""
11650_좌표 정렬하기

2019.04.29 PBY 최초 작성
"""

N = int(input())
array = []
for i in range(N):
    array.append(list(map(int, input().split())))

array.sort(key = lambda x: (x[0], x[1]))

for i in range(N):
    print(array[i][0], array[i][1])