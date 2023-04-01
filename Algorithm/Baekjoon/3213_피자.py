"""
3213 피자

수학, 그리디

- 더 깔끔하게 짜고 싶음
- 문제 이해에 어려움이 있음. 예제 1번의 답이 왜 3인지에 대해서
한 번에 이해하기 어려움
3
1/2
3/4
3/4
쪼개고 남은 조각들을 모아서 주면 안 된다. 무조건 합쳐진 크기로 줘야한다.
그래서 아래와 같이 가능한 경우를 따져서 계산하였다.

sys.stdin.readline 을 쓰면 \n 이 같이 저장되기 때문에
'/' 로 split 해도 eat 만 남지 않았다.

그래서 count 가 무조건 3/4 만 채워져있었다. 예제 1 이 우연히 답이 잘 나왔다.
"""
#import sys
#input = sys.stdin.readline
count = [0, 0, 0] # 1/4. 2/4, 3/4
ans = 0

# input & count
for n in range(int(input())):
    eat = input().split('/')
    if eat[0] == '1' and eat[1] == '2': count[1] += 1
    elif eat[0] == '1' and eat[1] == '4': count[0] += 1
    else: count[2] += 1

# 3/4 & 1/4 combination
common = min(count[0], count[2])
count[0] -= common
count[2] -= common
ans += common
ans += count[2] # remained 3/4
# 2/4 & 2/4 combination
ans += count[1]//2
count[1] %= 2
# 2/4 & 1/4 combination (full)
common = min(count[0]//2, count[1])
ans += common
count[0] -= common*2
count[1] -= common
# 2/4 & 1/4 combination
common = min(count[0], count[1])
ans += common
count[0] -= common
count[1] -= common
ans += count[1]
# 1/4 combination
ans += count[0]//4
if count[0]%4 > 0:
    ans += 1
print(ans)



# 다른 코드 예시
# https://www.acmicpc.net/source/4426292
"""
#include <cstdio>
#include <algorithm>
#include <memory.h>
int main(void) {
	int n;
	scanf("%d", &n);
	int arr[3] = { 0 };
	for (int i = 0; i < n; i++){
		int a, b;
		scanf("%d/%d", &a, &b);
		if (b == 2) arr[1]++;
		else arr[a-1]++;
	}
	int ans = std::min(arr[0], arr[2]);
	arr[0] -= ans;
	arr[2] -= ans;
	ans += arr[1] / 2 + arr[2];
	arr[1] %= 2;
	if (arr[1]) {
		ans++;
		if (arr[0] >= 2) {
			arr[1] = 0; arr[0] -= 2;
		}
		else if (arr[0] == 1) { arr[1]= arr[0] = 0; }
	}
	printf("%d", ans + (arr[0] + 3) / 4);
}
"""

# 다른 코드 예시
# https://www.acmicpc.net/source/55728646
"""
a,b,c=map(eval('input(),'*int(input())).count,['3/4','1/2','1/4'])
print(a+(b+((max(0,c-a)+1)//2)+1)//2)
"""
