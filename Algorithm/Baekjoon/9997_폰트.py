"""
9997 폰트

비트마스킹 + 재귀

2022/04/16 제출 틀렸습니다
시간초과 (예상) 및 틀렸습니다 받음
https://www.acmicpc.net/board/view/38021

2022/08/27
모든 테스트 문장 개수를 세야하는데,
조건이 만족되었을 때 바로 return 을 쳤기 때문에 틀림
pypy3 로 제출해서 위의 반례로 인한 시간 초과는 나지 않음
"""

# 참고하기 좋은 방법!!! 조건이 만족되면 더 이상 진행하지 않고, 2의 승수만큼 더해줌
# https://www.acmicpc.net/source/21029931
"""
import sys
import itertools

input = lambda: sys.stdin.readline().rstrip()

def lowercase_string_or_computation(s):
    res = 0
    for c in s:
        res |= 1 << ord(c) - ord('a')
    return res

N = int(input())
words = list()
EXPECTED_SUM = (1 << 26) - 1
res = 0
case_exists = 0

for _ in range(N):
	v = lowercase_string_or_computation(input())
	case_exists |= v
	words.append(v)

def recursive(current_index, current_or_sum):
	global res
	global EXPECTED_SUM
	global words
	global N
	
	if current_or_sum == EXPECTED_SUM:
	    res += 2 ** (N - current_index)
	    return
	if len(words) == current_index:
		return
	else:
		recursive(current_index + 1, current_or_sum)
		recursive(current_index + 1, current_or_sum | words[current_index])

if case_exists == EXPECTED_SUM:
	recursive(0, 0)
print(res)
"""

# 맞았습니다
def recur(cur, value):
    global ans, N

    if value == (1<<26)-1:
        ans += 1

    for i in range(cur+1, N):
        recur(i, value | words[i])

N = int(input())
words = [0] * N
for i in range(N):
    word = input()
    for j in word:
        words[i] |= (1) << (ord(j)-ord('a'))
ans = 0
for i in range(N):
    recur(i, words[i])
print(ans)


# 틀렸습니다
"""
def recur(cur, value):
    global ans, N

    if value == (1<<26)-1:
        ans += 1
        return

    for i in range(cur+1, N):
        recur(i, value | words[i])

N = int(input())
words = [0] * N
for i in range(N):
    word = input()
    for j in word:
        words[i] |= (1) << (ord(j)-ord('a'))
ans = 0
for i in range(N):
    recur(i, words[i])
print(ans)
"""
