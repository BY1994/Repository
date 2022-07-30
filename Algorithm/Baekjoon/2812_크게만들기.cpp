/*
2812 크게 만들기

stack 연습
인덱스 접근에서 문제가 생기지 않을까 싶었는데
&& 나 || 는 short circuit 이라고 한다.
아스키코드로 '0' < '1' 이런 식이니까 굳이 숫자 변환하지 않고
문자열로 계산하였다.

틀렸습니다
반례
https://www.acmicpc.net/board/view/93032
10 4
7898111101
답 : 981111

10 4
7898111102
답 : 981112
==>
stack[sp] = 0 을 stack[sp-K] = 0 로 만들고 통과 
마지막에 K 가 남은 경우 소진을 시켜주는 로직 

2022.07.30 통과 
*/
#include <stdio.h>
 
int N, K;
char number[500010];
char stack[500010];
int sp;
int main(void)
{
	scanf("%d %d", &N, &K);
	scanf("%s", number);
	for (int i = 0; number[i]; ++i) {
		while (sp > 0 && K > 0 && stack[sp-1] < number[i]) {
			sp--;
			K--;
		}
		stack[sp++] = number[i];
	}
	stack[sp-K] = 0;
	printf("%s\n", stack);
	return 0;
}
