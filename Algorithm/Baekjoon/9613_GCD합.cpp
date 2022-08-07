/*
9613 GCD �� 

Ʋ�Ƚ��ϴ�.
����(100*99/2) * n �� �� (1000000)
= 44'950'000'000 �־��� ��� int ���� ��� 
=> long long���� �����ϰ� �¾ҽ��ϴ�. 

���� �Խ��� �ݷ� �����
https://www.acmicpc.net/board/view/94840
�ߺ��� ���� ������ ��찡 ��� �� �� 
�Է� 
1
6 10 20 30 40 20 30 
����
200 

2022.08.07 ��� 
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
