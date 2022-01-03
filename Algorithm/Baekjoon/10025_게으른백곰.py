"""
10025 게으른 백곰
"""

# -k 부터 +k 범위로 잡아야할 듯
N, K = map(int, input().split())
ans = 0
coor = []
for _ in range(N):
    g, x = map(int, input().split())
    coor.append((x, g))

coor.sort()
p2 = 0
temp = coor[0][1]

for p1 in range(N):
    while p2 < N-1:
        if coor[p2+1][0] - coor[p1][0] > 2*K:
            break
        p2 += 1
        temp += coor[p2][1]

    if ans < temp:
        ans = temp

    temp -= coor[p1][1]

        
print(ans)

# 양동이 좌표만 가능한 줄 알고 잘못 짠 코드
"""
N, K = map(int, input().split())
ans = 0
coor = []
for _ in range(N):
    g, x = map(int, input().split())
    coor.append((x, g))

coor.sort()
p1 = 0
p2 = 0
temp = coor[0][1]
# 각 좌표마다 자리를 잡아보면서
for cur in range(N):
    while p1 < cur:
        if coor[cur][0] - coor[p1][0] <= K:
            break
        temp -= coor[p1][1]
        p1 += 1

    while p2 < N-1:
        if coor[p2+1][0] - coor[cur][0] > K:
            break
        p2 += 1
        temp += coor[p2][1]

    if ans < temp:
        ans = temp

print(ans)
"""


# https://www.acmicpc.net/source/11103400
# 미리 좌표를 다 만들어두기 => python 도 이런 풀이가 속도 훨씬 빨랐음
"""
	int len = 2 * k + 1;
	int cnt = 0;
	for (int i = 0; i < len && i <= 1000000; ++i) cnt += pos[i];

	int mx = cnt;
	for (int i = 0; i + len <= 1000000; ++i) {
		cnt += pos[i + len] - pos[i];
		mx = mx < cnt ? cnt : mx;
	}

	printf("%d", mx);
"""
