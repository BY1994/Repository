"""
2217 로프

2
10
15
정답 20

반례
https://www.acmicpc.net/board/view/79515
4
3
3
3
10
맞는 답 12
틀린 답 10
"""

N = int(input())
rope = []
for i in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)
ans = 0
for k in range(N):
    # k 까지 들어갔을 때 최대 무게
    w = rope[k]*(k+1)
    if ans <= w:
        ans = w

print(ans)

# 틀렸습니다
# 안 된다고 바로 break 하면 위의 반례 커버 안 됨 
"""
N = int(input())
rope = []
for i in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)
ans = 0
for k in range(N):
    # k 까지 들어갔을 때 최대 무게
    w = rope[k]*(k+1)
    if ans <= w:
        ans = w
    else:
        break

print(ans)
"""

# 예제도 틀림
# 이렇게 하면 15 에서 멈춰버림
"""
N = int(input())
rope = []
for i in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)
w = 0
for k in range(N):
    if rope[k] >= (w + rope[k]) / (k+1):
        w += rope[k]
    else:
        break

print(w)
"""
