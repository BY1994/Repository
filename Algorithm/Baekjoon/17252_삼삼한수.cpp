/*
17252 삼삼한 수 

수학 or brute force

3의 거듭제곱을 한번씩만 더한 수인지 판단 
틀렸습니다 => 0 을 고려하지 않음
0 은 3의 거듭제곱으로 만들 수 없기 때문에 NO 가 나와야함 

반례 찾기
https://www.acmicpc.net/board/view/39961 
최대 값 2147483647 을 넣으면 Runtime Exceed
종료 조건 변경시 해결됨 
*/

#include <stdio.h>
int main(void)
{
	int N;
	int flag = 0;
	scanf("%d", &N);
	while (N) {
		flag = 1;
		if (N % 3 == 2) {
			flag = 0;
			break;
		}
		N /= 3;
	}
	if (flag) printf("YES\n");
	else printf("NO\n");
	return 0;
}
