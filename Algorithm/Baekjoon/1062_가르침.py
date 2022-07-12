"""
1062 가르침

백트래킹

시간초과 나는 테스트케이스
https://www.acmicpc.net/board/view/62036

속도 개선 방법
K 가 5 이상일 때만 백트래킹, 그 아래는 읽을 수 있는 단어 0개
https://www.acmicpc.net/board/view/13447
가지치기를 하면 약 30 배는 빨라진다. (26개 알파벳 다 보다가 21 개만 보면 되니까, 2^5 이 없어짐)

처음에 생각한 것은 2**26 정도니까 가지치기 없이도 가능하다고 생각했는데,
2**26 * 50 까지 고려하면 (최종적으로 모든 word 돌면서 확인하니까)
시간 안에 들어올 수가 없다!!
"""

# 가지치기 버전 (통과)
import sys
sys.setrecursionlimit(10000000)

def backtracking(cur, count, depth):
    global ans, N, K

    if count >= K:
        possible = 0
        for i in range(N):
            if (cur & words[i]) == words[i]:
                possible += 1
        ans = max(ans, possible)
        return

    for i in range(depth, 26):
        if visited[i] == 1:
            continue
        visited[i] = 1
        backtracking(cur | (1 << i), count+1, i+1)
        visited[i] = 0

N, K = map(int, input().split())
visited = [0]*26
words = [0]*N
a = ord('a')
ans = 0
visited[0] = 1 # a
visited[2] = 1 # c
visited[8] = 1 # i
visited[13] = 1 # n
visited[19] = 1 # t

for i in range(N):
    word = input()
    for j in word:
        words[i] |= 1 << (ord(j) - a)

if K < 5:
    print(0)
else:
    backtracking(0x82105, 5, 0)
    print(ans)


# 느린 버전
"""
import sys
sys.setrecursionlimit(10000000)

def backtracking(cur, count, depth):
    global ans, N, K

    if count >= K:
        possible = 0
        for i in range(N):
            if (cur & words[i]) == words[i]:
                possible += 1
        ans = max(ans, possible)
        return

    for i in range(depth, 26):
        backtracking(cur | (1 << i), count+1, i+1)

N, K = map(int, input().split())
words = [0]*N
a = ord('a')
ans = 0
for i in range(N):
    word = input()
    for j in word:
        words[i] |= 1 << (ord(j) - a)

backtracking(0, 0, 0)
print(ans)
"""
