/*
17566 Bus Logic

비트마스킹

예제 없이 문제 이해가 어려움
첫번째 제출이 틀린 이유:
(1) 출발지점 (m) 에 bus stop 이 없으면 아예 해당 경로를 돌 수가 없음
(2) 원형으로 도는 경로이기 때문에 (지문의 그림) 출발점 빼고는 다 포함해야함 
*/
#include <stdio.h>
int m, b, s;
int count;
char stop[51];
unsigned long long stops[51];
unsigned long long max;

int main(void)
{
	scanf("%d %d %d", &m, &b, &s);
	for (int i = 0; i < b; ++i) {
		scanf("%s", stop);
		if (stop[m-1] == '0') continue; // 틀린 이유: bus stop 없는 걸 제외를 안 함 
		for (int j = 0; j < s; ++j) {
			if (j == m-1) continue; // 틀린 이유: 원형으로 도니까 출발점 빼고는 다 포함 
			if (stop[j] == '1') stops[i] |= 1LL;
			stops[i] <<= 1LL;
		}
		max |= stops[i];
	}
	for (int j = 0; j < s; ++j) {
		if (max & 1LL) count++;
		max >>= 1LL;
	}
	printf("%d\n", count);
	return 0;
}

