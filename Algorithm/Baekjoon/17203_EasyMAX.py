"""
BOJ 17203
∑|ΔEasyMAX|

2019.06.12 최초 작성
"""

# input
N, Q = map(int, input().split())
beats = list(map(int, input().split()))
beats_s = [0] * (N-1)

# predefine
for b in range(N-1):
    beats_s[b] = abs(beats[b+1]-beats[b])

# answer
for q in range(Q):
    start, end = map(int, input().split())
    print(sum(beats_s[start-1:end-1]))

"""
1. 틀렸습니다 - 절대값 고려 안 함!
2. 수정 후 정답!
"""
