/*
11005 진법 변환 2

기초 진법 변환
10 진법 to N 진법 

N 진법으로 변환했을 때 제일 긴 길이가 문제에서 주어지지 않음
0.5 초인 걸 보면 그렇게 길지 않게 설정한 것 같다.
최악을 고려해서 10 이 2의 4승은 되어야하니까 4배로 설정하였다.
=> 컴파일 안 됨;; 10억으로 변경 
=> 제출했더니 메모리 초과 나서 1억으로 변경 => 틀렸습니다 
=> int2str[0] = 0 이라고 착각했다. '0' 이어야하는데 
35 35 이런 반례 입력해보면 틀린 걸 볼 수 있다! 
*/

#include <stdio.h>

char int2str[129];
char ans[1000000000LL];
void init(void)
{
	for (int i = 0; i <= 9; ++i) int2str[i] = '0' + i;
	for (int i = 10; i <= 35; ++i) int2str[i] = 'A' + i - 10;
}

int main(void)
{
	int N, B;
	long long ind = 0LL;

	init();
	scanf("%d %d", &N, &B);
	while (N) {
		ans[ind] = int2str[N % B];
		ind += 1LL;
		N /= B;
	}
	for (long long i = 0LL; i < ind; i += 1LL) {
		printf("%c", ans[ind - 1LL - i]);
	}
	printf("\n");
	return 0;
} 
