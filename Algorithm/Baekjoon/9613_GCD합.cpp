/*
9613 GCD 합 

틀렸습니다.
조합(100*99/2) * n 의 수 (1000000)
= 44'950'000'000 최악의 경우 int 범위 벗어남 
=> long long으로 수정하고 맞았습니다. 

질문 게시판 반례 만들기
https://www.acmicpc.net/board/view/94840
중복된 값이 들어오는 경우가 고려 안 됨 
입력 
1
6 10 20 30 40 20 30 
정답
200 

2022.08.07 통과 
*/

#include <stdio.h>
long long arr[110];
long long ans;

long long gcd(long long x, long long y){
	return y? gcd(y, x%y) : x;
}

int main(void)
{
	int tc, n;
	scanf("%d", &tc);
	while (tc--) {
		ans = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%lld", &arr[i]);
		}
		for (int i = 0; i < n; ++i) {
			for (int j = i+1; j < n; ++j) {
				ans += gcd(arr[i], arr[j]);
			}
		}
		printf("%lld\n", ans);
	}
	return 0;
}
