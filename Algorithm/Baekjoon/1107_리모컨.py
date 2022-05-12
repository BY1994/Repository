"""
1107 리모컨

브루트포스
채널 1자리만 누르는 경우 9 가지
채널 2자리만 누르는 경우 9*9 = 81 가지
채널 3자리만 누르는 경우 9*9*9 = 729 가지
...
채널 7 자리만 누르는 경우 9**7 = 4782969가지
해당 방법마다 최소값 여부를 판단하면 1초 안에 탐색 가능
=> 그런데 아래 코드를 실행했을 때 느렸다.
왜인지는 파악하지 못했고, if count >= ans 로 가지치기 추가하니 빨라졌다.


# EOF 에러
https://www.acmicpc.net/board/view/53321
버튼이 0 개인 경우 입력 받으면 안 됨

풀이를 보니 너무 복잡하게 생각했다.
모든 경우를 for 문으로 다 돌면서 가능한지 보면 되는 듯
"""

import sys
sys.setrecursionlimit(100000000)

N = int(input())
M = int(input())
buttons = [0]*10

if M:
    broken = list(map(int, input().split()))
    for i in broken:
        buttons[i] = 1

# + 나 - 로 거기까지 가는 경우
ans = abs(N - 100)

def push(cur, count, n):
    global ans
    if count >= ans:
        return

    if count == n:
        ans = min(ans, count+abs(cur-N))
        return

    for i in range(10):
        if buttons[i] == 1:
            continue
        push(cur*10+i, count+1, n)
    

for i in range(1,8):
    for j in range(10):
        if buttons[j] == 1:
            continue
        push(j, 1, i)

print(ans)


# 1등 풀이
# https://www.acmicpc.net/source/36843948
# N 에서 한칸씩 아래로 + 한칸씩 위로 가면서 가능하면 바로 멈추기
"""
#include <cstdio>
#include <cmath>

int button[10];

bool chk(int n) {
	if (n < 0) return 0;
	while (1) {
		if (button[n % 10]) return 0;
		n /= 10;
		if (n == 0) break;
	}
	return 1;
}

int len(int n) {
	int l = 0;
	while (1) {
		l++;
		n /= 10;
		if (n == 0) break;
	}
	return l;
}

int min(int a, int b) {
	return a < b ? a : b;
}

int main() {
	int N, M; scanf("%d %d", &N, &M);
	for (int i = 1; i <= M; i++) {
		int a; scanf("%d", &a);
		button[a] = 1;
	}
	int t = abs(100 - N);
	int cnt = 0;
	while (1) {
		if (cnt >= t) break;
		if (chk(N - cnt)) {
			cnt += len(N - cnt);
			break;
		}
		else if (chk(N + cnt)) {
			cnt += len(N + cnt);
			break;
		}
		cnt++;
	}
	printf("%d", min(cnt, t));
}
"""
