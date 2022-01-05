"""
14465 소가 길을 건너간 이유 5

누적합하고 맨 앞과 맨 끝 차이로 범위 내 개수 찾기
range의 종료 값 찾는 거를 헷갈려서 한 번 틀림
"""

N, K, B = map(int, input().split())
sign = [0]*100001
for _ in range(B):
    sign[int(input())] = 1

for i in range(1,N+1):
    sign[i] += sign[i-1]

ans = N
for i in range(1, N-K+2):
    temp = sign[i+K-1] - sign[i-1]
    if ans > temp:
        ans = temp

print(ans)
