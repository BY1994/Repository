"""
이 문제는 개수가 엄청 많이 들어오기 때문에 일반적인 정렬 방법으로는 못 푼다.
범위가 한정되어있기 때문에 카운팅 소트가 맞다

2020년 풀이 시도 => 메모리 초과
2021년 문제 파악
"""
import sys

counting = [0]*10001
t = int(sys.stdin.readline())
for _ in range(t):
	counting[int(sys.stdin.readline())]+=1

for i in range(10001):
        for j in range(counting[i]):
                sys.stdout.write(str(i) + '\n')

# 시간초과 => 헉 질문답안을 보니 print 를 쓰면 시간초과라고 한다.
"""
counting = [0]*10001
t = int(input())
for _ in range(t):
	counting[int(input())]+=1

for i in range(10001):
        for j in range(counting[i]):
                print(i)
"""

# 메모리 초과 => 원인 print 를 * 해서 문자열로 만든 다음에 하니까
# 문자열이 차지하는 공간이 많았던 것
"""
counting = [0]*10001
t = int(input())
for _ in range(t):
	counting[int(input())]+=1

for i in range(10001):
	if (counting[i]):
		print(f"{i}\n"*counting[i], end='')
"""
